python-titlecase
================

This is a (minor) update and repackaging of Stuart Colville's
(`<http://muffinresearch.co.uk>`_) Python port of
John Gruber's (`<http://daringfireball.net/>`_) ``titlecase`` Perl library.

Changes
-------

In this version, ``titlecase`` takes two optional arguments, ``uppercase``
and ``lowercase``, which should be functions that take a string and return an
uppercase (resp. lowercase) version of the string. I use it for wrapping
the initial uppercase character in a ``<span />`` on a different project.

It's also packaged up for easier use with that project; it's not really
meant to go to PyPI. 
