'''

Tabular Data - Exercise

The script reads a table from a file into a 
Python table (i.e. a list of lists).

'''

T = open("table-1.txt")

table = []

for line in T:
    # split() returns a list
    table.append(line.split())

print table

