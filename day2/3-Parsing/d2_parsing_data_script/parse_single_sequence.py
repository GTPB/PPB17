'''

Parsing - Exercise 3

The script reads a file in FASTA format and writes the header 
to a file and the sequence to a different one.

'''

fasta = open('SingleSeq.fasta')
header = open('header.txt', 'w')
seq = open('seq.txt', "w")

for line in fasta:
    if line[0] == '>':
        header.write(line)
    else:
        seq.write(line)

header.close()
seq.close()

