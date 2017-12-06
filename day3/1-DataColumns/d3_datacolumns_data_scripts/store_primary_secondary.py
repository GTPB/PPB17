'''

Data Columns - Exercise 4

Extend the script read_write_primary_secondary.py (Exercise 3)
so that it stores primary and secondary neuron lengths to 
different lists.

'''
# Open two output files
Outfile1 = open("primary_neurons.txt", "w")
Outfile2 = open("secondary_neurons.txt", "w")

# Initialise two different lists
primary = []
secondary = []

for line in open("neuron_data-2.txt"):
    data = line.split()
    print data
    if data[0] == '1':
        Outfile1.write(line)
	primary.append(float(data[1]))
    else:
        Outfile2.write(line)
	secondary.append(float(data[1]))

print primary, secondary

Outfile1.close()
Outfile2.close()
