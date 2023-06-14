#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/3/15 8:17 PM
    @Usage: python3 vcf_filter_svlen.py xx.vcf min_svlen max_svlen > xxxa.vcf
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

minsvlen = int(sys.argv[2])
maxsvlen = int(sys.argv[3])

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'):
            print(line.rstrip())
            continue
        temp = line.rstrip().split('\t')
        info = temp[7]
        info_dic = string2dict(info)
        if 'SVLEN' in info_dic:
            svlen = int(info_dic['SVLEN'])
        else:
            if 'END' in info_dic:
                svlen = int(info_dic['END']) - int(temp[1]) + 1
            else:
                print('ERROR')
                exit()
        if abs(svlen) >= minsvlen and abs(svlen) <= maxsvlen:
            print(line.rstrip())
