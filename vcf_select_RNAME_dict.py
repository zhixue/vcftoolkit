#python3 select_vcf.py in.vcf Chr.list out.vcf
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


chrlist = sys.argv[2]
chr_dict = dict() # 'q':'r'
with open(chrlist) as f:
    for line in f:
        temp = line.rstrip().split('\t')
        chr_dict[temp[0].split(' ')[0]] = temp[1]

outvcf = sys.argv[3]


load_record = 0
write_record = 0

fout = open(outvcf,'w')

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'):
            fout.write(line)
        else:
            load_record += 1
            temp = line.rstrip().split('\t')
            chrn = temp[0]
            info = string2dict(temp[7])
            if 'RNAMES' in info:
                skip = 0
                rnames = info['RNAMES'].split(',')
                for rname in rnames:
                    if rname in chr_dict:
                        if chr_dict[rname] != chrn:
                            skip = 1
                            break
                if skip == 0:
                    fout.write(line)
                    write_record += 1

print("# Load {n1} records, write {n2} records.".format(n1=load_record,n2=write_record))
fout.close()
