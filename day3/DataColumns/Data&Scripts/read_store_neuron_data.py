'''

Data Columns - Exercise 2

The script reads neuron lengths from neuron_data.txt and
stores them as floating point numbers into a list.

'''

length_list = []

for line in open("neuron_data.txt"):
    print line.split()
    length_list.append(float(line.strip()))

print length_list
