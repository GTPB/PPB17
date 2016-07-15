#### Solution to challenge #1
```
import sys

print sys.argv

filename = sys.argv[1]

gbk = open(filename)

for line in gbk:
    if line[0:5] == 'LOCUS':
        print line

```

<a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day4/Pipelines/Running-BLAST_sys.argv.md#challenge-1>back<a/>
<br>
<br>


#### Solution to challenge #2

```
import subprocess

seqs = ['P00519', 'P05480', 'P12931']

for seq in seqs:
      command_line = ['blastp','-query',
                seq + '.fasta','-out',
                seq + '_blout', '-outfmt',
                '6','-db','nr.00']
      subprocess.call(command_line)
```
<a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day4/Pipelines/Running-BLAST_sys.argv.md#challenge-2>back<a/>
<br>
<br>



#### Solution to challenge #3
```
seqs = ['P00519', 'P05480', 'P12931']

out = open('blast_best_scores', 'w')

for seq in seqs:
      first_line = open(seq + '_blout').readline()
      column = first_line.split()
      out.write(column[0] + '\t' + column[2] + '\n')

out.close()
```
<a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day4/Pipelines/Running-BLAST_sys.argv.md#challenge-3>back<a/>
<br>
<br>
