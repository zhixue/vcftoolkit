#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/5/30 9:33 AM
    @Usage: python3 vcf_random_select.py raw.vcf number > new.vcf
"""
import sys
import random

rawvcf = sys.argv[1]
output_n = int(sys.argv[2])
SEED = 4214
random.seed(4214)

input_n = 0
with open(rawvcf) as f:
    for line in f:
        if line.startswith('#'):
            continue
        else:
            input_n += 1


a = [i for i in range(input_n)]
random.shuffle(a)
choose_lines = set(a[:output_n])

i = 0
with open(rawvcf) as f:
    for line in f:
        if line.startswith('#'):
            print(line.rstrip())
        else:
            i += 1
            if i in choose_lines:
                print(line.rstrip())
