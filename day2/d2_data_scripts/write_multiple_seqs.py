'''
Parsing - Exercise 6

The script reads a multiple sequence regord FASTA file and 
writes the sequences to a new file separated by a blank line.

'''

fasta = open('sprot_prot.fasta')
seqs = open('seqs.txt', 'w')

for line in fasta:
	if line[0] == '>':
		seqs.write('\n')
	elif line[0] != '>':
		seqs.write(line.strip() + '\n')

seqs.close()

