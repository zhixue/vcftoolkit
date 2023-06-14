#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/12/17 4:12 PM
    @Usage:
"""
# python3 leftjoin.py file1 file2  output
import sys


f2_dict = dict()
with open(sys.argv[2]) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        if temp[0] not in f2_dict:
            f2_dict[temp[0]] = [temp[1]]
        else:
            f2_dict[temp[0]] += [temp[1]]

i = 0
success_i = 0
fout = open(sys.argv[3],'w')
with open(sys.argv[1]) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        i += 1
        #if i == 1:
        #    continue
        colkey = temp[0]
        sample = temp[1]
        flag = 0
        addcols = '.'

        if colkey in f2_dict:
            if sample in f2_dict[colkey]:
                addcols = '1'
                success_i += 1
                flag = 1
        elif colkey.split('.')[0] in f2_dict:
            if sample in f2_dict[colkey.split('.')[0]]:
                addcols = '1'
                success_i += 1
                flag = 2
        elif colkey.lstrip('rna-gnl|WGS_SDMP|mrna.') in f2_dict:
            if sample in f2_dict[colkey.lstrip('rna-gnl|WGS_SDMP|mrna.')]:
                addcols = '1'
                success_i += 1
                flag = 3
        elif colkey.replace('.','') in f2_dict:
            if sample in f2_dict[colkey.replace('.','')]:
                addcols = '1'
                success_i += 1
                flag = 4
        elif len(colkey.split('g')) > 1:
            tifrunner_colkey = 'gnm2.' + colkey.split('g')[1]
            if tifrunner_colkey in f2_dict:
                if sample in f2_dict[tifrunner_colkey]:
                    addcols = '1'
                    success_i += 1
                    flag = 5


        if colkey == 'KB01gM3RAJ.1':
            print(colkey + ' ' + addcols)
            print(flag)
        fout.write(line.rstrip() + '\t' + addcols + '\n')
        #if addcols != '.':
        #    for addcol in addcols.split(';;'):
        #        if addcol != '':
        #            fout.write('\t'.join([temp[0], temp[3], addcol.split('::')[0],addcol.split('::')[1]]))
fout.close()
print('Read line, write line')
print(i)
print(success_i)
