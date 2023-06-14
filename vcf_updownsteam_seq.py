#python3 vcf_updownsteam_seq.py  x.fa x.vcf flank_len > seq.txt
# seq.txt
# CHROM POS ......  Seq
# ................	.aTa.
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


def flank_seq(seq, pos_start, pos_end, flank_len):
	flank_left = seq[max(0,pos_start-flank_len):pos_start-1]
	flank_right = seq[pos_end:pos_end+flank_len]
	return flank_left.lower(), flank_right.lower()



flank_len = int(sys.argv[3])
fafile = sys.argv[1]
vcffile = sys.argv[2]

fa_dict = dict()
chrn = ''
with open(fafile) as fin:
	for line in fin:
		if line.startswith('>'):
			chrn = line.rstrip().split()[0][1:]
			fa_dict[chrn] = ''
		else:
			fa_dict[chrn] += line.rstrip()


with open(vcffile) as fin:
	for line in fin:
		if line.startswith('#'):
			print(line.strip())
		else:
			temp = line.rstrip().split('\t')
			pos_start = int(temp[1])
			info = string2dict(temp[7])
			pos_end = int(info['END'])
			#if info['SVTYPE'] == 'INS':
			#	pos_end += 1
			flank_seqs = flank_seq(fa_dict[temp[0]], pos_start, pos_end, flank_len)
			ref_up_down_seq = flank_seqs[0] + temp[3].upper() + flank_seqs[1]
			alt_up_down_seq = flank_seqs[0] + temp[4].upper() + flank_seqs[1]
			print(line.strip() + '\t' + ref_up_down_seq + '\t' + alt_up_down_seq)


