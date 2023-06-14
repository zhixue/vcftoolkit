#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/3/21 8:07 PM
    @Usage:
"""
MAXMISSFRAC = 0.5

import sys

samplen = 0

typesx = []
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'):
            print(line.rstrip())
            if line.startswith("#CHROM"):
                samplen = len(line.rstrip().split('\t')) - 9
        else:
            temp = line.rstrip().split('\t')
            summiss = 0
            sumcall = 0
            for i in range(9,len(temp)):
                if temp[i][:3] not in typesx:
                    typesx.append(temp[i][:3])
                if temp[i].startswith('./.'):
                    summiss += 1
                else:
                    sumcall += 1
            #if summiss / samplen > MAXMISSFRAC:
            if sumcall > summiss:
                if temp[0].startswith('Sca'):
                    continue
                print('\t'.join(temp))
