<a href="https://github.com/ELIXIR-ITA-training/python_course"> Back to Timetable</a>



# Parsing data records I

Two sequence records in FASTA format:


```
>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARRWRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN

>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARRWRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
```

> ####  **Challenge #1**
---
>
>Open the file `SingleSeq.fasta`, read its content line by line and print it
>
---

See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-#1">solution to challenge #1</a>

<br>
<br>


> #### **Challenge #2**
---
>
>Open the file `SingleSeq.fasta`, read its content line by line and write it to another file.
>
---

See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-2">solution to challenge #2</a>

<br>
<br>

### Writing different things depending on a condition

Read a sequence in FASTA format and print only the header of the sequence

```
>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARWRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
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
  statementN
```

Check these conditions:

- ` 'ACTC'[0] == 'C' `  is  True or false?
- ` 'ACTC'[0] == 'A' `  is  True or false?


Operators:

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
if 'A' in nucl: print 'A'
if 'C' in nucl: print 'C'
if 'T' in nucl: print 'T'
if 'G' in nucl: print 'G'
```

> #### **Challenge #3**
---
>Read a sequence in FASTA format  from the file  `SingleSeq.fasta` and print only the header of the sequence
>
>
```
>>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARWRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
```
>
---


See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-3">solution to challenge #3</a>
<br>
<br>

> #### **Challenge #4**
---
>
>Read a file in FASTA format and write to a new file
only the header of the record.
>
---

See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-4">solution to challenge #4</a>

<br>
<br>

> #### **Challenge #5**
---
>
>Read a file in FASTA format and write to a new file only the sequence (without the header).
>
---

See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-5">solution to challenge #5</a>

<br>
<br>

> #### **Challenge: Merge programs 4 and 5**
---
> In other words, read a file in FASTA format and write the header to a file and the sequence to a different one.
>
---

See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-4-and-5-mergred"> solution to challenges #4 and #5 merged</a>

<br>
<br>

> #### **Challenge #6**
---
>Let’s increase the difficulty just a bit…
>
>+   Read a FASTA file line by line
>+   Save the header in a variable and the sequence in a different one
>+   Print header and sequence separately
>
---

See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-6">solution to challenge #6</a>


<br>
<br>

> #### **Challenge #7**
---
>+   Implement challenge #6 by counting the number of cysteine ("C") residues in the sequence
>+   Print separately header, sequence and the number of cysteine residues
>
---


See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-7">solution to challenge #7</a>

<br>
<br>

> #### **Challenge #8**
---
>+ Read a file in FASTA format line-by-line.
>+   Print or write the **record** to a file only if the sequence is from Homo sapiens.
>
---

See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-8">solution to challenge #8</a>

<br>
<br>


> #### **Challenge #9**
---
>Very often in reality you will need to analyze several sequences….
>
> Consider the content of the file `SwissProt-Human.fasta`

```
SwissProt-Human.fasta

>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARRSSWRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYYEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
>sp|P62258|1433E_HUMAN 14-3-3 protein epsilon OS=Homo sapiens
MDDREDLVYQAKLAEQAERYDEMVESMKKVAGMDVELTVEERNLLSVAYKNVIGARRASWRIISSIEQKEENKGGEDKLKMIREYRQMVETELKLICCDILDVLDKHLIPAANTGESKVFYYKMKGDYHRYLAEFATGNDRKEAAENSLVAYKAASDIAMTELPPTHPIRLGLALNFSVFYYEILNSPDRACRLAKAAFDDAIAELDTLSEESYKDSTLIMQLLRDNLTLWTSDMQGDGEEQNKEALQDVEDENQ
>sp|Q04917|1433F_HUMAN 14-3-3 protein eta OS=Homo sapiens GNYWHAHMGDREQLLQRARLAEQAERYDDMASAMKAVTELNEPLSNEDRNLLSVAYKNVVGARRSSWRVISSIEQKTMADGNEKKLEKVKAYREKIEKELETVCNDVLSLLDKFLIKNCNDFQYESKVFYLKMKGDYYRYLAEVASGEKKNSVVEASEAAYKEAFEISKEQMQPTHPIRLGLALNFSVFYYEIQNAPEQACLLAKQAFDDAIAELDTLNEDSYKDSTLIMQLLRDNLTLWTSDQQDEEAGEGN
...
...
...

```
>
>Download a Uniprot multiple sequence FASTA file. Write the record headers to a new file.
>
---


See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-9">solution to challenge #9</a>

<br>
<br>

> #### **Challenge #10**
---
>Read a multiple sequence FASTA file and write the sequences to a new file separated by a blank line
>
---


See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-10">solution to challenge #10</a>

<br>
<br>

> #### **Challenge #11**
---
>Read a file in FASTA format and copy to a new file the records' Accession Numbers (AC).
>
---


See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-11">solution to challenge #11</a>

<br>
<br>

> #### **Challenge #12**
---
>+   Read FASTA records from a file
>+   Count (and print) the cysteine residues in each sequence.
>
---


See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-12">solution to challenge #12</a>

<br>
<br>

> #### **Challenge #13**
---
>Read the multiple sequence FASTA file `sprot_prot.fasta` and write to a new file only the records from Homo sapiens.
>
---


See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-13">solution to challenge #13</a>

<br>
<br>

> #### **Challenge #14 homework**
---
>+  Read a multiple sequence file in FASTA format and only write to a new file the records the sequences of which start with a methionine ('M') and have at least two tryptophan residues ('W')
>
>First:
>
>+   Read a multiple sequence file in FASTA format and write to a new file only the records of the sequences starting with a methionine ('M')
>
>Then
>
>+    Read a multiple sequence file in FASTA format and write to a new file only the records of the sequences having at least two tryptophan residues ('W')
>
>Finally merge the two steps
>
---



See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-14">solution to challenge #14</a>

<br>
<br>

> #### **Challenge #15 homework**
---
>Read a Genbank record and write to a file the nucleotide sequence in FASTA format. Extract and write to a file the gene sequence from the Candida albicans genomic DNA, chromosome 7, complete sequence (file ap006852.gbk)
>
> Try to write it in FASTA format:
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
>
---


See the <a href="https://github.com/ELIXIR-ITA-training/python_course/day2/3-Parsing/Parsing-Theory-I.solutions.md#solution-to-challenge-15">solution to challenge #15</a>



## Parsing data records

+ Start by visually inspecting the file you want to parse

+   Identify the information you want to extract

+   Identify separators to select your information using if conditions

+   Use  lists if you have to compare data from different files
