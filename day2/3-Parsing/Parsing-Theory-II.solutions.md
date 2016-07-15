
#### Solution to challenge #1

```
cancer_file = open('cancer-expressed.txt')

cancer_list = []

for line in cancer_file:
  AC = line.strip()
  cancer_list.append(AC)
print cancer_list
```
<a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day2/3-Parsing/Parsing-Theory-II.md#challenge-1">back<a/>


#### Solution to challenge #2

```
InputFile = open("SwissProtHuman.fasta","r")
AC_list = []
for line in InputFile:
  if line[0] == '>':
    fields = line.split('|')
    AC_list.append(fields[1])
print AC_list
```
<a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day2/3-Parsing/Parsing-Theory-II.md#challenge-2">back<a/>


#### Solution to challenge #3

```
cancer_file = open('cancer-expressed.txt')
human_fasta = open('SwissProt-Human.fasta')
Outfile = open('cancer-expressed.fasta','w')

cancer_list = []

for line in cancer_file:
  AC = line.strip()
  cancer_list.append(AC)

for line in human_fasta:
  if line[0] == '>':
    AC = line.split('|')[1]
    if AC in cancer_list:
      Outfile.write(line)

Outfile.close()
```


*We are not writing the whole record but the header line only*

<a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day2/3-Parsing/Parsing-Theory-II.md#challenge-3">back<a/>


#### Solution to challenge #4
One possible solution
```
cancer_file = open('cancer-expressed.txt')
human_fasta = open('SwissProt-Human.fasta')
Outfile = open('cancer_expressed.fasta','w')

cancer_list = []
seq = ''

for line in cancer_file:
  AC = line.strip()
  cancer_list.append(AC)

for line in human_fasta:
  if line[0] == '>':
    if seq:
      if AC in cancer_list:
        Outfile.write(header + seq)
      header = line
      AC = line.split('|')[1]
      seq = ''
  else:
    seq = seq + line

if AC in cancer_list:
  Outfile.write(header+seq)
```

another possible solution:
```
cancer_file = open('cancer-expressed.txt')
human_fasta = open('SwissProt-Human.fasta')
Outfile = open('cancer_expressed.fasta','w')

cancer_list = []

for line in cancer_file:
  AC = line.strip()
  cancer_list.append(AC)

for line in human_fasta:
  if line[0] == ">":
    field = line.split("|")
    AC = field[1]
    if AC in cancer_list:
      Outfile.write(line)
  else:
    if AC in cancer_list:
      Outfile.write(line)
Outfile.close()
```


<a href="https://github.com/Pfern/BPBR16-Bioinformatics-using-Python-for-Biomedical-Researchers/blob/master/day2/3-Parsing/Parsing-Theory-II.md#challenge-4">back<a/>
