

# Data columns

## Reading  data from a table and writing data to a table

After this module you can:
+   Read a list of numbers from a text file
+  Write a list of numbers to a text file
+  Calculate an average value
+  Calculate a standard deviation

We will use the file `neuron_data.txt` containing data on dendrites lengths:

```
16.38
139.90
441.46
29.03
40.93
202.07
142.30
346.00
300.00
```

and the file `neuron_data-2.txt` that contains the same data plus an extra column with the indication 1 for primary neurons and 2 for secondary neurons:

```
1         16.38
2         139.90
2         441.46
1         29.03
1         40.93
2         202.07
1         142.30
2         346.00
2         300.00
```
### What do we have to do?

+  Read data columns from files
+  Store data columns to data structures
+  Convert text into numbers
+  Convert numbers into text
+  Write text to data columns (i.e. with appropriate format)


**Our Goal  is to beat Excel at its own game!**

## Some useful built-in functions

- `split()` Stores elements from different columns to a list
- `unpack()` Stores elements from different columns to a list using a given format
- `join()` Concatenates objects from a list
- `strip()` Removes blank spaces and newline characters
- `int()` Converts a string into an integer
- `float()` Converts a string into a floating point number
- `str()`  Converts an object into a string
- `repr()` Converts an object into a string



### Program 1

1.  Write a program that reads the file with neuron lengths (`neuron_data.txt`) and saves an identical copy of the file.
2. Extend the program so that neuron lengths are stored as floating point numbers into a list.


#### Program 1 - solution
```
neuron_lengths = []

for line in open("neuron_data.txt"):
    neuron_lengths.append(float(line.strip()))

print neuron_lengths
```

#### Program 2

Extend the program so that it read data form `neuron_data-2.txt` and  stores primary and secondary neuron lengths to different lists.

### Program 2 - solution

```
primary = []
secondary = []

for line in open("neuron_data-2.txt"):
    data = line.split()
    if data[0] == '1':
        primary.append(float(data[1]))
    else:
        secondary.append(float(data[1]))

print primary, secondary
```

## Manipulating data in the columns

+  Calculate max and min length
+  Calculate their average length
+  Calculate the standard deviation

<img src="../../img/builtin.png" alt="slot" style="width: 300px;"/>

### Program 3

1.  Extend program 1 so that it calculates the neuron length average and prints it.
2.  Extend program 2 so that it calculates the neuron length average separately for primary and secondary neurons. Print the two averages: which neurons are on average longer?

#### Program 3.1 - solution

```
length_list = []

for line in open("neuron_data.txt"):
    length_list.append(float(line.strip()))

av = sum(length_list)/float(len(length_list))
print av
```

#### Program 3b - solution
```
primary = []
secondary = []

for line in open("neuron_data-2.txt"):
    data = line.split()
    if data[0] == '1':
        primary.append(float(data[1]))
    else:
        secondary.append(float(data[1]))

primary_av = sum(primary)/float(len(primary))
secondary_av = sum(secondary)/float(len(secondary))

print "primary neuron average: ",primary_av
print "secondary neuron average: ", secondary_av
```

### Program 4


Extend program 3 so that it calculates the standard deviation
of the neuron length.

#### Program 4 solution

```
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

print primary_av, stddev
```

## How to **write** data to columns

This implies that data needs to be nicely formatted and written to a file

+  String concatenation
+  String formatting

The argument of the `write()` function MUST be a string

```
>>> out = open('data_out.txt', 'w')
>>> out.write(3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: expected a character buffer object
>>>
```

```
>>> out = open('data_out.txt', 'w')
>>> out.write(str(3))
>>>
```

An example of string concatenation using `+` :
```
out = open('data_out.txt', 'w')
out.write(str(1) + '\t' + str(16.38) + '\n')
out.close()
```


### Program 5

Use two lists with data from `neuron_data-2.txt` to write a table identical to `neuron_data-2.txt`.  Do it using **string concatenation**.


#### Program 5 - solution

```
out = open('neuron_data-3.txt', 'w')

data1 =  [1, 2, 2, 1, 1, 2, 1, 2, 2]
data2 = [16.38, 139.90, 441.46, 29.03, 40.93,
202.07, 142.30, 346.00, 300.00]

for i in xrange(len(data1)):
    out.write(str(data1[i]) + '\t' +
    str(data2[i]) + '\n')
out.close()
```

Nice output can be generated by formatting characters:

```
print '%d'%(77)
print '%s'%('text')
print '%4.1f'%(2.1111)
```
```
print 'The square root of %5.2f is %5.2f'%(a, math.sqrt(a))

print 'The square root of %10.2f is %5.2f'%(a, math.sqrt(a))

print "%i%s%f%s"%(1, '\t', 2.5, '\n')
```

### Program 6

Use two lists with data from `neuron_data-2.txt` to write a table identical to `neuron_data-2.txt`. Do it using **string formatting**.

#### Program 6 - solution

```
out = open('neuron_data-3.txt', 'w')

data1 =  [1, 2, 2, 1, 1, 2, 1, 2, 2]
data2 = [16.38, 139.90, 441.46, 29.03, 40.93,
202.07, 142.30, 346.00, 300.00]

for i in xrange(len(data1)):
  out.write("%i%s%f%s"%(data1[i],'\t', data2[i],'\n'))

out.close()
```
If you want to switch two columns:

```
Outfile = open('neuron_data-3.txt', 'w')

data1 =  [1, 2, 2, 1, 1, 2, 1, 2, 2]
data2 = [16.38, 139.90, 441.46, 29.03, 40.93,
202.07, 142.30, 346.00, 300.00]

for i in xrange(len(data1)):
Outfile.write("%i%s%f%s"%(data2[i],'\t', data1[i],'\n'))

Outfile.close()
```

## Reading and writing tables
+ Read each table column into a different list
+  Use a for loop running over the length of the list to write the elements of the lists to a file (using string concatenation or formatting)
+  You can write the columns in a different order

### Match the formatting expressions and their result

<img src="../../img/expression_values.png" alt="slot" style="width: 300px;"/>

### Program 7


Write a program that reads the `neuron_data-2.txt` file, calculates the number of primary neurons, their total length, and the shortest and the longest lengths.


Write the results to a file using string formatting.


You can repeat the exercise for secondary neurons.

#### Program 7 - solution

```
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
```
