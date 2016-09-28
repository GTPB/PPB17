infile = open("test_sample.fasta")

header = ''
seq = ''

for line in infile:
    if line.startswith('>') and not seq:
        header = line.strip()
    elif line.startswith('>') is False:
        seq += line.strip()
    elif line.startswith('>') and seq:
        AC = header.split('|')[1]
        print 'AC:' + AC + ', length:' + str(len(seq))
        header = line.strip()
        seq = ''

AC = header.split('|')[1]
print 'AC:' + AC + ', length:' + str(len(seq))
