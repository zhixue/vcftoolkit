# python3 vcf_GTreplace_missing.py raw.vcf > new.vcf
import sys


with open(sys.argv[1]) as fin:
	for line in fin:
		if line.startswith('#'):
			print(line.rstrip())
		else:
			temp = line.rstrip().split('\t')
			for i in range(9,len(temp)):
				if temp[i].startswith('./.:NaN'):
					temp[i] = '0/0' + temp[i][3:]
				elif temp[i].find('cuteSV'):
					temp[i] = '0/1' + temp[i][3:]

			print('\t'.join(temp))
