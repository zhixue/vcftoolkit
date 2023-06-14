#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/12/3 2:43 PM
    @Usage: python3 grep_addone.py raw.txt grep.list newcolname > new.txt
"""

import sys

grep_list = []
with open(sys.argv[2]) as f:
    for line in f:
        grep_list += [line.rstrip().split('.')[0]]

i = 0
with open(sys.argv[1]) as f:
    for line in f:
        i += 1
        if i == 1:
            print(line.rstrip() + '\t' + sys.argv[3])
        if line.startswith('ID'):
            continue
        temp = line.rstrip().split('\t')
        grep_flag = 0
        for item in grep_list:
            if item in temp[5]:
                grep_flag = 1
                print(line.rstrip() + '\t' + '1')
                break
        if grep_flag == 0:
            print(line.rstrip() + '\t' + '0')

