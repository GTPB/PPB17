'''
Parsing - Exercise 13

The script reads a file in FASTA format and copies 
the record ACs to a new file .

'''

InputFile = open("SwissProtHuman.fasta")
Outfile = open("SwissProtHuman_ACs.txt", "w")

for line in InputFile:
    if line[0] == '>':
        # AC is a list. Here we take its second element: 
        AC = line.split('|')[1]
        # Insert a newline character
        Outfile.write(AC + '\n') 

Outfile.close()

