'''

Tabular Data - Exercise

The script creates an empty table of 10 x 10 cells,
fills it with the numbers from 1 to 100, and saves
the table to a tab-separated file.

'''

empty_table = [[0]*10 for x in xrange(10)]

n = 0
for row in empty_table:
    for i in xrange(len(row)):
        n = n + 1
        row[i] = str(n) 

outfile = open("table100.txt", "w")

for row in empty_table:
    outfile.write('\t'.join(row) + '\n')
outfile.close()
    
