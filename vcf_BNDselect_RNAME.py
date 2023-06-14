#python3 select_vcf.py in.vcf RefChrPrefix QueryChrPrefix offset out.vcf
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


RefChrPrefix = sys.argv[2]
QueryChrPrefix = sys.argv[3]
offset = int(sys.argv[4]) # default=0 AA: 0 BB: -10 
outvcf = sys.argv[5]


load_record = 0
write_record = 0

fout = open(outvcf,'w')

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'):
            fout.write(line)
        else:
            temp = line.rstrip().split('\t')
            chrn_n = int(temp[0].lstrip(RefChrPrefix))
            info = string2dict(temp[7])
            if not info['SVTYPE'] in ['BND','TRA','BND/TRA','TRA/BND']:
                continue
            load_record += 1
            chrn_n_bnd = int(temp[4].split(RefChrPrefix)[1].split(':')[0])
            if 'RNAMES' in info:
                skip = 0
                rnames = info['RNAMES'].split(',')
                for rname in rnames:
                    if rname.startswith(QueryChrPrefix):
                        if int(rname.replace(QueryChrPrefix,'')) != chrn_n + offset:
                            if int(rname.replace(QueryChrPrefix,'')) != chrn_n_bnd + offset:
                                skip = 1
                                break
                if skip == 0:
                    fout.write(line)
                    write_record += 1

print("# Load {n1} records, write {n2} records.".format(n1=load_record,n2=write_record))
fout.close()

