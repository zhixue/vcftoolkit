# python3 vcf_svtype_divide.py raw.vcf prefix


import sys

def string2dict(long_string, sep=';', eq='=', rm_quote=False):
    if rm_quote:
        long_string = long_string.replace('"', '').replace("'", '')
    long_string = long_string.replace('; ', ';')
    out_dict = dict()
    tmp = long_string.rstrip(sep).split(sep)
    for i in tmp:
        if len(i.split(eq)) == 2:
            key, value = i.split(eq)
        else:
            key = i.split(eq)[0]
            value = eq.join(i.split(eq)[1:])
        out_dict[key] = value
    return out_dict

header = ''
svtypes = ['DEL', 'DUP', 'INS', 'INV', 'BND']
svtypes2idx = {'DEL':0 , 'DUP':1, 'INS':2, 'INV':3, 'BND':4}
svtypes_temp_lines = {'DEL':[] , 'DUP':[], 'INS':[], 'INV':[], 'BND':[]}
svtypes_dict = dict() # CHROM, POS, REF, ALT

prefix = sys.argv[2]

with open(sys.argv[1]) as fin:
	for line in fin:
		if line.startswith('#'):
			header += line
		else:
			temp = line.rstrip().split('\t')
			info = string2dict(temp[7])
			svtype = info['SVTYPE'][:3]
			if svtype == 'TRA':
				svtype = 'BND'
			sv_uniq_inf = (temp[0],temp[1],temp[4]) #temp[3],temp[4])
			if sv_uniq_inf in svtypes_dict:
				continue
			svtypes_dict[sv_uniq_inf] = ''
			svtypes_temp_lines[svtype] += [line]

print('# Finish reading!')

for i in range(len(svtypes)):
	svtype_out = svtypes[i]
	with open(prefix + '.' + svtype_out + '.vcf', 'w') as fout:
		fout.write(header + ''.join(svtypes_temp_lines[svtype_out]))

print('# Finish writing!')

