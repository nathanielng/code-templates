#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

# To test this module:
# python -m unittest -v nested

def string_maxlen(txt,max_len=12):
    n = len(txt)
    if n <= max_len:
        return txt
    elif n > max_len-3:
        return txt[:(max_len-3)] + '...'

# python -m unittest -v nested.TestStringMaxLength
class TestStringMaxLength(unittest.TestCase):
    def test_short_strings(self):
        self.assertEqual(string_maxlen('abcdefghij'),     'abcdefghij')
        self.assertEqual(string_maxlen('abcdefghijk'),    'abcdefghijk')
        self.assertEqual(string_maxlen('abcdefghijkl'),   'abcdefghijkl')

    def test_long_strings(self):
        self.assertEqual(string_maxlen('abcdefghijklm'),  'abcdefghi...')
        self.assertEqual(string_maxlen('abcdefghijklmn'), 'abcdefghi...')

def print_structure(elmt,level=0,max_level=5):
    txt=''
    if level > max_level:
        return txt

    whitespace = " " * (level * 2)
    if isinstance(elmt, (dict)) is True:
        for k in elmt.keys():
            if type(elmt[k])==int:
                txt += whitespace + "+'{0}': {1}\n".format(k,elmt[k])
            elif type(elmt[k])==str:
                my_str=elmt[k][:40]
                txt += whitespace + "+'{0}': '{1}'\n".format(k,my_str)
            else:
                txt += whitespace + "+'{0}': {1}\n".format(k,type(elmt[k]))
                txt += print_structure(elmt[k],level+1,max_level=max_level)
    elif isinstance(elmt, (list)) is True:
        txt += whitespace + "+[list]\n"
        if len(elmt) > 0:
            txt += print_structure(elmt[0],level+1,max_level=max_level)
    else:
        pass
    return txt

# python -m unittest -v nested.TestPrintStructure
class TestPrintStructure(unittest.TestCase):
    def test_dict_int(self):
        d = {'integer': 123}
        self.assertEqual(print_structure(d),"+'integer': 123\n")

    def test_dict_string(self):
        d = {'string': 'abc'}
        self.assertEqual(print_structure(d),"+'string': 'abc'\n")

    def test_dict_list(self):
        d = {'list': [1,2,3]}
        self.assertEqual(print_structure(d),"+'list': <class 'list'>\n  +[list]\n")

if __name__ == "__main__":
    unittest.main()
