#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/2/8 11:49 AM
    @Usage: python3 gfa_pggb_segfrompath.py input.gfa path_prefix use > output.S.gfa
            python3 gfa_pggb_segfrompath.py input.gfa path_prefix exclude > output.S.gfa
"""

import sys

# load path
used_segs = set()
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('P'):
            temp = line.rstrip().split('\t')
            if temp[1].startswith(sys.argv[2]):
                segs = set([x.rstrip('-').rstrip('+') for x in temp[2].split(',')])
                used_segs = used_segs.union(segs)

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('S'):
            temp = line.rstrip().split('\t')
            if sys.argv[3] == 'exclude':
                if not temp[1] in used_segs:
                    print(line.rstrip())
            else:
                if temp[1] in used_segs:
                    print(line.rstrip())
