#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/1/12 3:50 PM
    @Usage: python3 merge_GroupSpecific_inf.py raw_inf.tsv col GroupSpecific.table > new.tsv
"""

import sys


gs_dict = dict()
with open(sys.argv[3]) as f:
    for line in f:
        if line.startswith('GF'):
            continue
        if line.startswith('SV'):
            continue
        temp = line.rstrip().split('\t')
        ftid = temp[0]
        gs = temp[1]
        if ftid not in gs_dict:
            gs_dict[ftid] = gs
        else:
            gs_dict[ftid] += ',' + gs

col = int(sys.argv[2])
with open(sys.argv[1]) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        if temp[col - 1] in gs_dict:
            print(line.rstrip() + '\t' + gs_dict[temp[col - 1]])

