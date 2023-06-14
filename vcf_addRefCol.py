# python3 vcf_addRefCol.py raw.vcf Sample > new.vcf
import sys
FORMAT='0/0:NaN:0:0,0:--:NaN:NaN:NaN:NAN:NAN:NAN'

with open(sys.argv[1]) as fin:
	for line in fin:
		if line.startswith('##'):
			print(line.rstrip())
		else:
			if line.startswith('#CHROM'):
				print(line.rstrip() + '\t' + sys.argv[2])
			else:
				print(line.rstrip() + '\t' + FORMAT)

