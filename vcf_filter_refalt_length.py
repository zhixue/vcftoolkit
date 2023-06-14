#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/10/26 7:00 PM
    @Usage: python3 raw.vcf > sv.vcf
"""
import sys

minlen = 50
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'):
            print(line.rstrip())
            continue
        temp = line.rstrip().split('\t')
        ref = temp[3]
        alts = temp[4]
        lenref = len(ref)
        maxlenalts = max([len(x) for x in alts.split(',')])
        minlenalts = min([len(x) for x in alts.split(',')])
        if abs(lenref - maxlenalts) >= minlen or abs(lenref - minlenalts) >= minlen:
            print(line.rstrip())

