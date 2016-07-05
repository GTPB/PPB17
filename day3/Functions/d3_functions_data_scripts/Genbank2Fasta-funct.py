'''

Functions - Exercise 5

The script defines a function that takes as argument 
a Genbank record and returns the nucleotide sequence 
in FASTA format.

'''

def genbank2fasta(filename): 
    name = filename.split('.')[0] 
    InputFile = open(filename)
    OutputFile = open(name + ".fasta","w")
    flag = 0
    for line in InputFile:
        if line[0:9] == 'ACCESSION':
            AC = line.split()[1].strip()
            OutputFile.write('>'+AC+'\n')
        if line[0:6] == 'ORIGIN': 
            flag = 1
            continue
        if flag == 1:
            fields = line.split()
            if fields != []:
                seq = ''.join(fields[1:])
                OutputFile.write(seq +'\n')
    OutputFile.close()

filename = "ap006852.gbk"
genbank2fasta(filename) 





