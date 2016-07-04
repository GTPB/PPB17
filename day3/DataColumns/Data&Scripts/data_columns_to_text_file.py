'''
Data Columns - Exercise 8

The script uses two lists with data from neuron_data-2.txt
to write a table identical to neuron_data-2.txt.
Basically, it writes two lists of numbers to a text file

'''

Outfile = open('neuron_data-3.txt', 'w')

data1 =  [1, 2, 2, 1, 1, 2, 1, 2, 2]
data2 = [16.38, 139.90, 441.46, 29.03, 40.93, 
         202.07, 142.30, 346.00, 300.00]

# Using string concatenation: 
for i in xrange(len(data1)):
    Outfile.write(str(data1[i]) + '\t' + 
                  str(data2[i]) + '\n')

# Using string formatting: 
#for i in xrange(len(data1)):
#    Outfile.write("%i%s%f%s"%(data1[i],'\t', 
#                              data2[i],'\n'))

Outfile.close()
