'''

Data Columns - Exercise 3

The script reads the file neuron_data-2.txt, stores primary neurons 
to a file and secondary neurons to a different file.

'''
# Open two output files
Outfile1 = open("primary_neurons.txt", "w")
Outfile2 = open("secondary_neurons.txt", "w")

for line in open("neuron_data-2.txt"):
    data = line.split()
    if data[0] == '1':
        Outfile1.write(line)
    else:
        Outfile2.write(line)

Outfile1.close()
Outfile2.close()
