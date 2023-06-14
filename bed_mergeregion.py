#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/3/6 5:10 PM
    @Usage: python3 bed_mergeregion.py raw.bed > new.bed
"""

import sys

last_chr = ''
last_start = 0
last_end = 0
with open(sys.argv[1]) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        chrn = temp[0]
        start_pos = temp[1]
        end_pos = temp[2]
        if last_chr != chrn:
            if last_chr != '':
                print('\t'.join([str(x) for x in [last_chr, last_start, last_end, 1]]))
            # new chr, init
            last_chr = chrn
            last_start = start_pos
            last_end = end_pos
            continue
        if last_end != start_pos:
            print('\t'.join([str(x) for x in [last_chr, last_start, last_end, 1]]))
            last_start = start_pos
        last_end = end_pos

    # last one
    print('\t'.join([str(x) for x in [last_chr, last_start, last_end, 1]]))
