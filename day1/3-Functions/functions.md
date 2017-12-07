<a href="https://github.com/joanamarques/python_course"> Back to Timetable</a>


## Functions

**A block of code that performs a specific task**


Why do we use functions?


They are useful to organise your script, in particular if you need to **repeat actions** (e.g. a complex calculation) several times


A function can be accessed from different parts of a script or even from different scripts.


In order to use a function, you have first to define it and then to call it


<img src="../../img/functions1.png" alt="slot" style="width: 300px;"/>

<img src="../../img/functions2.png" alt="slot" style="width: 300px;"/>


---
> ####  **Challenge #1**
>
>
>-  Write a function triangle_area(b, h) that returns the area of a triangle
>-    Call the function for b = 2.28 and h = 3.55
>-    Print the result
>
---
<img src="../../img/trianglev2.png" alt="slot" style="width: 100px;"/>

See the <a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.solutions.md#solution-to-challenge-1">solution to challenge #1<a/>
<br>
<br>

## General remarks

- The statement to define a function is `def`

- A function must be **defined** and **called** using brackets

- The body of a function is a block of code that is initiated
by a colon character followed by *indented instructions*

- The last indented statement marks the end of a function definition

### More remarks

- You   can   insert   in   the   body   of   a   function   a documentation  string  in  quotation  marks.  This  string can  be  retrieved  using  the `__doc__`  attribute  of  the function object

- You can **pass arguments** to a function

- A function may or may not **return** a value

```
def triangle_area(b, h):
    '''Returns the area of a triangle'''  
    return (b*h)/2.0

print triangle_area.__doc__
```
---
> ####  **Challenge #2**
>
> Define a function with two arguments: `get_values(arg1, arg2)` that returns the sum, the difference, and the product of `arg1` and `arg2`.
>
---

See the <a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.solutions.md#solution-to-challenge-2">solution to challenge #2<a/>
<br>
<br>



## Remarks
-  The statement `return` exits a function, optionally passing
back a value to the caller.

-   A `return`  statement  with  no  arguments  is  the  same  as returning `None`.

-   The returned value can be assigned to a variable

```
>>> def j(x,y):
...     return x + y
...
>>> s = j(1, 100)
>>> print s
101
>>>
```
## Function arguments

Every Python object can be passed as argument to a function.<br>
A function call can be the argument of a function too.

```
>>> def increment(x):
...     return x + 1
...
>>> def print_arg(y):
...     print y
...
>>> print_arg(increment(5))
6
>>>
```

Multiple parameters can be passed to a function. In this case, the order of the arguments in the caller must be exactly the same as that in the function definition

```
>>> def print_funct(num, seq):
...     print num, seq
...     return
...
>>> print_funct(10, "ACCTGGCACAA")
10 ACCTGGCACAA
>>>
```

The sequence of arguments passed to a function is a **tuple**


AND


Functions return multiple values in the form of
**tuples** as well


## Tuples


A tuple is an **immutable** sequence of object

This means that, once you have defined it, you cannot change/replace its elements


`variabile = (item1, item2, item3,…)``


Brackets are optional, i.e. you can use either:


`Tuple = (1,2,3)` or   `Tuple = 1,2,3`


A **tuple of a single item** must be written either:


`Tuple = (1,)` or   `Tuple = 1,`

```
>>> my_tuple = (1,2,3)
>>> my_tuple[0]       #indexing
1
>>> my_tuple[:]       #slicing
(1, 2, 3)
>>> my_tuple[2:]      #slicing
(3, )
```

BUT

```
>>> my_tuple[0] = 0     #re-assigning
(Forbidden)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support
item assignment
>>>
```

```
>>> def f(a,b):
...     return a + b, a*b, a-b

>>> sum, prod, diff = f(20, 2)
>>> print sum

>>> result = f(20, 2)
>>> print result
>>> print result[0]
```

It is possible to assign a name to the arguments of a function. In this case, the order is not important

```
>>> def print_funct(num, seq):
...     print num, seq
...     return
...
>>> print_funct(seq = "ACCTGGCACAA", num = 10)
10 ACCTGGCACAA
>>>
```


## Default arguments

It is also possible to use default arguments (optional). These optional arguments must be placed in the last position(s) of the function definition

```
def print_funct(num, seq = "A"):
    print num, seq
    return

print_funct(10, "ACCTGGCACAA")

print_funct(10)
```

## Summary

- def F(x,y):
- F(3,'codon')
- return
- function arguments


---
> ####  **Challenge #3**
>
>Write a function that takes as arguments two points [x1, y1, z1] and [x2, y2, z2] and returns the distance between the two points.
>
---

See the <a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.solutions.md#solution-to-challenge-3">solution to challenge #3<a/>
<br>
<br>

---
> ####  **Challenge #4**
>
>Write a function that :
>-  Takes as input a file name (of a FASTA file).
>-  Opens the file.
>-  Returns the header of the sequence record.
>
>Print the header.
>
---

See the <a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.solutions.md#solution-to-challenge-4">solution to challenge #4<a/>
<br>
<br>

---
> ####  **Challenge #5**
>
>Insert the function call in a for loop running on a list of 3 sequence file names.
>
---

See the <a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.solutions.md#solution-to-challenge-5">solution to challenge #5<a/>
<br>
<br>

---
> ####  **Challenge #6**
>
>Consider two output schemes for exercise 4:
>1. All the the headers are written to the same output file
>2. Each header is written in a separate output file
>
---


See the <a href="https://github.com/joanamarques/python_course/blob/master/day1/3-Functions/functions.solutions.md#solution-to-challenge-6">solution to challenge #6<a/>
<br>
<br>


## General remarks

-  Python uses **dynamical** namespaces: when a function is
called, *its namespace is automatically created*

- The variables defined in the body of a function live in its *local* namespace and not in the script (or module) *global* namespace

- Local objects can be made global using the **global** statement

- When a function is called, names of the objects used in its body
are first searched in the function namespace and subsequently,
if they are not found in the function body, they are searched in
the script (module) global namespace.

```
>>> def f():
...     x = 100
...     return x
...
>>> print x
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> f()
100
>>> print x
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>>
```
`x` is a local name of the function `f()` namespace and it is not recognised by the `print` statement in the main script  even after the function call

```
>>> def g():
...     global x
...     x = 200
...     return x
...
>>> print x
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> g()
200
>>> print x
200
>>>
```

The variable `x`, defined in the body of the `g()` function, is made global using the **global** statement but is recognized by the `print` statement in the main script  only after the function call

```
>>> y = "ACCTGGCACAA"
>>> def h():
...     print y
...
>>> h()
'ACCTGGCACAA'
```

`y` is recognized when `h()` is called as it is a global name.
The  number  of  arguments  can  be  variable  (i.e.  can  change  from  one function call to the other); in this case, you can use * or ** symbols.

1st  case             (\*args) =>          tuple of arguments
2nd  case             (\**args)=>          dictionary of arguments

```
>>> def print_args(\*args):
...     print args
...     return
...
>>> print_args(1,2,3,4,5)
(1, 2, 3, 4, 5)
>>> print_args("Hello world!")
(‘Hello world!’,)
>>> print_args(100, 200, "ACCTGGCACAA")
(100, 200, ‘ACCTGGCACAA’)
>>> def print_args2(**args):
...     print args
...     return
...
>>>  print_args2(num  =  100,  num2  =  200, seq  =
"ACCTGGCACAA")
{'num': 100, 'seq': 'ACCTGGCACAA', 'num2': 200}
```

<a href="https://github.com/joanamarques/python_course/readme.md> Back to Timetable</a>
