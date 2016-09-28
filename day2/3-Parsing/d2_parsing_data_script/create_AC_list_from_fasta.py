'''
Parsing - Exercise 12

The script creates a list containing Uniprot ACs extracted from a FASTA file
and prints the list.

'''

InputFile = open("SwissProt-Human.fasta","r")


AC_list = []

for line in InputFile:
    if line[0] == '>':
        #AC is a list. Here we take its second element: 
        AC = line.split('|')[1]
        AC_list.append(AC)

print AC_list

