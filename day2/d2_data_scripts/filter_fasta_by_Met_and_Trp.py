'''

Parsing - Exercise 11

The script reads a multiple sequence record file in FASTA format and 
writes to a new file only the records the sequences of which start 
with a methionine ('M') AND contain at least two tryptophans ('W').

'''

fasta = open('SwissProtHuman.fasta','r')
outfile = open('SwissProtHuman-Filtered.fasta','w')

seq = ''

for line in fasta:
    # This is to take the first record into account
    if line[0:1] == '>' and seq == '': 
            header = line
    elif line [0:1] != '>':
            seq = seq + line
    elif line[0:1] == '>' and seq != '': 
	    TRP_num = seq.count('W')
	    if seq[0] == 'M' and TRP_num > 1:
                    outfile.write(header + seq)
       	    seq = ''
            header = line

# This is to take the last record into account
TRP_num = seq.count('W')
if seq[0] == 'M' and TRP_num > 1:
    outfile.write(header + seq)
outfile.close()

