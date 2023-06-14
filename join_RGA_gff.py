#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/11/17 6:39 PM
    @Usage: python3 join_RGA_gff.py NDH108_rgaugury.RGA.info.txt gene.gff > rgagene.bed
"""
import sys

rga_dict = dict()
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('ID'):
            continue
        temp = line.rstrip().split('\t')
        gene = temp[0].split('.')[0]
        rgatype = temp[2]
        if not gene in rga_dict:
            rga_dict[gene] = set([rgatype])
        else:
            if not rgatype in rga_dict[gene]:
                rga_dict[gene].add(rgatype)

with open(sys.argv[2]) as f:
    for line in f:
        if line.startswith('#'):
            continue
        temp = line.rstrip().split('\t')
        if temp[2] == 'gene':
            gene = temp[8].split(';')[0].split('=')[1]
            if gene in rga_dict:
                print('\t'.join([temp[0],temp[3],temp[4],gene,','.join(rga_dict[gene])]))





