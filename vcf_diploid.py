#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/3/16 4:06 PM
    @Usage:
"""

import sys

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'):
            print(line.rstrip())
        else:
            temp = line.rstrip().split('\t')
            for i in range(9,len(temp)):
                temp[i] = temp[i] + '|' + temp[i]
            print('\t'.join(temp))
            
