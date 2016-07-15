'''

Pipelines - Exercise

The script runs local BLAST+ on a protein query (P05480.fasta).
The database used is stored in the nr.00 directory, which is in 
the /home/blast/db directory.
The .ncbirc file has been created beforehand in the /home directory.
It contains the following lines:

; Start the section for BLAST configuration
[BLAST]
; Specifies the path where BLAST databases are installed
BLASTDB=/Users/allegra1/Documents/blast/db/nr.00

In this particular case, nr.00 is a database downloaded from the
NCBI ftp site, but it is possible to use a custom database (e.g. genome.fasta), 
which must originally be in FASTA format and processed using the command:

makeblastdb –in genome.fasta -parse_seqids -dbtype prot

'''

import os
S = "blastp -query P05480.fasta -out\
     blast_output -db nr.00"
os.system(S)

