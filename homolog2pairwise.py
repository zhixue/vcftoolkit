#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/11/30 10:34 AM
    @Usage: python3 homolog2pairwise.py homolog_group.txt > homolog_pairwise.txt
"""
from itertools import combinations
import sys

with open(sys.argv[1]) as f:
    for line in f:
        temp = line.rstrip().split(' ')
        for itempair in combinations(temp, 2):
            print(' '.join(itempair))

