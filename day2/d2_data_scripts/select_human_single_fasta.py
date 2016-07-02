'''

Parsing - Exercise 4

The script reads a sequence record file in FASTA format
and prints the record only if the sequence is from Homo sapiens.

'''


seq_fasta = open("SingleSeq.fasta")

seq = ''
header = '' 

for line in seq_fasta:
    if line[0] == '>':
        if "Homo sapiens" in line:
            header = line
    else:
	if header:
            seq = seq + line

if header:
    print header + seq
else:
    print "The record is not from H. sapiens"
	

	
