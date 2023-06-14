#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/3/28 10:15 AM
    @Usage:
"""
import sys

sample = ''
nump = dict()
numa = dict()
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('# '):
            if sample != '':
                print('\t'.join([sample, 'All', numa[sample]]).rstrip())
                print('\t'.join([sample, 'Primary', nump[sample]]).rstrip())
            sample = line.rstrip().split(' ')[-1].split('.')[0]
        elif line.startswith('##'):
            stype = line.rstrip().split(' ')[-1]
        else:
            num, chrn = line.lstrip().rstrip().split(' ')
            if stype == 'All':
                if sample not in numa:
                    numa[sample] = ''
                numa[sample] += chrn + '\t' + num + '\t'
            else:
                if sample not in nump:
                    nump[sample] = ''
                nump[sample] += chrn + '\t' + num + '\t'

    print('\t'.join([sample, 'All', numa[sample]]).rstrip())
    print('\t'.join([sample, 'Primary', nump[sample]]).rstrip())
