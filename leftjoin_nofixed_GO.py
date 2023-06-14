#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/11/25 4:01 PM
    @Usage:
"""
# python3 leftjoin.py file1 file1_col file2 file2_col output
import sys


f2_dict = dict()
with open(sys.argv[3]) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        if '::'.join(line.rstrip().split('\t')[2:4]) == '':
            continue
        if temp[int(sys.argv[4])-1] not in f2_dict:
            f2_dict[temp[int(sys.argv[4])-1]] = ['GO:' + '::'.join(line.rstrip().split('\t')[2:4])]
        else:
            if 'GO:' + '::'.join(line.rstrip().split('\t')[2:4]) not in f2_dict[temp[int(sys.argv[4])-1]]:
                f2_dict[temp[int(sys.argv[4]) - 1]] += ['GO:' + '::'.join(line.rstrip().split('\t')[2:4])]

i = 0
success_i = 0
fout = open(sys.argv[5],'w')
with open(sys.argv[1]) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        i += 1
        if i == 1:
            continue
        colkey = temp[int(sys.argv[2])-1]
        if colkey in f2_dict:
            addcols = ';;'.join(f2_dict[colkey]) + ';;'
            success_i += 1
        elif colkey.split('.')[0] in f2_dict:
            addcols = ';;'.join(f2_dict[colkey.split('.')[0]]) + ';;'
            success_i += 1
        elif colkey.lstrip('rna-gnl|WGS_SDMP|mrna.') in f2_dict:
            addcols = ';;'.join(f2_dict[colkey.lstrip('rna-gnl|WGS_SDMP|mrna.')]) + ';;'
            success_i += 1
        elif colkey.replace('.','') in f2_dict:
            addcols = ';;'.join(f2_dict[colkey.replace('.','')]) + ';;'
            success_i += 1
        elif len(colkey.split('g')) > 1:
            tifrunner_colkey = 'gnm2.' + colkey.split('g')[1]
            if tifrunner_colkey in f2_dict:
                addcols = ';;'.join(f2_dict[tifrunner_colkey]) + ';;'
                success_i += 1
        else:
            addcols = '.'
        # fout.write(line.rstrip() + '\t' + addcols + '\n')
        if addcols != '.':
            for addcol in addcols.split(';;'):
                if addcol != '':
                    fout.write('\t'.join([temp[0], temp[3], addcol.split('::')[0],addcol.split('::')[1]]))
fout.close()
print('Read line, write line')
print(i)
print(success_i)
