#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Hongzhang Xue
    @Modified: 2023/5/11 8:36 PM
    @Usage: python3 gaf_map_stat.py idt_90 file query_num query_base
"""
import sys

description = '''
https://github.com/lh3/gfatools/blob/master/doc/rGFA.md#the-graph-alignment-format-gaf
Col	Type	Description
1	string	Query sequence name
2	int	Query sequence length
3	int	Query start (0-based; closed)
4	int	Query end (0-based; open)
5	char	Strand relative to the path: "+" or "-"
6	string	Path matching /([><][^\s><]+(:\d+-\d+)?)+|([^\s><]+)/
7	int	Path length
8	int	Start position on the path (0-based)
9	int	End position on the path (0-based)
10	int	Number of residue matches
11	int	Alignment block length
12	int	Mapping quality (0-255; 255 for missing)
'''

def union_length(regions):
    regions = sorted(regions)
    count_length = 0
    for i in range(1, len(regions)):
        if regions[i-1][1] > regions[i][1]:
            regions[i] = (regions[i][0], regions[i-1][1])
        count_length += \
            (regions[i-1][1] - regions[i-1][0] + 1) - \
            max(0, regions[i-1][1] - regions[i][0] + 1)
    # final one
    count_length += regions[-1][1] - regions[-1][0] + 1
    return count_length


idt_c = int(sys.argv[1])
gaf = sys.argv[2]

query_length = dict()
query_map_region = dict()

with open(gaf) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        # like paf
        if float(temp[9]) / float(temp[10]) * 100 < idt_c:
            continue
        if temp[0] not in query_length:
            query_length[temp[0]] = int(temp[1])
            # query end open -> query end closed
        if temp[0] not in query_map_region:
            query_map_region[temp[0]] = [(int(temp[2]), int(temp[3]) - 1)]
        else:
            if [(int(temp[2]), int(temp[3]) - 1)] not in query_map_region[temp[0]]:
                query_map_region[temp[0]] += [(int(temp[2]), int(temp[3]) - 1)]

query_num = int(sys.argv[3])
query_base = int(sys.argv[4])

query_map_length = dict()
for key in query_map_region:
    query_map_length[key] = union_length(query_map_region[key])

print("# Query number: " + str(sys.argv[3]))
print("# Query base: " + str(sys.argv[4]))
print("# Query mapping rate over identity " + str(sys.argv[1]) + "%: " + str(len(query_length)/query_num))
print("# Query mapping base rate over identity " + str(sys.argv[1]) + "%: " + str(sum([query_map_length[x] for x in query_map_length])/query_base))

for key in query_length:
    # query, query length, query map length, query map coverage ,query map region
    print('\t'.join([str(x) for x in [key, query_length[key], query_map_length[key], query_map_length[key]/query_length[key], query_map_region[key]]]))

