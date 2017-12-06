import rpy2.robjects as robjects
r = robjects.r
F= open ("table.txt")
lines=F.readlines()
l1=[]
l2=[]
l3=[]
l4=[]
for line in lines:
    col=line.split(',')
    l1.append(float(col[0]))
    l2.append(float(col[1]))
    l3.append(col[2])
    l4.append(float(col[3]))

    #l.append(float(line.split()[0]))

R_vector1= robjects.FloatVector(l1)
R_vector2= robjects.FloatVector(l2)
R_vector3= robjects.Vector(l3)
print ("mean",(r.mean(R_vector1)),(r.mean(R_vector2)))
print (R_vector3)
print ("2", "3")
