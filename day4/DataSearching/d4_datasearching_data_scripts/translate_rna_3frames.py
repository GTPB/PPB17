'''

Searching - Exercise 2

Using the codonAMINO dictonary from tgac.py, the program
reads and translates the sequence in the input file rna_seq.fasta
(does it for all the three reading frames).

'''



F = open('rna_seq.fasta')
Out = open('protein_seq.fasta','w')

seq = ''
for line in F:
   if line[0] == '>':
      header = line.split()
      geneID = header[0]
      Out.write(geneID + '_protein\n')
   else:
      seq = seq + line.strip()

from tgac import codonAMINO

prot = ''
# Repeat 3 times (one per frame)
for j in range(3):
   # Insert a separator between frames
   Out.write(str(j) + "-frame\n")
   # Start from the first, second, third position
   for i in range(j,len(seq),3):
      if codonAMINO.has_key(seq[i:i+3]):
         prot = prot + codonAMINO[seq[i:i+3]]
      else:  
         prot = prot + '*'
   Out.write(prot + '\n')
   prot = ''
