#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/12/7 10:09 AM
    @Usage: python3 leftjoin_nofixed_kaks_gfinf.py raw.kaks gf.txt new.kaks
"""
import sys


f2_dict = dict()
with open(sys.argv[2]) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        f2_dict[temp[0].split('.')[0]] = [temp[2], temp[3], temp[1],temp[17],temp[18],temp[19],temp[20],temp[8]]
        f2_dict[temp[0]] = [temp[2], temp[3], temp[1],temp[17],temp[18],temp[19],temp[20],temp[8]]
        f2_dict[temp[0].replace('.','')] = [temp[2], temp[3], temp[1],temp[17],temp[18],temp[19],temp[20],temp[8]]

i = 0
success_i = 0
fout = open(sys.argv[3],'w')
with open(sys.argv[1]) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        # change here
        seqcol = 4

        seq = temp[seqcol]
        i += 1
        # header
        if seq == 'Sequence':
            continue
        colkey = seq.split('-')[0]
        if colkey in f2_dict:
            addcols = '\t'.join(f2_dict[colkey]) + '\t'
            success_i += 1
        elif colkey.split('.')[0] in f2_dict:
            addcols = '\t'.join(f2_dict[colkey.split('.')[0]]) + '\t'
            success_i += 1
        elif colkey.lstrip('rna-gnl|WGS_SDMP|mrna.') in f2_dict:
            addcols = '\t'.join(f2_dict[colkey.lstrip('rna-gnl|WGS_SDMP|mrna.')]) + '\t'
            success_i += 1
        elif colkey.replace('.','') in f2_dict:
            addcols = '\t'.join(f2_dict[colkey.replace('.','')]) + '\t'
            success_i += 1
        elif len(colkey.split('g')) > 1:
            tifrunner_colkey = 'gnm2.' + colkey.split('g')[1]
            if tifrunner_colkey in f2_dict:
                addcols = '\t'.join(f2_dict[tifrunner_colkey]) + '\t'
                success_i += 1
        else:
            addcols = '.'
        addcols1 = addcols
        colkey = seq.split('-')[1]
        if colkey in f2_dict:
            addcols = '\t'.join(f2_dict[colkey]) + '\t'
            success_i += 1
        elif colkey.split('.')[0] in f2_dict:
            addcols = '\t'.join(f2_dict[colkey.split('.')[0]]) + '\t'
            success_i += 1
        elif colkey.lstrip('rna-gnl|WGS_SDMP|mrna.') in f2_dict:
            addcols = '\t'.join(f2_dict[colkey.lstrip('rna-gnl|WGS_SDMP|mrna.')]) + '\t'
            success_i += 1
        elif colkey.replace('.', '') in f2_dict:
            addcols = '\t'.join(f2_dict[colkey.replace('.', '')]) + '\t'
            success_i += 1
        elif len(colkey.split('g')) > 1:
            tifrunner_colkey = 'gnm2.' + colkey.split('g')[1]
            if tifrunner_colkey in f2_dict:
                addcols = '\t'.join(f2_dict[tifrunner_colkey]) + '\t'
                success_i += 1
        else:
            addcols = '.'
        addcols2 = addcols
        # fix error
        if seq == 'AMD16G02640-Contig1G00050':
            f2_dict['Contig1G00050'][:3] = ['OG0034036', 'distributed', 'NDH814']
            addcols2 = '\t'.join(f2_dict['Contig1G00050']) + '\t'
        if seq == 'Contig397G00010-NDH01G030050':
            f2_dict['Contig397G00010'][:3] = ['OG0039208', 'distributed', 'ZP06']
            addcols1 = '\t'.join(f2_dict['Contig397G00010']) + '\t'


        if addcols1.split('\t')[0] == addcols2.split('\t')[0]:
            fout.write(addcols1 + addcols2 + '\t' + line)
        else:
            print(line.rstrip(), addcols1, addcols2)
            exit()
fout.close()
print('Read line, write line')
print(i)
print(success_i/2)