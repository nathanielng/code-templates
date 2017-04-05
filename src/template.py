#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import argparse

def run_shell_command(cmd,redirect='stdout'):
    cmd_list=cmd.split()
    if redirect is None or redirect=='null':
        try:
            from subprocess import DEVNULL  # py3k
        except ImportError:
            DEVNULL = open(os.devnull, 'wb')
        server = subprocess.Popen(cmd_list,shell=False,
                 stdout=DEVNULL,stderr=DEVNULL)
    else:
        server = subprocess.Popen(cmd_list,shell=False,
                 stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    out,err = server.communicate()
    if out:
        print(out)
    if err:
        print(err)
    exit_code=server.returncode
    return out,err,exit_code

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
