'''
Parsing - Exercise 5

The script reads a multiple sequence record FASTA file and 
writes the record headers to a new file.

'''

fasta = open('sprot_prot.fasta')
headers = open('headers.txt', 'w')

for line in fasta:
    if line[0] == '>':
        headers.write(line)

headers.close()

