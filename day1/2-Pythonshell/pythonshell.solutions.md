#### Solution to challenge #2
```
from math import pi
R = 10.0
V = (4.0/3.0)*pi*(R**3)
print V
```
in this case we import a specific object from math instead of importing the whole `math` module <br>
Advantages: if the module is big and we need only one  function; we not using the "." syntax and the name of the variable pi is shorter!  
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
<br>
<br>

#### Solution to challenge #5
```
import math

ATP = 3.5
ADP = 1.8
Pi = 5.0
R = 0.00831
T = 298
deltaG0 = -30.5

deltaG = deltaG0 + R * T * math.log(ADP * Pi / ATP)

print deltaG
```
