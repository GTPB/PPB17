'''

Parsing - Exercise 17

The script reads a genbank record and writes to a file 
the nucleotide sequence in FASTA format.

'''

InputFile = open("ap006852.gbk")
OutputFile = open("ap006852.fasta","w")

# Initialise a flag
flag = 0

for line in InputFile:
    # Get the AC and write it in the output header
    # Here you could also use the input line starting
    # by LOCUS
    if line[0:9] == 'ACCESSION':
        AC = line.split()[1].strip()
        OutputFile.write('>'+AC+'\n')
    # When ORIGIN is encountered, set flag = 1
    if line[0:6] == 'ORIGIN': 
        flag = 1
        # This jumps to next line in the loop
        # Otherwise next if is checked for the
        # ORIGIN line too
        continue
    # flag is 1 for all lines after ORIGIN
    if flag == 1:
        fields = line.split()
        if fields != []:
            seq = ''.join(fields[1:])
            OutputFile.write(seq +'\n')

OutputFile.close()

