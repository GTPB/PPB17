'''

Parsing - Exercise 16

The script reads a multiple sequence file in FASTA format and 
only write to a new file the records the Uniprot ACs of which 
are present in the list created in Exercise 14).

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
for line in human_fasta: 
    if line[0] == ">":
        AC = line.split("|")[1] 
        # Write the header to the output
        if AC in cancer_list:
            Outfile.write(line)
    else:
        # Write the sequence to the output
        if AC in cancer_list:
            Outfile.write(line)

Outfile.close()

