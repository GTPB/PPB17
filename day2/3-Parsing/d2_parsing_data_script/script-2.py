infile = open("test_sample.fasta")

seq = ''
header = ''

for line in infile:
    if line[0] == '>' and seq == '':
        header = line
    elif line[0] != '>':
        seq = seq + line.strip()
    elif line[0] == '>' and seq != '':
        print header, seq
        header = line
        seq = ''

print header, len(seq)


