#python3 vcf2matrix.py raw.vcf > matrix.txt
import sys
with open(sys.argv[1]) as fin:
	for line in fin:
		if line.startswith('##'):
			continue
		else:
			if line.startswith('#'):
				temp = line.rstrip().split('\t')
				sample_n = len(temp[9:])
				print('ID' + '\t'  + '\t'.join(temp[9:]))
			else:
				temp = line.rstrip().split('\t')
				svid = temp[2]
				gtvector = [0] * sample_n
				for i in range(sample_n):
					if temp[9+i].startswith('0/1'):
						gtvector[i] = 1
				print(svid + '\t' + '\t'.join([str(x) for x in gtvector]))



