<a href="https://github.com/ELIXIR-ITA-training/python_course"> Back to Timetable</a>

Hints for the whole project 

1. Write a `generate_peptide.py` script whose input is the `nuclear_antigen.fasta` file and output is a fasta file like this: 
```
>|125985|1
MAENGDNEKMAALE
>|125985|2
AENGDNEKMAALEA
>|125985|3
ENGDNEKMAALEAK
>|125985|4
```

where  125985 is the AC number of the original sequence and 1,2,3,4, ... is a counter. Should you find too complicated to write `generate_peptide.py`, there is a copy in the material folder 


2. What should the input & output of each function be?
3. Organize different output files in different directories.
4. How many BLAST databases do you need?
5. What blastp options create a good output format?
6. os.listdir(directory_name) --> list of file names
7. Make BLAST database --> page 433
8. BLAST output option -outfmt 6 --> output as a table
9. The best score is in the first line, last column of the BLAST output file.
10.The file.readline() function just reads the first line of the file.
