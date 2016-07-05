'''

Pipelines - Exercise 

The script runs BLAST on more than one input sequence.

'''

inputf = ['P05480.fasta', 'P00519.fasta', 'P12931.fasta']

import os

n = 0
for seq in inputf:
    print seq
    n = n + 1
    s = str(n)
    cmd = 'blastp -query '+ seq + ' -out Blast-' + s + '.out -db nr.00 '
    print cmd
    os.system(cmd)
	
