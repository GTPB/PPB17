
#### Solution to challenge #1

```
neuron_lengths = []

for line in open("neuron_data.txt"):
    neuron_lengths.append(float(line.strip()))

print neuron_lengths
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/blob/master/day3/3-DataColumns/DataColumns.md#challenge-1">back <a/>
<br>
<br>



#### Solution to challenge #2
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

<a href="https://github.com/ELIXIR-ITA-training/python_course/blob/master/day3/3-DataColumns/DataColumns.md#challenge-2">back <a/>
<br>
<br>


#### Solution to challenge #3
Ona possible solution

```
length_list = []

for line in open("neuron_data.txt"):
    length_list.append(float(line.strip()))

av = sum(length_list)/float(len(length_list))
print av
```

 another possible solution

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
<a href="https://github.com/ELIXIR-ITA-training/python_course/blob/master/day3/3-DataColumns/DataColumns.md#challenge-3">back <a/>
<br>
<br>



#### Solution to challenge #4

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
<a href="https://github.com/ELIXIR-ITA-training/python_course/blob/master/day3/3-DataColumns/DataColumns.md#challenge-4">back <a/>
<br>
<br>


#### Solution to challenge #5

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
<a href="https://github.com/ELIXIR-ITA-training/python_course/blob/master/day3/3-DataColumns/DataColumns.md#challenge-5">back <a/>
<br>
<br>



#### Solution to challenge #6
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
<a href="hhttps://github.com/ELIXIR-ITA-training/python_course/blob/master/day3/3-DataColumns/DataColumns.md#challenge-6">back <a/>
<br>
<br>


#### Solution to challenge #7
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
<a href="https://github.com/ELIXIR-ITA-training/python_course/blob/master/day3/3-DataColumns/DataColumns.md#challenge-7">back <a/>
<br>
<br>
