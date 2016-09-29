infile = open('table-1.txt')
outfile = open('table.out', 'w')

table = []

for line in infile:
    col = line.strip().split('\t')
    table.append(col)

row5 = [str(i) for i in [5,3,7,19,8]]

print row5

#table.insert()

for row in table:
    outfile.write('\t'.join(row) + '\n')

outfile.close()
