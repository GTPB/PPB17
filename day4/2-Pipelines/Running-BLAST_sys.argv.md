<a href="https://github.com/ELIXIR-ITA-training/python_course"> Back to Timetable</a>


# Pipelines

### Running BLAST from Python

## Five ways to run BLAST
-  locally from the shell command line
-  locally from a Python script or interactive Python session
-  locally using Biopython
-  through the NCBI web server using Biopython
-  using your browser and the BLAST web page



## What are the advantages of running BLAST locally?

-  you can search a query sequence in a customised database, e.g. in a newly sequenced genome you are studying, or a set of protein sequences of your interest (e.g. only protein kinases).
-  you may want to insert the program in a pipeline
-  only by running BLAST locally you have full control over the sequence database and by that, reproducibility of your search

## Running Blast locally
-  Download and install the BLAST+ package from [here](http://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)
-  BLAST manual can be find [here](http://www.ncbi.nlm.nih.gov/books/NBK1762/)
-  The downloaded files are unpacked into a BLAST directory, and you have to add the path of this directory to the PATH environment variable of your computer (i.e. tell your system where to look for the installed BLAST programs)
-  Otherwise, you have to change to the BLAST directory on the shell and run BLAST from there
-   Inform the BLAST programs which directory to search for the databases
-   In other words you have to modify two environment variables: `PATH` and `BLASTDB`

### Modify the `PATH` environment variable
-  When you install the program from source, you will have to place the downloaded package under a desired directory, e.g. `/home/john`
-   When you unpack the package, a BLAST directory will appear in
`/home/john` (e.g. ``/home/john/ncbi-blast-2.2.23+``)
-  You have to add to the PATH environment variable the bin directory under this BLAST directory


*Under the bash shell (`.bash_profile` or `.bashrc`)*
```
PATH=$PATH:/home/john/blast-2.2.23+/bin
export PATH
```

*Under the tcsh shell (.cshrc ):*
```
setenv PATH ${PATH}:/home/john/ncbi-blast-2.2.23+/bin
```

>Notice that when you use the dmg disk to install BLAST on Mac OS X (10.4 or higher), all BLAST+ programs will be installed under `/usr/local/ncbi/blast/bin`


### Modify the BLASTDB environment variable

- Create the BLAST database directory `/blast/db` in your
home directory
```
mkdir /home/john/blast/db
```
-  This is the directory where you will put all the databases (either downloaded from the BLAST website or your custom ones) that you will use with BLAST.
-  Save at least a database in `/home/john/blast/db`
•  If you want to download a database from NCBI, go [here](ftp://ftp.ncbi.nlm.nih.gov/blast/db)

### Create a `.ncbirc` text file in your home directory having the following path specification

```
; Start the section for BLAST configuration
[BLAST]
; Specifies the path where BLAST databases are installed
BLASTDB=/home/john/blast/db
```

The semicolon at the beginning of the first and third lines indicates a comment.

-  Unless you use a pre-formatted database downloaded from the NCBI ftp site, you will need to format your custom sequence file.
-   `makeblastdb` produces BLAST databases from FASTA files:
```
makeblastdb –in genome.fasta -parse_seqids -dbtype prot
```
`-in` is the option for the input file <br/>
`-parse_seqids` enables parsing of sequence ids <br/>
`-dbtype` type of input molecules (nucl or prot)<br/>

The query sequence can be in FASTA format and this is the structure of the command line:
```
blastProgram -query InSeq.fasta -db Database -out OutFile
```
For example:
```
blastp -query P05480.fasta -out blast_output -db nr.00
```
`blastp` aligns protein sequences, nr.00 is the name of the BLAST-formatted database<br/>
`blast_output` is the name you have chosen for the BLAST output<br/>
`P05480.fasta` is a file that contains your query sequence in FASTA format<br/>

```
import os
S = "blastp -query P05480.fasta -out\
    blast_output -db nr.00"
os.system(S)
```


```
import subprocess
command_line = ['blastp','-query',
                'P05480.fasta','-out',
                'blout','-db','nr.00']
subprocess.call(command_line)
```

### Passing the input to a Python program from the command line


```
python gbk_to_fasta.py ap006852.gbk
```

```
import sys

print sys.argv

% python sys_argv.py
['sys_argv.py']

% python sys_argv.py ap006852.gbk
['sys_argv.py', 'ap006852.gbk']

% python sys_argv.py ap006852.gbk ap006852.fasta
['sys_argv.py', 'ap006852.gbk', 'ap006852.fasta']
```

>#### Challenge #1
---
>- Read the ap006852.gbk  file into a program (read_gbk.py) from the command line;
>- Read the file line-by-line and print the line corresponding to the 'LOCUS' identifier;
>-   Run the program.
>
---

<a href="https://github.com/ELIXIR-ITA-training/python_course/day4/Pipelines/Running-BLAST_sys.argv.solutions.md#solution-to-challenge-1">solution to challenge #1<a/>
<br>
<br>


>#### Challenge #2
---
>Run Blastp from a script for the three sequences
```
seqs = ['P00519', 'P05480', 'P12931']
```
>Use subprocess and a tabular format for the output
>
>The option for the output format is `-outfmt`<br/>
>0 = pairwise<br/>
>1 = query-anchored showing identities<br/>
>2 = query-anchored no identities<br/>
>3 = flat query-anchored, show identities<br/>
>4 = flat query-anchored, no identities<br/>
>5 = XML Blast output<br/>
>6 = tabular<br/>
>7 = tabular with comment lines<br/>
>8 = Text ASN.1<br/>
>9 = Binary ASN.1<br/>
>10 = Comma-separated values<br/>
>
---

a href="https://github.com/ELIXIR-ITA-training/python_course/day4/Pipelines/Running-BLAST_sys.argv.solutions.md#solution-to-challenge-2">solution to challenge #2<a/>
<br>
<br>




>#### Challenge #3
---
>Read the three blast output files and write to a new file file the values in the first and the third columns just for the first line of each file.
>
---

<a href="https://github.com/ELIXIR-ITA-training/python_course/day4/Pipelines/Running-BLAST_sys.argv.solutions.md#solution-to-challenge-3">solution to challenge #3<a/>
<br>
<br>
