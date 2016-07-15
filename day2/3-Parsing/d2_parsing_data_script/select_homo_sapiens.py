'''
Parsing - Exercise 7

The script reads a multiple sequence record FASTA file and 
write to a new file only the records from Homo sapiens.

'''

fasta = open('sprot_prot.fasta')
output = open('homo_sapiens.fasta', 'w')

seq = ''

for line in fasta:
    if line[0] == '>' and seq == '':
        header = line
    elif line[0] != '>':
        seq = seq + line
    elif line[0] == '>' and seq != '':
        if "Homo sapiens" in header:
            output.write(header + seq)
        header = line
        seq = ''

if "Homo sapiens" in header:
    output.write(header + seq)

output.close() 
