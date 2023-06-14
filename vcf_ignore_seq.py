# python3 vcf_ignore_seq.py raw.vcf > new.vcf
import sys



with open(sys.argv[1]) as fin:
	for line in fin:
		if line.startswith('#'):
			print(line.rstrip())
		else:
			temp = line.rstrip().split('\t')
			if len(temp[3]) > 3:
				temp[3] = '.'
			if len(temp[4]) > 3:
				temp[4] = '.'
			for i in range(9,len(temp)):
				this_s = temp[i]
				spt_this = this_s.split(':')
				for j in range(len(spt_this)):
					if len(spt_this[j]) > 20:
						spt_this[j] = '.'
				temp[i] = ':'.join(spt_this)
			print('\t'.join(temp))
