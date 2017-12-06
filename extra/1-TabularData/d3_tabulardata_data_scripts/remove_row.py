'''

Tabular Data - Exercise

The script removes a row from the input table and 
writes the modified table to a tab-separated file.

'''


T = open("table-1.txt")
out_T = open("table-1.out", "w")

table = []

for line in T:
    table.append(line.split())

# pop(i) removes the i-th element from a list
table.pop(2)

for elem in table:
    # 'x'.join(L) joints the elements of L using x as join.
    out_T.write('\t'.join(elem) + '\n')

out_T.close()

