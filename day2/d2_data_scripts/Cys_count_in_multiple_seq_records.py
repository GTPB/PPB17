'''

Parsing - Exercise 8

The script reads FASTA records from a file and counts 
the cysteine residues in each sequence.

'''


fasta = open('SwissProt-Human.fasta')

seq = ''

for line in fasta:
        #This is needed to take into account the first record
        if line[0] == '>' and seq == '':
                header = line[4:10]
        elif line[0] != '>':
                seq = seq + line.strip()
        elif line[0] == '>' and seq != '':
                cys_num = seq.count('C')
                print "The number of Cys in ", header, 'is: ', cys_num
                header = line[4:10]
                seq = ''

#This is needed for taking the last record into account
cys_num = seq.count('C')
print "The number of Cys in ", header, 'is: ', cys_num

