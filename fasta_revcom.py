#!/usr/bin/env python3 fasta revcom.py in.fa > out.fa
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/10/29 10:49 AM
    @Usage:
"""
import sys

def revcom(st):
    pairs = {
        "A": "T",
        "C": "G",
        "G": "C",
        "T": "A",
        "a": "t",
        "c": "g",
        "g": "c",
        "t": "a",
        "N": "N"
    }

    reverse_complement = ""
    for index in range(len(st) - 1, 0, -1):
        base = st[index]
        complement = pairs[base]
        reverse_complement += complement
    return reverse_complement


with open(sys.argv[1]) as f:
    seq = ''
    for line in f:
        if line.startswith('>'):
            if seq != '':
                print(revcom(seq))
            print(line.rstrip())
            seq = ''
        else:
            seq += line.rstrip()
    # last one
    print(revcom(seq))

