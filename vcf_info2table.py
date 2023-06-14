#python3 vcf_info2table.py in.vcf sv.list > out.tsv
import sys 
# info select
# olp_gene, olp_exon, olp_CDS, olp_repeat

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



with open(sys.argv[2]) as f:
    svlist = [x.rstrip() for x in f.readlines()]


sv_info_dict = dict()
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'):
            continue
        else:
            temp = line.rstrip().split('\t')
            svid = temp[2]
            info = string2dict(temp[7])
            if 'olp_gene' in info:
                olp_gene = info['olp_gene']
            else:
                olp_gene = 'NA'

            if 'olp_exon' in info:
                olp_exon = info['olp_exon']
            else:
                olp_exon = 'NA'

            if 'olp_CDS' in info:
                olp_CDS = info['olp_CDS']
            else:
                olp_CDS = 'NA'

            if 'olp_ud3k' in info:
                olp_ud3k = info['olp_ud3k']
            else:
                olp_ud3k = 'NA'

            if 'olp_repeat' in info:
                olp_repeat = info['olp_repeat']
            else:
                olp_repeat = 'NA'




            sv_info_dict[svid] = [olp_gene,olp_exon,olp_CDS,olp_ud3k,olp_repeat]

for sid in svlist:
    print('\t'.join([sid] + sv_info_dict[sid]))






