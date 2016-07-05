'''

Tabular Data - Exercise

The script sorts a Python table by column 1 (i.e. the second column).
Then it converts the table integer elements into strings
and writes the table to a tab-separated file.

'''

# You can use itemgetter from the operator module 
#to retrieve specific fields from a list
from operator import itemgetter

data = [
[5, 10, 4, 3, 2],
[6, 7, 8, 9, 10],
]

# This command will sort a table by column 1 (i.e.
# the second column)
data.sort(key=itemgetter(1))

# The elements of each row are converted into strings
# List comprehension is used
data2 = []
for row in data:
    row = [str(i) for i in row]
    data2.append(row)

for elem in data2:
   print "\t".join(elem) + "\n"

# This is a different way to convert elements of each
# row into strings. 
#for row in data:
#    for i in xrange(len(row)):
#        row[i] = str(row[i])

#for elem in data:
#   print "\t".join(elem) + "\n"

