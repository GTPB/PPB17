
#### Solution to challenge #1

```
F = open('rna_seq.fasta')
Out = open('protein_seq.fasta','w')

seq=''
for line in F:
    if line[0] == '>':
        header = line.split()
        geneID = header[0]
        Out.write(geneID + '_protein\n')
    else:
        seq = seq + line.strip()

from tgac import codonAMINO
prot = ''
for i in range(0,len(seq),3):
    triplet =seq[i:i+3]
    if codonAMINO.has_key(triplet): # is the triplet in the dictionary? equivalent to: if triplet in codonAMINO
        prot = prot + codonAMINO[triplet]
    else:
        prot = prot + '?'

Out.write(prot + '\n')
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day4/DataSearching/DataSearching.md#challenge-1">back<a/>
<br>
<br>



#### Solution to challenge #2
```
from tgac import codonAMINO

prot = ''
for j in range(3):
    Out.write(str(j) + "-frame\n")
    for i in range(j,len(seq),3):
        if codonAMINO.has_key(seq[i:i+3]):
            prot = prot + codonAMINO[seq[i:i+3]]
        else:
            prot = prot + '*'

    Out.write(prot + '\n')
prot = ''
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day4/DataSearching/DataSearching.md#challenge-2">back<a/>
<br>
<br>
