#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/11/2 8:59 PM
    @Usage:
"""

import sys

lt = sys.argv[1]
gfc = sys.argv[2]


gflist = []
with open(lt) as f:
    for line in f:
        gflist += [line.rstrip()]


with open(gfc) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        if temp[0] in gflist:
            ndgenes = temp[7].split(',')
            for g in ndgenes:
                print(temp[0] + '\t' + g)

