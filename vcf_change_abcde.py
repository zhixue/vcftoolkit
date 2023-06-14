#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/3/23 3:28 PM
    @Usage:
"""
import sys
import logging


def transname(a):
    if ord(a[-1]) - ord('n') <= 0 and a[0] == 'a':
        return (ord(a[0]) - 97)*26 + ord(a[-1]) - 96
    else:
        return (ord(a[0]) - 97) * 26 + ord(a[-1]) - 96 + 1

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'):
            if line.startswith("#CHROM"):
                temp = line.rstrip().split('\t')
                for i in range(9, len(temp)):
                    rawname = temp[i]
                    temp[i] = 'P' + str(transname(rawname))
                    #logging.info(temp[i] + '\t' + rawname)
                print('\t'.join(temp))
                continue
            print(line.rstrip())
        else:
            print(line.rstrip())