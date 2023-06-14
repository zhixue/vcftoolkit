#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/4/4 5:03 PM
    @Usage: python3 subBUSCO.sh full_table.tsv chrlist
"""

import sys


chrlist = set()
with open(sys.argv[2]) as f:
    for line in f:
        chrlist.add(line.rstrip())

searched_chrlist = set()
frag_ids = dict()
complete_ids = dict()
all_ids = dict()

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'):
            continue
        temp = line.rstrip().split('\t')
        if temp[0] not in all_ids:
            all_ids[temp[0]] = 0
        if temp[1] == 'Missing':
            continue
        if temp[2] in chrlist:
            searched_chrlist.add(temp[2])
            if temp[1] == 'Fragmented':
                if temp[0] not in frag_ids:
                    frag_ids[temp[0]] = 1
            else:
                if temp[0] not in complete_ids:
                    complete_ids[temp[0]] = 1
                else:
                    complete_ids[temp[0]] += 1
print('# Complete, Single, Duplicated:')
print(len(complete_ids)/len(all_ids),
      len([key for key in complete_ids if complete_ids[key]==1])/len(all_ids),
      len([key for key in complete_ids if complete_ids[key]>1])/len(all_ids))


