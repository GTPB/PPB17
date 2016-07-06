# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number

print 'Python version ' + sys.version
print 'Pandas version ' + pd.__version__


#GET DATA
Location = r'/Users/allegra1/Documents/didattica/TrainingCourses/TGAC/April2015/Course/Day4/PythonLibraries/Pandas/gene_expression.csv'
Location1 = r'/Users/allegra1/Documents/didattica/TrainingCourses/TGAC/April2015/Course/Day4/PythonLibraries/Pandas/gene_expression-few.csv'

df = pd.read_csv(Location)

print df.info()
print df.head()

df = pd.read_csv(Location, header=None)
print df.info()

print df.tail()
df = pd.read_csv(Location1, names=['Gene','Expression'])
print df.head(5)

#import os
#os.remove(Location)

#PREPARE DATA
'''
The data we have consists of genes and the expression values in different experiments. 
We already know that we have 1,002 records and none of the records are missing (non-null values). 
We can verify the "Gene" column still only has five unique genes.

We can use the unique property of the dataframe to find all the unique records of the "Gene" column.
'''

# Method 1:
print df['Gene'].unique()

# If you actually want to print the unique values:
for x in df['Gene'].unique():
    print x

# Method 2:
print df['Gene'].describe()

'''
Since we have multiple values per gene, we need to aggregate this data 
so we only have a gene to appear once. This means the 1,002 rows will 
need to become 10. We can accomplish this by using the groupby function.
'''

# Create a groupby object
gene = df.groupby('Gene')

# Apply the sum function to the groupby object
df = gene.sum()
print df


#ANALYSE DATA
'''

To find the most popular name or the baby name with the higest birth rate, 
we can do one of the following.

- Sort the dataframe and select the top row
- Use the max() attribute to find the maximum value

'''
# Method 1:
Sorted = df.sort(['Expression'], ascending=False)
print Sorted.head(1)

# Method 2:
df['Expression'].max()

#PRESENT DATA
'''
Here we can plot the Expression column and label the graph to show the end user 
the highest point on the graph. In conjunction with the table, the end user has
 a clear picture that gene3 is the most expressed gene in the data set.
'''

# Create graph
df['Expression'].plot(kind='bar')
plt.show()

print "The most experssed gene"
print df.sort(columns='Expression', ascending=False)




