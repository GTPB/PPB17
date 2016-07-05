'''

Functions - Exercise 4b

The script is an extension of return_headers_loop.py that 
writes each header in a separate output file.

'''

def return_header(filename):
    fasta = open(filename)
    for line in fasta:
        if line[0] == '>':
            return line

filenames = ['SingleSeq1.fasta',
             'SingleSeq2.fasta',
             'SingleSeq3.fasta']
n = 0
for name in filenames: 
    n = n + 1
    output = open("header" + str(n) + ".txt", "w")
    output.write(return_header(name))

output.close()

