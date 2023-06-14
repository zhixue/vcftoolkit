#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2022/12/2 12:08 PM
    @Usage:
"""
from itertools import combinations

Fg = {'A':range(1,11),
      'B':range(11,21),
      'C':range(21,71),
      'D':range(71,81),
      'E':range(81,96),
      'F':range(96,101)}


for n in range(5,0,-1):
    #print(n)
    for items in combinations(Fg.keys(), n):
        use_index = []
        print(items)
        for item in items:
            use_index += list(Fg[item])
        #print(use_index)
        # get data from dataframe using index
        # ...
        # get auc
        # print(auc)

