



# Parsing data records I

Two sequence records in FASTA format:


```
>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARR
WRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFY
LKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVF
YEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGD
AGEGEN

>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARR
WRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFY
LKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVF
YEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGD
AGEGEN
```

### Program 1


Open the file `SingleSeq.fasta`, read its content line by line
and print it

#### Program 1 - solution

```
seq = open("SingleSeq.fasta")

for line in seq:
print line
```

### Program 2


Open the file `SingleSeq.fasta`, read its content line by line
and write it to another file.

#### Program 2 - solution

```
seq = open("SingleSeq.fasta")
seq_2 = open("SingleSeq-2.fasta","w")

for line in seq:
seq_2.write(line)

seq_2.close()
```
### Writing different things depending on a condition

Read a sequence in FASTA format and print only the
header of the sequence

```
>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGAR
WRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFY
LKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVF
YEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGD
AGEGEN
```

Making choices: The `if/elif/else` statements

```
if condition1 #if expression in condition1is TRUE
    statements1   #execute statements1
elif condition2 #else if expression in condition2is TRUE
    statements2 #execute statements2...
elif condition3 #etc...
...
…

else:
  statementsN
```

Check these conditions:
` 'ACTC'[0] == 'C' `  is  True or false?
` 'ACTC'[0] == 'A' `  is  True or false?

```
==    !=     =>    <=    >      <
```

The `if/elif/else` construct produces different effects compared with the use of a series of `if` conditions

```
nucl = ['A','C','T','G']
if 'A' in nucl: print 'A'
elif 'C' in nucl: print 'C'
elif 'T' in nucl: print 'T'
else: print 'G'
```

```
nucl = ['A','C','T','G']
if 'A' in
if 'C' in
nucl: print 'A'
nucl: print 'C'
if 'T' in nucl: print 'T'
if 'G' in nucl: print 'G'
```

### Program 3

Read a sequence in FASTA format and print only the
header of the sequence

```
>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGAR
WRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFY
LKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVF
YEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGD
AGEGEN
```
#### Program 3 - solution

```
seq = open("SingleSeq.fasta")

for line in seq:
if line[0] == '>':
print line

>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARR
WRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFY
LKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVF
YEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGD
AGEGEN
```

```
seq = open("SingleSeq.fasta")

for line in seq:
if line[0] == '>':
print line
```

```
seq = open("SingleSeq.fasta")

for line in seq:
if line[0] != '>':
print line
```


```
seq = open("SingleSeq.fasta")

for line in seq:
if line[0] != '>':
print line
```

### Program 4


Read a file in FASTA format and write to a new file
only the header of the record.

#### Program 4 - solution

```
fasta = open('SingleSeq.fasta')
header = open('header.txt', 'w’)

for line in fasta:
if line[0] == '>':
header.write(line)

header.close()
```

### Program 5


Read a file in FASTA format and write to a new file
only the sequence (without the header).

#### Program 5 - solution

```
fasta = open('SingleSeq.fasta')
seq = open('seq.txt','w')

for line in fasta:
if line[0] != '>':
seq.write(line)

seq.close()
```

### Merge programs 4 and 5


In other words, read a file in FASTA format and write
the header to a file and the sequence to a different
one.

#### Programs 4 & 5 merged

```
fasta = open('SingleSeq.fasta')
header = open('header.txt', 'w')
seq = open('seq.txt','w')

for line in fasta:
if line[0] == '>':
header.write(line)
else:
seq.write(line)

header.close()
seq.close()
```

### Program 6
Let’s increase the difficulty just a bit…

+   Read a FASTA file line by line
+   Save the header in a variable and the sequence
in a different one
+   Print header and sequence separately

#### Program 6 - solution

```
seq_fasta = open("SingleSeq.fasta")

seq = ''

for line in seq_fasta:
if line[0] == '>':
header = line
else:
seq = seq + line.strip()

print header, seq
```

### Program 7



+   Implement program 6 by counting the number of
cysteine ("C") residues in the sequence
+   Print separately header, sequence and the
number of cysteine residues

