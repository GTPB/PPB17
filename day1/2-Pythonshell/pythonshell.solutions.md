#### Solution to challenge #2
```
from math import pi
R = 10.0
V = (4.0/3.0)*pi*(R**3)
print V
```
in this case we import a specific object from math instead of importing the whole `math` module <br>
Advantages: if the module is big and we need only one  function; we not using the "." syntax and the name of the variable pi is shorter!  

<a href="https://github.com/joanamarques/python_course/blob/master/day1/2-Pythonshell/pythonshell.md#challenge-2
">back<a/>

<br>
<br>

#### Solution to challenge #3
```
import math

x1 = 43.64
y1 = 30.72
z1 = 88.95

x2 = 45.83
y2 = 31.11
z2 = 92.04

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
print dist
```
<a href="https://github.com/joanamarques/python_course/blob/master/day1/2-Pythonshell/pythonshell.md#challenge-3
">back<a/>
