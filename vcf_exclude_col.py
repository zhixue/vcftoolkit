#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/3/30 4:52 PM
    @Usage: python3 vcf_exclude_col.py vcffile col1,col2,... > newvcffile
"""

import sys
excludes_cols = sys.argv[2].split(',')
care_cols = []
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('##'):
            print(line.rstrip())
        elif line.startswith('#CHROM'):
            temp = line.rstrip().split('\t')
            newtemp = []
            for i in range(len(temp)):
                if temp[i] in excludes_cols:
                    care_cols += [i]
                else:
                    newtemp += [temp[i]]
            print('\t'.join(newtemp))
        else:
            temp = line.rstrip().split('\t')
            newtemp = []
            for i in range(len(temp)):
                if i in care_cols:
                    continue
                else:
                    newtemp += [temp[i]]
            print('\t'.join(newtemp))


