# python3 leftjoin.py file1 file1_col file2 file2_col > new_file
import sys


f2_dict = dict()
with open(sys.argv[3]) as f:
	for line in f:
		temp = line.rstrip().split('\t')
		f2_dict[temp[int(sys.argv[4])-1]] = line.rstrip()
		f2_dict[temp[int(sys.argv[4]) - 1].split('.')[0]] = line.rstrip()
		f2_dict[temp[int(sys.argv[4]) - 1].replace('.','')] = line.rstrip()

i = 0
with open(sys.argv[1]) as f:
	for line in f:
		temp = line.rstrip().split('\t')
		i += 1

		flag = 0
		for item in temp[int(sys.argv[2])-1].split('-'):
			if item in f2_dict:
				flag = 1
				print(line.rstrip() + '\t' + f2_dict[item])
				break
			elif item.split('.')[0] in f2_dict:
				flag = 1
				print(line.rstrip() + '\t' + f2_dict[item.split('.')[0]])
				break
			elif item.replace('.','') in f2_dict:
				flag = 1
				print(line.rstrip() + '\t' + f2_dict[item.replace('.','')])
				break
		if flag == 0:
			print(line.rstrip() + '\t' + '.')
