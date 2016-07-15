'''

Data Columns - Exercise 1

The file reads the file with neuron lengths (neuron_data.txt) 
and saves an identical copy of the file.

'''

Infile = open('neuron_data.txt')
Outfile = open('neuron_data-copy.txt', 'w')

for line in Infile:
    Outfile.write(line)

Outfile.close()