#### Program 7 - solution

```
seq_fasta = open("SingleSeq.fasta")

seq = ''

for line in seq_fasta:
if line[0] == '>':
header = line
else:
seq = seq + line.strip()

num_cys = seq.count("C")

print header, seq, num_cys
```

### Program 8



+ Read a file in FASTA format line-by-line.
+   Print or write the record to a file only if the sequence
is from Homo sapiens.

#### Program 8 - solution

```
seq_fasta = open("SingleSeq.fasta")

seq = ''
header = ''

for line in seq_fasta:
if line[0] == '>':
if "Homo sapiens" in line:
header = line
else:
if header:
seq = seq + line

if header:
print header + seq
else:
print "The record is not from H. sapiens"
```

### Program 9

Very often in reality you will need to analyze several sequences….

```
SwissProt-Human.fasta
>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARRSS
WRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFY
LKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFY
YEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGD
AGEGEN
>sp|P62258|1433E_HUMAN 14-3-3 protein epsilon OS=Homo sapiens
MDDREDLVYQAKLAEQAERYDEMVESMKKVAGMDVELTVEERNLLSVAYKNVIGARRASW
RIISSIEQKEENKGGEDKLKMIREYRQMVETELKLICCDILDVLDKHLIPAANTGESKVF
YYKMKGDYHRYLAEFATGNDRKEAAENSLVAYKAASDIAMTELPPTHPIRLGLALNFSVF
YYEILNSPDRACRLAKAAFDDAIAELDTLSEESYKDSTLIMQLLRDNLTLWTSDMQGDGE
EQNKEALQDVEDENQ
>sp|Q04917|1433F_HUMAN 14-3-3 protein eta OS=Homo sapiens GN=YWHAH
MGDREQLLQRARLAEQAERYDDMASAMKAVTELNEPLSNEDRNLLSVAYKNVVGARRSSW
RVISSIEQKTMADGNEKKLEKVKAYREKIEKELETVCNDVLSLLDKFLIKNCNDFQYESK
VFYLKMKGDYYRYLAEVASGEKKNSVVEASEAAYKEAFEISKEQMQPTHPIRLGLALNFS
VFYYEIQNAPEQACLLAKQAFDDAIAELDTLNEDSYKDSTLIMQLLRDNLTLWTSDQQDE
EAGEGN
...
...
...

```


Download a Uniprot multiple sequence FASTA file. Write the record headers to a new file.

#### Program 9 - solution

```
fasta = open('SwissProt-Human.fasta')
headers = open('headers.txt', 'w')

for line in fasta:
if line[0] == '>':
headers.write(line)

headers.close()

>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
>sp|P62258|1433E_HUMAN 14-3-3 protein epsilon OS=Homo sapiens
>sp|Q04917|1433F_HUMAN 14-3-3 protein eta OS=Homo sapiens GN=YWHAH
```

### Program 10


Read a multiple sequence FASTA file and write the sequences to a new file separated by a blank line

#### Program 10 - solution

```
fasta = open('SwissProt-Human.fasta.fasta')
seqs = open('seqs.txt', 'w')

for line in fasta:
if line[0] == '>':
seqs.write('\n')
elif line[0] != '>':
seqs.write(line)
seqs.close()


seqs.write(line.strip() + '\n')
```

### Program 11



Read a file in FASTA format and copy to a new file the
records' AC.

#### Program 11 - solution

```
human_fasta = open('SwissProt-Human.fasta')
Outfile = open('SwissProt-Human-AC.txt','w')

for line in human_fasta:
if line[0] == '>':
AC = line.split('|')[1]
Outfile.write(AC + '\n')

Outfile.close()
```

### Program 12


+   Read FASTA records from a file
+   Count (and print) the cysteine residues in each
sequence.

#### Program 12 – solution I

