<a href="https://github.com/ELIXIR-ITA-training/python_course"> Back to Timetable</a>

Hints for the whole project 

1. Write a `generate_peptide.py` script whose input is the `nuclear_antigen.fasta` file and output is a fasta file (`nuclear_antigen_peptides.fasta`) like this: 
```
>|125985|1
MAENGDNEKMAALE
>|125985|2
AENGDNEKMAALEA
>|125985|3
ENGDNEKMAALEAK
>|125985|4
```

where  125985 is the AC number of the original sequence and 1,2,3,4, ... is a counter. Should you find too complicated to write `generate_peptide.py`, there is an already written copy in the material folder  :) 

2.  Search the peptides in the P.falciparum proteome file (`Plasmodium_falciparum.fasta`). The proteome is in fasta format: don't forget to format it for BLAST using this command line: 

```
makebalstdb -in my_db_file.fasta  -dbtype prot 

```

`-dbtype` specifies the type of input molecules (`nucl`or `prot`) 

Notice that BLAST can take as input directly a multiple sequence fasta file (e.g. `nuclear_antigen_peptides.fasta`).

3. The BLAST output option `-outfmt 6` yelds output in tabular format where the best score is in the last column. 

