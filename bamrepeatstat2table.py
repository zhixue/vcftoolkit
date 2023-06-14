#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/4/2 3:13 PM
    @Usage:
"""
import sys

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('# '):
            print()
            sample = line.rstrip().split()[1]
            print(sample.rstrip('.bam'), end='\t')
        elif line.startswith('##'):
            colna = line.rstrip().split()[1]
        else:
            print(line.rstrip(), end='\t')
