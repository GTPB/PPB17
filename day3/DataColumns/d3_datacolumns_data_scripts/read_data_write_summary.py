'''

Data Columns - Exercise 9

The script reads the neuron_data-2.txt file, calculates the number of primary neurons,
their total length, and the shortest and the longest lengths.
It finally writes a summary of the results to a file using string formatting.

'''

data = []

for line in open('neuron_data-2.txt'):
    columns = line.split()
    if columns[0] == '1': 
        data.append(float(columns[1]))

n_items = len(data)
total = sum(data)
shortest = min(data)
longest = max(data)

out = open("neuron_data_summary.txt","w") 
out.write("nr of lengths  : %7i \n"%(n_items))
out.write("tot length     : %7.1f \n"%(total))
out.write("shortest length: %7.2f \n"% (shortest))
out.write("longest length : %7.2f \n"%(longest))
out.close()

