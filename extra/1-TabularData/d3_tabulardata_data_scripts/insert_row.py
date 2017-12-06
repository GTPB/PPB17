'''

Tabular Data - Exercise

The script inserts a row in the input table and 
writes the modified table to a tab-separated file.

'''

T = open("table-1.txt")
out_T = open("table-1.out", "w")

table = []

for line in T:
    table.append(line.split())

# This is the row to insert
exp5 = ['5', '17', '17', '2', '13']
# insert(i, x) inserts x in position i
table.insert(2, exp5)

for elem in table:
    out_T.write('\t'.join(elem) + '\n')

out_T.close()

