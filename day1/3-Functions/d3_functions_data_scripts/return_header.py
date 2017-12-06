'''

Functions - Exercise 2

The sctipt defines a function that :
- Takes as input a file name (of a FASTA file). 
- Opens the file. 
- Returns the header of the sequence record. 
Finally, it prints the header.


'''

def return_header(filename):
    fasta = open(filename)
    for line in fasta:
        if line[0] == '>':
            return line
# Putting a comma at the end of the line, removes the 
# newline character.
print return_header('SingleSeq.fasta'),
