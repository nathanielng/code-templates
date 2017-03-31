#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import argparse

def main(filename=None):
    print("Hello world!")
    if os.path.isfile(filename) is not True:
        file_status = ' (file does not exist)'
    else:
        file_status = ''
    print("Input File = '{}'{}".format(filename,file_status))

    _, file_ext = os.path.splitext(filename)
    if not file_ext in ['.txt','.text']:
        print("File extension '{}' is invalid".format(file_ext))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Starting Template for Python 3 Programs')
    parser.add_argument('file',help='Input file')
    args = parser.parse_args()

    main(args.file)
