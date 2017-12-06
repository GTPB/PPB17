primary = []
secondary = []

for line in open("neuron_data-2.txt"):
    data = line.split()
    print data
    if data[0] == '1':
	     primary.append(float(data[1]))
    else:
	     secondary.append(float(data[1]))

print max(primary), min(secondary)
