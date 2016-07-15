'''

Data Columns - Exercise 6

The scripts reads neuron lengths from neuron_data-2.txt, 
calculates the neuron length average separately for primary 
and secondary neurons and prints the two averages

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
secondary_av = sum(secondary)/len(secondary)

print "primary neuron average: ",primary_av
print "secondary neuron average: ", secondary_av
