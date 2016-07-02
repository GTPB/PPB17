'''
Parsing - Exercise 10

The script reads a multiple sequence record file in FASTA format and 
writes to a new file only the records of the sequences having at least
two tryptophan residues ('W').

'''

outfile = open('SwissProtHuman-FilteredTrp.fasta','w')
fasta = open('SwissProtHuman.fasta','r')

seq = ''

for line in fasta:
    # This is to take the first record into account
    if line[0:1] == '>' and seq == '': 
        header = line
    elif line [0:1] != '>':
        seq = seq + line
    elif line[0:1] == '>' and seq != '': 
        TRP_num = seq.count('W')
        if TRP_num > 1:
            outfile.write(header + seq)
        seq = ''
        header = line

# This is to take the last record into account
TRP_num = seq.count('W')
if TRP_num > 1:
    outfile.write(header + seq)
outfile.close()

