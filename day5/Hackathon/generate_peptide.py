infile = open('nuclear_antigens.fasta')
out = open('nuclear_antigens_pep.fasta', 'w')

seq = ''

for line in infile:
    if line[0] == '>':
        if seq:
            for i in xrange(0, len(seq)):
                pep = seq[i:i+14]
                if len(pep) ==  14:
                    out.write('>|%s|%i\n%s\n' % (header, i + 1, pep))
        header = line.split('|')[1]
        seq = ''
    else:
        seq = seq + line.strip()

if seq:
    for i in xrange(0, len(seq)):
        pep = seq[i:i+14]
        if len(pep) ==  14:
            out.write('>|%s|%i\n%s\n' % (header, i, pep))

out.close()
 
    
