'''

Parsing - Exercise 1

The script reads a file in FASTA format of a single sequence
record and writes to a new file the header of the record.

'''

fasta = open('SingleSeq.fasta')
header = open('header.txt', 'w')

for line in fasta:
    if line[0] == '>':
        header.write(line)

header.close()

