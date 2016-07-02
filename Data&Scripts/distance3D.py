'''

Given the (x,y,z) coordinates of two points, 
the script calculates their distance in the 3D space.

'''

import math

x1 = 43.64
y1 = 30.72
z1 = 88.95

x2 = 45.83
y2 = 31.11
z2 = 92.04

text = "La distanza cercata e'"

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
print text  + str(dist)
