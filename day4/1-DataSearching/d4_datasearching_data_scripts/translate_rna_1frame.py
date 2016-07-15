'''

Searching - Exercise 1

Using the codonAMINO dictonary from tgac.py, the program
reads and translates the sequence in the input file rna_seq.fasta
(limited to the first reading frame).

'''


F = open('rna_seq.fasta')
Out = open('protein_seq.fasta','w')

from tgac import codonAMINO

seq = ''
for line in F:
   # This collects the header 
   if line[0] == '>':
      header = line.split()
      geneID = header[0]
      Out.write(geneID + '_protein\n')
   # This collects the sequence
   else:
      seq = seq + line.strip()

prot = ''

# range(i, j, k) generates a list of numbers
# ranging from i to j-1 in steps of k
# We want to range from the first to the last
# position of the sequence.
for i in range(0,len(seq),3):
   if codonAMINO.has_key(seq[i:i+3]):
      prot = prot + codonAMINO[seq[i:i+3]]
   # If codonAMINO does not have the key, we
   # add a '*'
   else:  
      prot = prot + '*'

Out.write(prot + '\n')
