#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest
import re

# To test this module:
# python -m unittest -v regex_numbers

str_regex_ints=r'[+-]?[0-9]+'
str_regex_fixed =r'[+-]?[0-9]+\.[0-9]+'
str_regex_exp   =r'[+-]?[0-9]+\.[0-9]+[eEdD][+-]?[0-9]+'
str_regex_float =r'([+-]?[0-9]+(\.[0-9]+)?)([eEdD]([+-]?[0-9]+))?'

regex_ints   = re.compile(str_regex_ints)
regex_fixed  = re.compile(str_regex_fixed)
regex_exp    = re.compile(str_regex_exp)
regex_floats = re.compile(str_regex_float)

def get_ints(txt):
    matches = regex_ints.findall(txt)
    return [ int(x) for x in matches ]

def get_fixed(txt):
    matches = regex_fixed.findall(txt)
    return [ float(x) for x in matches ]

def get_floats(txt):
    matches = regex_floats.findall(txt)
    return [ float(x[0]+'e'+x[3]) for x in matches ]

def print_matches(matches):
    print('Number of matches: {0}'.format(len(matches)))
    for i,match in enumerate(matches):
        if type(match)==tuple:
            print("{0}: '{1}'".format(i,match[0]+'e'+match[3]))
        else:
            print("{0}: '{1}'".format(i,match))

class TestStringMaxLength(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(get_ints('123 +123 -123'), [123,123,-123])
        self.assertEqual(get_ints(' abc def \nghi jkl'), [])

    def test_fixed(self):
        self.assertEqual(get_fixed('1234.5678 -1234.5678'), [1234.5678, -1234.5678])
        self.assertEqual(get_fixed(' abc def \nghi jkl'), [])

    def test_floats(self):
        self.assertEqual(get_floats('1234.5678e+9 -1.2345678E-9 +1.2345678D+9'),
            [ 1234.5678e+9, -1.2345678e-9, +1.2345678e+9])
        self.assertEqual(get_floats(' abc def \nghi jkl'), [])

if __name__ == "__main__":
    print_matches(regex_ints.findall('123 +123 -123'))
    print_matches(regex_floats.findall('1234.5678e+9 -1.2345678E-9 +1.2345678D+9'))
    unittest.main()