```
fasta = open('sprot_prot.fasta')

seq = ''

for line in fasta:
if line[0] == '>' and seq == '':
header = line[4:10]
elif line[0] != '>':
seq = seq + line.strip()
elif line[0] == '>' and seq != '':
cys_num = seq.count('C')
print header, ': ', cys_num
header = line[4:10]
seq = ''

cys_num = seq.count('C')
print header, ': ', cys_num
```

#### Program 11 – solution II

```
fasta = open('sprot_prot.fasta')

seq = ''

for line in fasta:
if line[0]=='>':
if seq:
cys_num = seq.count('C')
print header, ':' , cys_num
header = line.split('|')[1]
seq = ''
else:
seq = seq + line.strip()
```

### Program 12


Read a multiple sequence FASTA file and write to a
new file only the records from Homo sapiens.

#### Program 12 – solution I

```
fasta = open('sprot_prot.fasta')
output = open('homo_sapiens.fasta', 'w')
seq = ''
for line in fasta:
if line[0] == '>' and seq == '':
header = line
elif line[0] != '>':
seq = seq + line
elif line[0] == '>' and seq != '':
if "Homo sapiens" in header:
output.write(header + seq)
header = line
seq = ''

if "Homo sapiens" in header:
output.write(header + seq)

output.close()
```
#### Program 12 – solution II

```
fasta = open('sprot_prot.fasta')
output = open('sprot_human.fasta', 'w')

seq = ''

for line in fasta:
if line[0]=='>':
if seq:
if "Homo sapiens" in header:
output.write(header + seq)
header = line
seq = ''
else:
seq = seq + line
output.close()
```
### Program 13 - homework

+  Read a multiple sequence file in FASTA format and only write to a new file the records the sequences of which start with a methionine ('M') and have at least two tryptophan residues ('W')

First:


+   Read a multiple sequence file in FASTA format and write to a new file
only the records of the sequences starting with a methionine ('M')


Then

+    Read a multiple sequence file in FASTA format and write to a new file
only the records of the sequences having at least two tryptophan
residues ('W')

Finally merge the two steps


```
fasta = open('SwissProtHuman.fasta','r')
outfile = open('SwissProtHuman-Filtered.fasta','w')

seq = ''

for line in fasta:
if line[0:1] == '>' and seq == '':
header = line
elif line [0:1] != '>':
seq = seq + line
elif line[0:1] == '>' and seq != '':
TRP_num = seq.count('W')
if seq[0] == 'M' and TRP_num > 1:
outfile.write(header + seq)
seq = ''
header = line

TRP_num = seq.count('W')
if seq[0] == 'M' and TRP_num > 1:
outfile.write(header + seq)
outfile.close()
```

### Program 14 - homework


Read a Genbank record and write to a file the nucleotide sequence in FASTA format. Extract and write to a file the gene sequence from the Candida albicans genomic DNA, chromosome 7, complete sequence (file ap006852.gbk)


Try to write it in FASTA format:
```
>AP006852
ccactgtccaatggctcaacacgccaatcatcatacaatacccccaacaggaatcaccaa
agtactgatgcttctcactatcaatagtttgtactttcaccacacaatagcagatgatcc
atctaaatccaccttcctatcgatcgtgaccacccccataaaataggtcaactccataaa
cacctccatcaccaacgctagactcacaacccagaacatgttaatcaaccggtgggccaa
Gtaccgttgtagctctctcgtaaacacaagaaccaacaccaaacaacatactacaactga
...
...
```

#### Program 14 - solution

```
InputFile = open("ap006852.gbk")
OutputFile = open("ap006852.fasta","w")
flag = 0

for line in InputFile:
if line[0:9] == 'ACCESSION':
AC = line.split()[1].strip()
OutputFile.write('>'+AC+'\n')
if line[0:6] == 'ORIGIN':
flag = 1
continue
if flag == 1:
fields = line.split()
if fields != []:
seq = ''.join(fields[1:])
OutputFile.write(seq +'\n')

InputFile.close()
OutputFile.close()
```

## Parsing data records

+ Start by visually inspecting the file you want to parse

+   Identify the information you want to extract

+   Identify separators to select your information using if conditions

+   Use  lists if you have to compare data from different files
