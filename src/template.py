#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os
import subprocess

def run_shell_command(cmd,redirect='stdout'):
    """
    redirect=
        null   - redirect to null
        stdout - save output & print to screen
        *      - save output but do not print to screen
    """
    cmd_list=cmd.split()
    if redirect=='null':
        try:
            from subprocess import DEVNULL  # Python 3.3+
        except ImportError:
            DEVNULL = open(os.devnull, 'wb')
        process = subprocess.Popen(cmd_list,shell=False,
                  stdout=DEVNULL,stderr=DEVNULL)
        process.communicate()
        return '','',process.returncode
    else:
        process = subprocess.Popen(cmd_list,shell=False,
                  stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out,err = process.communicate()
        if redirect=='stdout':
            if out:
                print(out.decode())
            if err:
                print(err.decode())
        return out.decode(),err.decode(),process.returncode

def main(filename=None):
    print("Hello world!")
    if os.path.isfile(filename) is not True:
        file_status = ' (file does not exist)'
    else:
        file_status = ''
    print("Input File = '{}'{}".format(filename,file_status))

    _, file_ext = os.path.splitext(filename)
    if file_ext not in ['.txt','.text']:
        print("File extension '{}' is invalid".format(file_ext))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Starting Template for Python 3 Programs')
    parser.add_argument('file',help='Input file')
    args = parser.parse_args()

    main(args.file)
