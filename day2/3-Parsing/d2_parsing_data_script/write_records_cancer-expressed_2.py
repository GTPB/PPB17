'''

Parsing - Exercise 16

The script reads a multiple sequence file in FASTA format and 
only write to a new file the records the Uniprot ACs of which 
are present in the list created in Exercise 14).
This version of the script collects the header and the sequence
separately, in case you wanted to manipulate them.

'''

# We need two input files
cancer_file = open('cancer-expressed.txt')
human_fasta = open('SwissProt-Human.fasta')

Outfile = open('cancer-expressed_records.fasta','w')

# Create the list from cancer-expressed.txt
cancer_list = []
for line in cancer_file:
	AC = line.strip()
	cancer_list.append(AC)

# Read the FASTA input and check if ACs are in cancer_list
seq = ""
for line in human_fasta:
    # Take the first record into account
    if line[0] == '>' and seq == '':
        header = line
        AC = line.split('|')[1]
    elif line[0] != '>':
        seq = seq + line
    elif line[0] == '>' and seq != '':
        if AC in cancer_list:
            Outfile.write(header + seq)
        # Re-initialise variables for the next record
        header = line
        AC = line.split('|')[1]
        seq = ''

# Take the last record into account
if AC in cancer_list:
	Outfile.write(header + seq)

Outfile.close()

