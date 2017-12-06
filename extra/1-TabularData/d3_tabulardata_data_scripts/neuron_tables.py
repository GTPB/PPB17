'''

Tabular Data - Exercise

The script: 
1) generates two tables from neuron_data.txt, one for 
primary and one for secondary neurons.
2) sorts the primary neuron’s table and shows the three 
longest neurons. 
3) turns the primary neuron's table and calculates 
the neuron length average.

'''

neurons = open("neuron_data.txt")

table1 = []
table2 = []

for line in neurons:
    col = line.split()
    if col[0] == 'Primary':
        table1.append([col[0], float(col[1])])
    else:
        table2.append([col[0], float(col[1])])

# sort by second column
from operator import itemgetter
table1.sort(key=itemgetter(1))

#show the three longest neurons
print table1[-3:]


# turn the table and calculate average
columns = zip(*table1)
lengths = columns[1]
print lengths
print sum(lengths) / len(lengths)

