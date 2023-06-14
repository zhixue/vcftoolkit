#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/3/6 8:29 PM
    @Usage: python3 gfa_addprefix.py x.gfa prefix_ > new.gfa
"""
import sys
import re

format_explain = '''
GFA 1.0
https://github.com/GFA-spec/GFA-spec/blob/master/GFA1.md

Type	Description
#	Comment
H	Header
S	Segment
L	Link
J	Jump (since v1.2)
C	Containment
P	Path
W	Walk (since v1.1)
'''

with open(sys.argv[1]) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        # segment line
        if line.startswith('S'):
            sname = temp[1]
            temp[1] = sys.argv[2] + sname
            print('\t'.join(temp))
        # link line
        elif line.startswith('L'):
            sfrom = temp[1]
            sto = temp[3]
            temp[1] = sys.argv[2] + sfrom
            temp[3] = sys.argv[2] + sto
            print('\t'.join(temp))
        # containment line
        elif line.startswith('C'):
            scontainer = temp[1]
            scontaned = temp[3]
            temp[1] = sys.argv[2] + scontainer
            temp[3] = sys.argv[2] + scontaned
            print('\t'.join(temp))
        # path line
        elif line.startswith('P'):
            spass = temp[2]
            newspass = []
            for seg_ori in spass.split(','):
                newspass += [sys.argv[2] + seg_ori]
            temp[2] = ','.join(newspass)
            print('\t'.join(temp))
        # walk line
        elif line.startswith('W'):
            swalk = temp[6]
            newswalk = ''
            segs = re.split('[><]', swalk)[1:]
            dires = re.findall('[><]+', swalk)

            newsegs = []
            for seg in segs:
                newsegs += [sys.argv[2] + seg]
            for i in range(len(dires)):
                newswalk += dires[i] + newsegs[i]
            temp[6] = newswalk
            print('\t'.join(temp))

