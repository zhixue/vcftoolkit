#python3 fasta_rename2.py raw.fa raw.Chr.list new.fa
import sys


chr_dict = dict()
with open(sys.argv[2]) as f:
	for line in f:
		temp = line.rstrip().split('\t')
		ctgid = temp[0].split(' ')[0]
		if len(temp) == 1: 
			chr_dict[ctgid] = ctgid
		else:
			chr_dict[ctgid] = temp[1]


write_flag = 0
with open(sys.argv[3],'w') as fout:
	with open(sys.argv[1]) as fin:
		for line in fin:
			if line.startswith('>'):
				ctg = line.rstrip()[1:].split(' ')[0]
				if ctg in chr_dict:
					write_flag = 1
					fout.write('>' + chr_dict[ctg] + '\n')
				else:
					write_flag = 0
			else:
				if write_flag:
					fout.write(line)


