'''

Functions - Exercise 4a

The script is an extension of return_headers_loop.py that 
writes all the headers to a single output file.

'''

def return_header(filename):
    fasta = open(filename)
    for line in fasta:
        if line[0] == '>':
            return line

filenames = ['SingleSeq.fasta',
             'SingleSeq.fasta',
             'SingleSeq.fasta']

output = open("headers.txt", "w")

for name in filenames: 
    output.write(return_header(name) + '\n')

output.close()
