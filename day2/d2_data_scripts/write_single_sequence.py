'''

Parsing - Exercise 2

The script reads a file in FASTA format and writes to a new file only the sequence (without the header).

'''


seq_fasta = open("SingleSeq.fasta")
Outfile = open("seq.txt","w") 

seq = ''

for line in seq_fasta:
	if line[0] != '>':
            Outfile.write(line)

Outfile.close()
