'''

Tabular Data - Exercise

The script reads the input table into a Python table,
transposes the table, removes a row, transposes back the table
and writes it to a file.

'''

T = open("table-1.txt")

table = []

for line in T:
    table.append(line.split())

# Transpose the table. Columns become rows.
columns = zip(*table)

# Remove a row (corresponding to element in position 3)
columns.pop(3)

# Transpose back. Rows become back columns
rows = zip(*columns)

for elem in rows: 
    print '\t'.join(elem)
