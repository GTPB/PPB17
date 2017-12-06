'''

Tabular Data - Exercise

The script reads the input table into a Python table,
transposes the table and writes the transposed table to 
a file.

'''

T = open("table-1.txt")

table = []

for line in T:
    table.append(line.split())

# Transpose table. It generates a transposed table.
columns = zip(*table)

for elem in columns:
    print '\t'.join(elem)
