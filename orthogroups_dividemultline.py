#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/11/25 11:29 AM
    @Usage:
"""
import sys

def pav_gene_type(presence_n,all_n,cutoff=0.75):
    if presence_n == all_n:
        return 'core'
    if presence_n >= all_n * cutoff:
        return 'softcore'
    if presence_n > 1:
        return 'distributed'
    else:
        return 'private'


with open(sys.argv[1]) as f:
    i = 0
    sample_len = 0
    for line in f:
        i += 1
        if i == 1:
            temp = [x.split('.')[0] for x in line.rstrip().split('\t')]
            samples = temp[1:]
            sample_len = len(samples)
        else:
            temp = [x.replace(' ','').split(',') for x in line.rstrip('\n').split('\t')]
            ortho = temp[0][0]
            #print(temp[1:])

            present_number = sum([1 for x in temp[1:] if x != ['']])
            family_size = sum([len(x) for x in temp[1:] if x != ['']])
            pav_type = pav_gene_type(present_number, sample_len)
            for i in range(1, sample_len+1):
                sample = samples[i-1]
                if temp[i] != ['']:
                    family_size_in_this_sample = len(temp[i])
                    for pep in temp[i]:
                        print('\t'.join([str(x) for x in [pep, sample, ortho, pav_type, present_number, family_size, family_size_in_this_sample]]))

