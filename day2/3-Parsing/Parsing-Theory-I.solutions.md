<a name="c1"></a>
#### Solution to challenge #1

```
seq = open("SingleSeq.fasta")

for line in seq:
    print line
```

<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-1">back</a>
<a href="https://github.com/ELIXIR-ITA-training/python_course/blob/master/day2/3-Parsing/Parsing-Theory-I.md#challenge-1">back1</a>

#### Solution to challenge #2

```
seq = open("SingleSeq.fasta")
seq_2 = open("SingleSeq-2.fasta","w")

for line in seq:
    seq_2.write(line)

seq_2.close()
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-2">back</a>
href="https://github.com/ELIXIR-ITA-training/python_course/blob/master/day2/3-Parsing/Parsing-Theory-I.md#challenge-2">back1</a>


#### Solution to challenge #3
A number of possible solutions
```
seq = open("SingleSeq.fasta")

for line in seq:
    if line[0] == '>':
        print line

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
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-3">back</a>



#### Solution to challenge #4

```
fasta = open('SingleSeq.fasta')
header = open('header.txt', 'w’)

for line in fasta:
    if line[0] == '>':
        header.write(line)

header.close()
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-4">back</a>



#### Solution to challenge #5

```
fasta = open('SingleSeq.fasta')
seq = open('seq.txt','w')

for line in fasta:
    if line[0] != '>':
        seq.write(line)

seq.close()
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-5">back</a>



#### Solution to challenge #4 and #5 mergred


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
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-merge-programs-4-and-5">back</a>



#### Solution to challenge #6

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
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-6">back</a>



#### Solution to challenge #7

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
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-7">back</a>


#### Solution to challenge #8

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

Note the use of `if header`:

Apparently **there is no statement after the condition**


In Python empty objects in 'if' conditions are interpreted as `False` by default.


Therefore `header` here is treated as Boolean:
- if it is empty it will be interpreted as `False`
- once it is filled, it becomes `True`

<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-8">back</a>


#### Solution to challenge #9
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
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-9">back</a>


#### Solution to challenge #10

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
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-10">back</a>


#### Solution to challenge #11

```
human_fasta = open('SwissProt-Human.fasta')
Outfile = open('SwissProt-Human-AC.txt','w')

for line in human_fasta:
    if line[0] == '>':
        AC = line.split('|')[1]
        Outfile.write(AC + '\n')

Outfile.close()
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-11">back</a>



#### Solution to challenge #12

One possible solution:
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

another possible solution:

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
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-12">back</a>



#### Solution to challenge #13
One possible solution:
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
another possible solution:
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
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-13">back</a>



#### Solution II to challenge #14
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
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-14">back</a>


#### Solution II to challenge #15

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
<a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.md#challenge-15">back</a>
