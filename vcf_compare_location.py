# python3 vcf_compare_location.py b.vcf colname_in_b c.vcf colname_in_c 1

import sys
max_dist = 1000


def read_vcf(loc, colname_include, ignore_chr=False):
	loc_dict = dict()
	used_col = 0
	with open(loc) as f:
		for line in f:
			if line.startswith('#'):
				if line.startswith('#CHROM'):
					temp = line.rstrip().split('\t')
					for col in range(9, len(temp)):
						if colname_include in temp[col]:
							used_col = col
							print('#' + loc + ' ' + colname_include + ' ' + str(used_col))
				continue
			else:
				temp = line.rstrip().split('\t')
				if temp[used_col] in ('.', '0'):
					continue
				if temp[used_col].startswith('./.:NAN:0,0,0'):
					continue
				if ignore_chr:
					chrn = '_'
				else:
					chrn = temp[0]
				pos = int(temp[1])
				if chrn not in loc_dict:
					loc_dict[chrn] = []
				if pos not in loc_dict[chrn]:
					loc_dict[chrn] += [pos]
	for key in loc_dict:
		loc_dict[key] = sorted(loc_dict[key])
	return loc_dict

def count_n(dict_set):
	count = 0
	for key in dict_set:
		count += len(dict_set[key])
	return count

def count_redundant_n(dict_set):
	count = 0
	for key in dict_set:
		last_pos = -1000000
		for j in dict_set[key]:
			if j - last_pos <= max_dist:
				count += 1
			last_pos = j
	return count

def compare_loc_dict(locb,locc):
	tp = 0
	tp_pos = dict()
	for keyb in locb:
		if keyb in locc:
			for posb in locb[keyb]:
				for posc in locc[keyb]:
					if abs(posb - posc) <= max_dist:
						if posb not in tp_pos and posc not in tp_pos:
							tp += 1
							tp_pos[posb] = ''
							tp_pos[posc] = ''
						break
					if posc - posb > max_dist:
						break
	locb_n = count_n(locb) - count_redundant_n(locb)
	locc_n = count_n(locc) - count_redundant_n(locc)
	fp = locc_n - tp
	fn = locb_n - tp
	precision = 0
	recall = 0
	f1 = 0
	if tp + fp != 0:
		precision = tp / (tp + fp)
	if tp + fn != 0:
		recall = tp / (tp + fn)
	if recall + precision != 0:
		f1 = 2 * ((recall * precision) / (recall + precision))
	#print(locb, locc)
	print('# locb_n, locc_n, tp, fp, fn, precision, recall, f1')
	print(locb_n, locc_n, tp, fp, fn, precision, recall, f1)


ignore_chr = sys.argv[5]
colname_in_b = sys.argv[2]
vcfb = read_vcf(sys.argv[1], colname_in_b, ignore_chr)
colname_in_c = sys.argv[4]
vcfc = read_vcf(sys.argv[3], colname_in_c, ignore_chr)

compare_loc_dict(vcfb,vcfc)


