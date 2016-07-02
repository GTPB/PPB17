'''

Parsing - Exercise 15

The script reads a multiple sequence FASTA file one record after the other, 
checks if the record header contains one of the ACs present in the list created in exercise 14). If YES, copies the record headers to a new file.

'''
# We need two input files
cancer_file = open('cancer-expressed.txt')
human_fasta = open('SwissProt-Human.fasta')

Outfile = open('cancer-expressed_headers.fasta','w')

# Create the list from cancer-expressed.txt
cancer_list = []
for line in cancer_file:
    AC = line.strip()
    cancer_list.append(AC)

# Read the FASTA input and check if ACs are in cancer_list
for line in human_fasta:
    if line[0] == '>':
        AC = line.split('|')[1]
        if AC in cancer_list:
            Outfile.write(line)

Outfile.close()

