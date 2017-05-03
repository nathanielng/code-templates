#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import matplotlib

def create_color_list():
    color_names = matplotlib.colors.cnames
    color_list  = []
    for key,value in color_names.items():
        ivalue = int(value[1:], 16)
        rvalue = int(value[1:3],16)
        gvalue = int(value[3:5],16)
        bvalue = int(value[5:], 16)
        color_list.append([key, value, ivalue, rvalue, gvalue, bvalue])
    return color_list

def sort_color_list(color_list, sort_index):
    return sorted(color_list, key=lambda c: c[sort_index])

def print_color_list(color_list,sort_order=None):
    if sort_order=='alphabetical':
        sorted_list = sort_color_list(color_list, sort_index=0)
    elif sort_order=='value':
        sorted_list = sort_color_list(color_list, sort_index=2)
    elif sort_order=='red':
        sorted_list = sort_color_list(color_list, sort_index=3)
    elif sort_order=='green':
        sorted_list = sort_color_list(color_list, sort_index=4)
    elif sort_order=='blue':
        sorted_list = sort_color_list(color_list, sort_index=5)
    else:
        # No sort order
        for item in color_list:
            key, value, ivalue, r, g, b = item
            print('{0}: {1}'.format(value,key))
        return

    for item in sorted_list:
        key, value, ivalue, r, g, b = item
        print('{0}: {1}'.format(value,key))

if __name__ == "__main__":
    color_list  = create_color_list()
    print_color_list(color_list,sort_order='alphabetical')
