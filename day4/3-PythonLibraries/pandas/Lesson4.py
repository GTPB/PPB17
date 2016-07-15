#LESSON-4
'''
Now we were going to go back to the basics. We will be working with a small data set so 
that you can easily understand what I am trying to explain. We will be adding columns, 
deleting columns, and slicing the data many different ways. Enjoy!
'''

# Import all libraries needed for the tutorial
import pandas as pd
#from numpy import random
#import matplotlib.pyplot as plt

# Our small data set
d = [0,1,2,3,4,5,6,7,8,9]

# Create dataframe
df = pd.DataFrame(d)
#print df

# Lets change the name of the column
df.columns = ['ID']
#print df

# Lets add a column
#df['NewCol'] = 5
df['NewCol'] = [i + 1 for i in df['ID']]
#print df

# Lets modify our new column
df['NewCol'] = df['NewCol'] + 1
#print df

# We can delete columns
del df['NewCol']
df

# Lets add a couple of columns
df['test'] = 3
df['square'] = df['ID']**2
print df

# If we wanted, we could change the name of the index
i = ['a','b','c','d','e','f','g','h','i','j']
df.index = i
#print df

#We can now start to select pieces of the dataframe using loc.
print 'The column values corresponding to index a are:'
print df.loc['a']

# df.loc[inclusive:inclusive]
print df.loc['a':'d']

# df.iloc[inclusive:exclusive]
# Note: .iloc is strictly integer position based. It is available from [version 0.11.0] (http://pandas.pydata.org/pandas-docs/stable/whatsnew.html#v0-11-0-april-22-2013) 
print df.iloc[0:3]

#We can also select using the column name.
print df['ID']
print df[['ID', 'test']]

# df['ColumnName'][inclusive:exclusive]
print df['ID'][0:3]
print df['square'][5:]
print df[['square', 'test']][:3]

#There is also some handy function to select the top and bottom records of a dataframe.
# Select top N number of records (default = 5)
df.head()
# Select bottom N number of records (default = 5)
df.tail()

#We can also flip the column names with the index using the T (transpose) function.
transpose = df.T
print transpose

print transpose.index







