'''

Data Columns - Exercise 7

The script reads neuron lengths from neuron_data-2.txt, calculates the 
standard deviation of the neuron lengths for the primary neurons and prints
average and standard deviation.

'''


primary = []
secondary = []

for line in open("neuron_data-2.txt"):
    data = line.split()
    if data[0] == '1':
	primary.append(float(data[1]))
    else:
	secondary.append(float(data[1]))

primary_av = sum(primary)/len(primary)

import math

total = 0.0
for value in primary:
    total += (value - primary_av) ** 2
stddev = math.sqrt(total / len(primary))

print "Length average of primary neurons: ", primary_av
print "Standard deviation of primary neuron lengths: ", stddev

