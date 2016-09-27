#### Solution to challenge #1
One  solution:

```
from operator import itemgetter
data = [
[5, 10, 4, 3, 2],
[6, 7, 8, 9, 10],
]

data.sort(key=itemgetter(1))

for row in data:
    for i in xrange(len(row)):
        row[i] = str(row[i]) #replace nr with strings

for elem in data:
    print "\t".join(elem) + "\n”
```

another possible solution:

```
from operator import itemgetter

data = [
[5, 10, 4, 3, 2],
[6, 7, 8, 9, 10],
]

data.sort(key=itemgetter(1))

# format table as strings
for row in data:
    row = [str(x) for x in row]
      print "\t".join(row)
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day3/4-TabularData/TabularData.md#challenge-1"> back<a/>
<br>
<br>


#### Solution to challenge #2

```
neurons = open("neuron_data.txt")

table1 = []
table2 = []

for line in neurons:
    col = line.split()
    if col[0] == 'Primary':
        table1.append([col[0],float(col[1])])
    else:
        table2.append([col[0],float(col[1])])

```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day3/4-TabularData/TabularData.md#challenge-2"> back<a/>
<br>
<br>


#### Solution to challenge #3

```
from operator import itemgetter

# sort by second column
table1.sort(key=itemgetter(1))

#show the three longest neurons
print table1[-3:]
```

<a href="https://github.com/ELIXIR-ITA-training/python_course/day3/4-TabularData/TabularData.md#challenge-3"> back<a/>
<br>
<br>


#### Solution to challenge #4

```
# rotate the table
columns = zip(*table1)
# take the 1st  column (1st  row of table1)
lengths = columns[1]
print lengths
# print average
print sum(lengths) / len(lengths)
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day3/4-TabularData/TabularData.md#challenge-4"> back<a/>
<br>
<br>


#### Solution to challenge #5
Create an empty table of 10 x 10 cells

```
>>> empty_table = [[0]*10 for x in xrange(10)]
>>> empty_table
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0,
0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0,
0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0,
0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day3/4-TabularData/TabularData.md#challenge-5"> back<a/>
<br>
<br>


#### Solution to challenge #6
Fill the table with the numbers from 1 to 100
```
>>> empty_table = [[0]*10 for x in xrange(10)]
>>> n = 0
>>> for row in empty_table:
...     for i in xrange(len(row)):
...         n = n + 1
...         row[i] = str(n)
...
>>> empty_table
[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], ['11', '12', '13', '14', '15', '16', '17', '18',
'19', '20'], ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30'], ['31', '32', '33',
'34', '35', '36', '37', '38', '39', '40'], ['41', '42', '43', '44', '45', '46', '47', '48', '49',
'50'], ['51', '52', '53', '54', '55', '56', '57', '58', '59', '60'], ['61', '62', '63', '64',
'65', '66', '67', '68', '69', '70'], ['71', '72', '73', '74', '75', '76', '77', '78', '79',
'80'], ['81', '82', '83', '84', '85', '86', '87', '88', '89', '90'], ['91', '92', '93', '94',
'95', '96', '97', '98', '99', '100']]
```
<a href="https://github.com/ELIXIR-ITA-training/python_course/day3/4-TabularData/TabularData.md#challenge-6"> back<a/>
<br>
<br>


#### Solution to challenge #7
Save the table to a tab-separated file
```
empty_table = [[0]*10 for x in xrange(10)]

n = 0
for row in empty_table:
for i in xrange(len(row)):
    n = n + 1
    row[i] = str(n)

outfile = open("table100.txt", "w")

for row in empty_table:
    outfile.write('\t'.join(row) + '\n')
outfile.close()
```<a href="https://github.com/ELIXIR-ITA-training/python_course/day3/4-TabularData/TabularData.md#challenge-7"> back<a/>
<br>
<br>
