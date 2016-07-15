# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt

#GET DATA
Location = r'/Users/allegra1/Documents/didattica/TrainingCourses/TGAC/April2015/Course/Day4/PythonLibraries/Pandas/gene_expression.csv'

df = pd.read_csv(Location, header = None)
df = pd.read_csv(Location, names=['Gene','Expression'])

print type(df)
print df.head()

'''
We are now going to save this dataframe into an Excel file, to then bring 
it back to a dataframe. We simply do this to show you how to read and write 
to Excel files.
We do not write the index values of the dataframe to the Excel file, since 
they are not meant to be part of our initial test data set.

'''
# Save results to excel
df.to_excel('Lesson3.xlsx', index=False)
print 'Done'

#Grab Data from Excel
'''
We will be using the read_excel function to read in data from an Excel file. 
The function allows you to read in specfic tabs by name or location.

Note: The location on the Excel file will be in the same folder as the notebook,
unless specified otherwise.

'''
# Location of file
Location1 = r'/Users/allegra1/Documents/didattica/TrainingCourses/TGAC/April2015/Course/Day4/PythonLibraries/Pandas/Lesson3.xlsx'

# Parse a specific sheet
#df = pd.read_excel(Location1, 0, index_col='Expression')
df = pd.read_excel(Location1, 0, header = False)
print  df.dtypes
print  df.index
print df.head()
