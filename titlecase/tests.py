#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for python-titlecase.
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

from titlecase import titlecase

def test_all_caps_regex():
    """Test - all capitals regex"""
    from titlecase import ALL_CAPS
    return bool(ALL_CAPS.match('THIS IS ALL CAPS')) is True

def test_initials_regex():
    """Test - uppercase initals regex with A.B"""
    from titlecase import UC_INITIALS
    return bool(UC_INITIALS.match('A.B')) is True

def test_initials_regex_2():
    """Test - uppercase initals regex with A.B."""
    from titlecase import UC_INITIALS
    return bool(UC_INITIALS.match('A.B.')) is True

def test_initials_regex_3():
    """Test - uppercase initals regex with ABCD"""
    from titlecase import UC_INITIALS
    return bool(UC_INITIALS.match('ABCD')) is False

def test_titlecase_with_replacement(input, output):
    text = titlecase(input, uppercase=lambda x: ('|%s|' % x.upper()))
    if not text == output:
        print "failure:\n\texpected: %s\n\tactual: %s" % (text, output)
        return False
    return True

def test_titlecase(input, output):
    text = titlecase(input)
    if not text == output:
        print "failure:\n\texpected: %s\n\tactual: %s" % (text, output)
        return False
    return True

# Each test is a pair of 
TESTS = [
    (
        test_all_caps_regex, []
    ),
    (
        test_initials_regex, []
    ),
    (
        test_initials_regex_2, []
    ),
    (
        test_initials_regex_3, []
    ),
    (
        test_titlecase_with_replacement, [
            "You're a nerd, bozo.",
            "|Y|ou're a |N|erd, |B|ozo."
        ]
    ),
    (
        test_titlecase, [
            "word/word",
            "Word/Word"
        ],
    ),
    (
        test_titlecase, [ 
            "dance with me/let‚Äôs face the music and dance",
            "Dance With Me/Let‚Äôs Face the Music and Dance"
        ]
    ),
    (
        test_titlecase, [
            "34th 3rd 2nd",
            "34th 3rd 2nd"
        ]
    ),
    (
        test_titlecase, [
            "Q&A with steve jobs: 'that's what happens in technology'",
            "Q&A With Steve Jobs: 'That's What Happens in Technology'"
        ]
    ),
    (
        test_titlecase, [
            "What is AT&T's problem?",
            "What Is AT&T's Problem?"
        ]
    ),
    (
        test_titlecase, [
            "Apple deal with AT&T falls through",
            "Apple Deal With AT&T Falls Through"
        ]
    ),
    (
        test_titlecase, [
            "this v that",
            "This v That"
        ]
    ),
    (
        test_titlecase, [
            "this v. that",
            "This v. That"
        ]
    ),
    (
        test_titlecase, [
            "this vs that",
            "This vs That"
        ]
    ),
    (
        test_titlecase, [
            "this vs. that",
            "This vs. That"
        ]
    ),
    (
        test_titlecase, [
            "The SEC's Apple probe: what you need to know",
            "The SEC's Apple Probe: What You Need to Know"
        ]
    ),
    (
        test_titlecase, [
            "'by the Way, small word at the start but within quotes.'",
            "'By the Way, Small Word at the Start but Within Quotes.'"
        ]
    ),
    (
        test_titlecase, [
            "Small word at end is nothing to be afraid of",
            "Small Word at End Is Nothing to Be Afraid Of"
        ]
    ),
    (
        test_titlecase, [
            "Starting Sub-Phrase With a Small Word: a Trick, Perhaps?",
            "Starting Sub-Phrase With a Small Word: A Trick, Perhaps?"
        ]
    ),
    (    
        test_titlecase, [
            "Sub-Phrase With a Small Word in Quotes: 'a Trick, Perhaps?'",
            "Sub-Phrase With a Small Word in Quotes: 'A Trick, Perhaps?'"
        ]
    ),
    (
        test_titlecase, [
            'sub-phrase with a small word in quotes: "a trick, perhaps?"',
            'Sub-Phrase With a Small Word in Quotes: "A Trick, Perhaps?"'
        ]
    ),
    (
        test_titlecase, [
            '"Nothing to Be Afraid of?"',
            '"Nothing to Be Afraid Of?"'
        ]
    ),
    (
        test_titlecase, [
            '"Nothing to be Afraid Of?"',
            '"Nothing to Be Afraid Of?"'
        ]    
    ),
    (   
        test_titlecase, [
            'a thing',
            'A Thing'
        ]
    ),
    (
        test_titlecase, [
            "2lmc Spool: 'gruber on OmniFocus and vapo(u)rware'",
            "2lmc Spool: 'Gruber on OmniFocus and Vapo(u)rware'"
        ]
    ),
    (
        test_titlecase, [
            'this is just an example.com',
            'This Is Just an example.com'
        ]
    ),
    (
        test_titlecase, [
            'this is something listed on del.icio.us',
            'This Is Something Listed on del.icio.us'
        ]
    ),
    (
        test_titlecase, [
            'iTunes should be unmolested',
            'iTunes Should Be Unmolested'
        ]
    ),
    (
        test_titlecase, [
            'reading between the lines of steve jobs‚Äôs ‚Äòthoughts on music‚Äô',
            'Reading Between the Lines of Steve Jobs‚Äôs ‚ÄòThoughts on Music‚Äô'
        ]
    ),
    (
        test_titlecase, [
            'seriously, ‚Äòrepair permissions‚Äô is voodoo',
            'Seriously, ‚ÄòRepair Permissions‚Äô Is Voodoo'
        ]
    ),
    (
        test_titlecase, [
            'generalissimo francisco franco: still dead; kieren McCarthy: still a jackass',
            'Generalissimo Francisco Franco: Still Dead; Kieren McCarthy: Still a Jackass'
        ]
    ),
    (
        test_titlecase, [
            "O'Reilly should be untouched",
            "O'Reilly Should Be Untouched"
        ]
    ),
    (
        test_titlecase, [
            "my name is o'reilly",
            "My Name Is O'Reilly"
        ]
    ),
    (
        test_titlecase, [
            "WASHINGTON, D.C. SHOULD BE FIXED BUT MIGHT BE A PROBLEM",
            "Washington, D.C. Should Be Fixed but Might Be a Problem"
        ]
    ),
    (
        test_titlecase, [
            "THIS IS ALL CAPS AND SHOULD BE ADDRESSED",
            "This Is All Caps and Should Be Addressed"
        ]
    ),
    (
        test_titlecase, [
            "Mr McTavish went to MacDonalds",
            "Mr McTavish Went to MacDonalds"
        ]
    ),
    (
        test_titlecase, [
            "this shouldn't\nget mangled",
            "This Shouldn't\nGet Mangled"
        ]
    ),
    ( 
        test_titlecase, [
            "this is http://foo.com",
            "This Is http://foo.com"
        ]
    ),
]
       
if __name__ == "__main__":
    successes = 0
    failures = 0
    for (test, args) in TESTS:
        if test(*args):
            successes += 1
        else:
            failures += 1
    print "%i successes, %i failures" % (successes, failures)
    exit(failures)
