#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/3/28 10:41 AM
    @Usage:
"""
import sys

sample = ''
nums = []
print('\t'.join(['# Sample', 'Total Read', 'Primary', 'Secondary', 'Supplementary', 'Duplicates',
                 'Primary duplicates', 'Mapped', 'Mapped%', 'Primary mapped', 'Primary mapped%',
                 'Paired', 'Read1', 'Read2', 'Properly mapped', 'Properly mapped%', 'Selfmate mapped',
                 'Singleton', 'Singleton%', 'Mate to different chr', 'Mate to different chr(MAPQ>=5)']))
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('# '):
            if sample != '':
                print('\t'.join([sample] + nums).rstrip())
                print('\t'.join([sample] + nums).rstrip())
            sample = line.rstrip().split(' ')[-1].split('.')[0]
            nums = []
        else:
            temp = line.rstrip().split(' ')
            nums += [temp[0]]
            if ':' in temp:
                for i in temp:
                    if i.startswith('('):
                        nums += [i[1:]]

