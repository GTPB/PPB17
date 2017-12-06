'''

Functions - Exercise 6

The script defines a function that takes as arguments 
two points [x1, y1, z1] and [x2, y2, z2] and returns 
the distance between the two points.

'''

import math

def distance(p1, p2): 
    dist = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)
    return dist

# The point x, y, z coordinates are given as tuples
p1 = (43.64, 30.72, 88.95)  
p2 = (45.83, 31.11, 92.04) 

print "Distance:", distance(p1, p2)
