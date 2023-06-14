#python3 select_vcf.py in.vcf svtypes svminlen svmaxlen > out.vcf
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


svtypes = sys.argv[2].split(',')
svmaxlen = int(sys.argv[4])
svminlen = int(sys.argv[3])


with open(sys.argv[1]) as f:
	for line in f:
		if line.startswith('#'):
			print(line.rstrip())
		else:
			temp = line.rstrip().split('\t')
			info = string2dict(temp[7])
			if info['SVTYPE'] in svtypes:
				if abs(int(info['SVLEN'])) < svmaxlen and abs(int(info['SVLEN'])) > svminlen:
					print(line.rstrip())


