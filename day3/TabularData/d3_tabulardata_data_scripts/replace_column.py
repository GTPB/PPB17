'''

Tabular Data - Exercise

The script transposes the intput table, removes a row and
inserts another row; then it transposes back the table (so that
rows become back columns) and writes the modified table to a 
tab-separated file.

'''

T = open("table-1.txt")

table = []

for line in T:
    table.append(line.split())

# Transpose the input table
columns = zip(*table)

# Remove a row (element in position 3 of the list)
columns.pop(3)
# Insert a row (a new element in position 3 of the list)
columns.insert(3, ['gene3', '20', '20', '20'])

# Transpose back the table: rows become columns
rows = zip(*columns)

for elem in rows: 
    print '\t'.join(elem)
