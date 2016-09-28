
Infile =  open('telomerase.txt')
Infile.readline()
insulin_seq =  Infile.read()
stripped_seq = insulin_seq.strip()

for amino_acid in 'ACDEFGHKILMNPQRSTVYW':
    number_of_aa= stripped_seq.count(amino_acid)
    freq_aa = float(number_of_aa)/len(stripped_seq)
    print amino_acid, round(freq_aa, 3)





