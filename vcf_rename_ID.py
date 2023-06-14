#python3 rename_ID.py raw.vcf > new.vcf

import sys


with open(sys.argv[1]) as fin:
	for line in fin:
		if line.startswith('#'):
			print(line.rstrip())
		else:
			temp = line.rstrip().split('\t')
			tp = temp[2].split('.')[1]
			temp[2] = tp + '.' + temp[0] + '.' + temp[1] 
			print('\t'.join(temp))
			
