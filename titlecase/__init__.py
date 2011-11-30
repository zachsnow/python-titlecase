#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Original Perl version by: John Gruber http://daringfireball.net/ 10 May 2008
Python version by Stuart Colville http://muffinresearch.co.uk
Modified by Zach Snow http://zachsnow.com
License: http://www.opensource.org/licenses/mit-license.php
"""

import re

__all__ = ['titlecase']
__version__ = '0.5.3'

SMALL = 'a|an|and|as|at|but|by|en|for|if|in|of|on|or|the|to|v\.?|via|vs\.?'
PUNCT = r"""!"#$%&'‚Äò()*+,\-./:;?@[\\\]_`{|}~"""

SMALL_WORDS = re.compile(r'^(%s)$' % SMALL, re.I)
INLINE_PERIOD = re.compile(r'[a-z][.][a-z]', re.I)
UC_ELSEWHERE = re.compile(r'[%s]*?[a-zA-Z]+[A-Z]+?' % PUNCT)
CAPFIRST = re.compile(r"^[%s]*?([A-Za-z])" % PUNCT)
SMALL_FIRST = re.compile(r'^([%s]*)(%s)\b' % (PUNCT, SMALL), re.I)
SMALL_LAST = re.compile(r'\b(%s)[%s]?$' % (SMALL, PUNCT), re.I)
SUBPHRASE = re.compile(r'([:.;?!][ ])(%s)' % SMALL)
APOS_SECOND = re.compile(r"^[dol]{1}['‚Äò]{1}[a-z]+$", re.I)
ALL_CAPS = re.compile(r'^[A-Z\s%s]+$' % PUNCT)
UC_INITIALS = re.compile(r"^(?:[A-Z]{1}\.{1}|[A-Z]{1}\.{1}[A-Z]{1})+$")
MAC_MC = re.compile(r"^([Mm]a?c)(\w+)")

def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

def titlecase(text, uppercase=uppercase, lowercase=lowercase):

    """
    Titlecases input text

    This filter changes all words to Title Caps, and attempts to be clever
    about *un*capitalizing SMALL words like a/an/the in the input.

    The list of "SMALL words" which are not capped comes from
    the New York Times Manual of Style, plus 'vs' and 'v'.

    """
    def capitalize(text, uppercase=uppercase):
        """
        Capitalize a word, ignoring initial punctuation.
        """
        return CAPFIRST.sub(lambda m: uppercase(m.group(0)), text)
    
    lines = re.split('[\r\n]+', text)
    processed = []
    for line in lines:
        all_caps = ALL_CAPS.match(line)
        words = re.split('[\t ]', line)
        tc_line = []
        for word in words:
            if all_caps:
                if UC_INITIALS.match(word):
                    tc_line.append(word)
                    continue
                else:
                    word = lowercase(word)
            
            if APOS_SECOND.match(word):
                word = word.replace(word[0], uppercase(word[0]))
                word = word.replace(word[2], uppercase(word[2]))
                tc_line.append(word)
                continue
            if INLINE_PERIOD.search(word) or UC_ELSEWHERE.match(word):
                tc_line.append(word)
                continue
            if SMALL_WORDS.match(word):
                tc_line.append(lowercase(word))
                continue

            match = MAC_MC.match(word)
            if match:
                tc_line.append("%s%s" % (capitalize(match.group(1)),
                                      capitalize(match.group(2))))
                continue

            if "/" in word and not "//" in word:
                slashed = []
                for item in word.split('/'):
                    slashed.append(capitalize(item))
                tc_line.append("/".join(slashed))
                continue

            hyphenated = []
            for item in word.split('-'):
                hyphenated.append(capitalize(item))
            tc_line.append("-".join(hyphenated))

        result = " ".join(tc_line)

        result = SMALL_FIRST.sub(lambda m: '%s%s' % (
            m.group(1),
            capitalize(m.group(2))
        ), result)

        result = SMALL_LAST.sub(lambda m: capitalize(m.group(0)), result)

        result = SUBPHRASE.sub(lambda m: '%s%s' % (
            m.group(1),
            capitalize(m.group(2))
        ), result)
        
        processed.append(result)

    return "\n".join(processed)
