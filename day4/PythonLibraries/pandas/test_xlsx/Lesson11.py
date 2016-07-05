#Lesson 11
#Grab data from multiple excel files and merge them into a single dataframe.

import pandas as pd
import os

#Create 3 excel files

# Create DataFrame
d = {'Gene':[1], 'Number':[255]}
df = pd.DataFrame(d)
print df

# Export to Excel
df.to_excel('test1.xlsx', sheet_name = 'test1', index = False)
df.to_excel('test2.xlsx', sheet_name = 'test2', index = False)
df.to_excel('test3.xlsx', sheet_name = 'test3', index = False)
print 'Done'

#Place all three Excel files into a DataFrame

#Get a list of file names but make sure there are no other excel files 
#present in the folder.

# List to hold file names
FileNames = []

# Your path will be different, please modify the path below.
os.chdir(r'/Users/allegra1/Documents/didattica/TrainingCourses/TGAC/April2015/Course/Day4/PythonLibraries/Pandas/test_xlsx/')

# Find any file that ends with ".xlsx"
for files in os.listdir("."):
    if files.endswith(".xlsx"):
        FileNames.append(files)

#FileNames = ['test1.xlsx', 'test2.xlsx', 'test3.xlsx']

#Create a function to process all of the excel files.

def GetFile(fnombre):
    # Path to excel file
    # Your path will be different, please modify the path below.
    location = r'/Users/allegra1/Documents/didattica/TrainingCourses/TGAC/April2015/Course/Day4/PythonLibraries/Pandas/test_xlsx/' + fnombre
    # Parse the excel file
    # 0 = first sheet
    df = pd.read_excel(location, 0)
    
    # Tag record to file name
    df['File'] = fnombre
    
    # Make the "File" column the index of the df
    return df.set_index(['File'])

# Go through each file name, create a dataframe, and add it to a list.
# i.e. df_list = [df, df, df]
# Create a list of dataframes
df_list = [GetFile(fname) for fname in FileNames]
print df_list

# Combine all of the dataframes into one
big_df = pd.concat(df_list)
print big_df
print big_df.dtypes
# Plot it
big_df['Gene'].plot(kind='bar');

import matplotlib.pylab as plt
plt.show() 
