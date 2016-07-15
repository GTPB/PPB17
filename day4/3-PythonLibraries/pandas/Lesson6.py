#Lets take a look at the groupby function.

# Import libraries
import pandas as pd

# Our small data set
d = {'one':[1,1,1,1,1],
     't2wo':[2,2,2,2,2],
     'letter':['a','a','b','b','c'],
     'three':[3,3,3,3,3]}

# Create dataframe
df = pd.DataFrame(d)
print df

# Create group object
one = df.groupby('letter')

# Apply sum function
print one.sum()

letterone = df.groupby(['letter','one']).sum()
print letterone
print letterone.index

'''
You may want to NOT have the columns you are grouping by become your index, 
this can be easily achieved as shown below.
'''

letterone = df.groupby(['letter','one'], as_index=False).sum()
print letterone
print letterone.index
