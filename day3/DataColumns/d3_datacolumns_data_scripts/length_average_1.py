'''

Data Columns - Exercise 5

The script reads neuron lengths from neuron_data.txt, 
calculates the neuron length average and prints the average.

'''

length_list = []

for line in open("neuron_data.txt"):
    length = length_list.append(float(line.strip()))

av = sum(length_list)/len(length_list)

print av
