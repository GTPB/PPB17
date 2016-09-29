ac_cancer = open("cancer-expressed.txt")

ac_list = []

for line in ac_cancer:
    ac = line.strip()
    ac_list.append(ac)

print ac_list
    


'''
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
'''
