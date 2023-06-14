#!/usr/bin/env python vcf_info gene_dividemultline.py in.vcf > table.tsv
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/8/19 4:17 PM
    @Usage:
"""
import sys

def string2dict(long_string, sep=';', eq='=', rm_quote=False):
    if rm_quote:
        long_string = long_string.replace('"', '').replace("'", '')
    long_string = long_string.replace('; ', ';')
    out_dict = dict()
    tmp = long_string.rstrip(sep).split(sep)
    for i in tmp:
        if len(i.split(eq)) == 2:
            key, value = i.split(eq)
        else:
            key = i.split(eq)[0]
            value = eq.join(i.split(eq)[1:])
        out_dict[key] = value
    return out_dict

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'):
            continue
        else:
            temp = line.rstrip().split('\t')
            info = string2dict(temp[7])
            if 'olp_gene' in info or 'olp_ud3k' in info:
                if 'olp_gene' in info:
                    geneids = info['olp_gene'].split(',')
                else:
                    geneids = list(set([x.split('.')[0] for x in info['olp_ud3k'].split(',')]))
                summaryolpinfo = temp[7].split('STRANDS=+-;')[1]
                svsupp = info['SUPP']
                svlen = info['SVLEN']
                svtype = info['SVTYPE']
                for gene in geneids:
                    print('\t'.join([temp[2], svsupp, svlen, svtype, gene, summaryolpinfo]))

