# python3 vcf_uniq.py raw.vcf > new.vcf
import sys

svtypes_dict = dict() # CHROM, POS, REF, ALT

with open(sys.argv[1]) as fin:
	for line in fin:
		if line.startswith('#'):
			print(line.rstrip())
		else:
			temp = line.rstrip().split('\t')
			sv_uniq_inf = (temp[0],temp[1]) #temp[3],temp[4])
			if sv_uniq_inf in svtypes_dict:
				continue
			svtypes_dict[sv_uniq_inf] = ''
			print(line.rstrip())




