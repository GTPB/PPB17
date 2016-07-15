from operator import itemgetter
in_file = open("random_distribution.tsv")

# read table to floats
table = []
for line in in_file:
    rows = line.split()
    rows = [float(x) for x in rows]
    table.append(rows)
columns = zip(*table)
# sort the table by second, then by third column
table_sorted = sorted(table, key = itemgetter(1, 2))
table = zip(*columns)
# format table as strings
for row in table_sorted:
    row = [str(x) for x in row]
    print "\t".join(row)

