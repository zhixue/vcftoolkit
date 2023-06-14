# python3 svid_join.py SVphe.txt SVexp.txt > new.txt
import sys


pidx = {'DiseaseResistance':0, 'FruitSize':1}

svp_dict = dict()
i = 0
with open(sys.argv[1]) as f:
	for line in f:
		i += 1
		if i == 1:
			continue
		temp = line.rstrip().split('\t')
		svid = temp[1]
		phe = temp[0]
		if phe == 'FruitCoat':
			continue
		p = temp[2]
		olpgene = temp[3]
		olpexon = temp[4]
		olpcds = temp[5]
		olpud3k = temp[6]
		olprepeat = temp[7]
		if svid not in svp_dict:
			p_dr = 0
			p_fs = 0
			svp_dict[svid] = [p_dr,p_fs,olpgene,olpexon,olpcds,olpud3k,olprepeat]
		svp_dict[svid][pidx[phe]] = p

i = 0
with open(sys.argv[2]) as f:
	for line in f:
		i += 1
		if i == 1:
			continue
		temp = line.rstrip().split('\t')
		svid = temp[0]
		if svid in svp_dict:
			print('\t'.join([svid] + svp_dict[svid] + temp[1:]))



