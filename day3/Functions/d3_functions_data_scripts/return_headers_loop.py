'''

Functions - Exercise 3

The sctipt defines a function that :
- Takes as input a file name (of a FASTA file). 
- Opens the file. 
- Returns the header of the sequence record. 
The function call is then inserted in a for loop running 
on a list of 3 sequence file names.

'''

def return_header(filename):
    fasta = open(filename)
    for line in fasta:
        if line[0] == '>':
            return line

filenames = ['SingleSeq.fasta','SingleSeq.fasta','SingleSeq.fasta']
for name in filenames: 
    # Putting a comma at the end of the line, removes the 
    # newline character.
    print return_header(name),
