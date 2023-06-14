#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/11/30 2:50 PM
    @Usage: python3 pairwise_drop_same.py Homolog_pairwise.txt Homolog_group.idt100.fa.fg.txt > Homolog_pairwise.filtered.txt
"""
import sys

samegene_dict = dict()
with open(sys.argv[2]) as f:
    for line in f:
        genes = line.rstrip().split()[1:]
        if len(genes) > 1:
            for i in range(len(genes)):
                for j in range(len(genes)):
                    if i != j:
                        if genes[i] not in samegene_dict:
                            samegene_dict[genes[i]] = [genes[j]]
                        else:
                            samegene_dict[genes[i]] += [genes[j]]

with open(sys.argv[1]) as f:
    for line in f:
        temp = line.rstrip().split(' ')
        if temp[0] in samegene_dict:
            if temp[1] in samegene_dict[temp[0]]:
                continue
        print(line.rstrip())


