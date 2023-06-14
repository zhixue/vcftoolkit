#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/12/22 12:53 PM
    @Usage: python3 RGA_summary_chr.py xx.RGA.info.txt REG_split_char
"""
# e.g. python3 RGA_summary_chr.py Adu.RGA.info.txt G
import sys


gene_chr_dict = dict()
protein_chr_dict = dict()

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('ID'):
            continue
        temp = line.rstrip().split('\t')
        protein = temp[0]
        gene = protein.split('.')[0]
        rga_type = temp[2]
        chrn = gene.split(sys.argv[2])[0]

        if chrn not in gene_chr_dict:
            gene_chr_dict[chrn] = dict()
        if chrn not in protein_chr_dict:
            protein_chr_dict[chrn] = dict()

        if rga_type not in gene_chr_dict[chrn]:
            gene_chr_dict[chrn][rga_type] = set()
        if rga_type not in protein_chr_dict[chrn]:
            protein_chr_dict[chrn][rga_type] = set()

        gene_chr_dict[chrn][rga_type].add(gene)
        protein_chr_dict[chrn][rga_type].add(protein)

rga_print_list = ['NBS>NBS', 'NBS>CNL', 'NBS>TNL', 'NBS>CN', 'NBS>TN',
              'NBS>NL', 'NBS>TX', 'NBS>RNL', 'NBS>RN', 'NBS>Others',
              'RLP', 'RLK', 'TM-CC', 'RPW8']
# gene
print('### Gene')
for chrn in sorted(gene_chr_dict.keys()):
    print(chrn,end=' ')
    for rga_type in rga_print_list:
        if rga_type in gene_chr_dict[chrn]:
            print(len(gene_chr_dict[chrn][rga_type]), end=' ')
        else:
            print(0, end=' ')
    print('')

print('### Protein')
for chrn in sorted(protein_chr_dict.keys()):
    print(chrn,end=' ')
    for rga_type in rga_print_list:
        if rga_type in protein_chr_dict[chrn]:
            print(len(protein_chr_dict[chrn][rga_type]), end=' ')
        else:
            print(0, end=' ')
    print('')

