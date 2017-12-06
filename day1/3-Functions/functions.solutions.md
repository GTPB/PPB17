#### Solution to challenge #1

```
def triangle_area(b, h):
    A = (b*h)/2.0 # function  body
    return A      # function  body

print triangle_area(2.28, 3.55)
```

```
def triangle_area(b, h):
    return (b*h)/2.0

print triangle_area(2.28, 3.55)
```
<a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.md#challenge-1">back</a>
<br>
<br>

#### Solution to challenge #2

```
def get_values(arg1, arg2):
    s = arg1 + arg2
    d = arg1 - arg2
    p = arg1 * arg2
    return s, d, p

print get_values(15, 8)
```
<a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.md#challenge-2">back</a>
<br>
<br>



#### Solution to challenge #3

```
import math

def distance(p1, p2):
    dist = math.sqrt((p1[0]-p2[0])**2 +
                     (p1[1]-p2[1])**2 +
                     (p1[2]-p2[2])**2)
    return dist

p1 = (43.64, 30.72, 88.95)
p2 = (45.83, 31.11, 92.04)

print "Distance:", distance(p1, p2)
```
<a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.md#challenge-3">back</a>
<br>
<br>

#### Solution to challenge #4

```
def return_header(filename):
    fasta = open(filename)
    for line in fasta:
      if line[0] == '>':
        return line

print return_header('SingleSeq.fasta')
```
<a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.md#challenge-4">back</a>
<br>
<br>


#### Solution to challenge #5
```
def return_header(filename):
    fasta = open(filename)
    for line in fasta:
        if line[0] == '>':
            return line

filenames = ['SingleSeq1.fasta',
              'SingleSeq2.fasta',
              'SingleSeq3.fasta']

for name in filenames:
    print return_header(name)
```
<a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.md#challenge-5">back</a>
<br>
<br>


#### Solution to challenge #6
one possible solution
```
def return_header(filename):
    fasta = open(filename)
    for line in fasta:
        if line[0] == '>':
            return line

filenames = ['SingleSeq1.fasta',
             'SingleSeq2.fasta',
             'SingleSeq3.fasta']

output = open("headers.txt", "w")

for name in filenames:
    output.write(return_header(name) + '\n')

output.close()
```
another possible solution

```
def return_header(filename):
    fasta = open(filename)
    for line in fasta:
        if line[0] == '>':
          return line

filenames = ['SingleSeq1.fasta',
             'SingleSeq2.fasta',
             'SingleSeq3.fasta']
n = 0
for name in filenames:
    n = n + 1
    output = open("header" + str(n) + ".txt", "w")
    output.write(return_header(name))

output.close()
```
<a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.md#challenge-6">back</a>
<br>
<br>
