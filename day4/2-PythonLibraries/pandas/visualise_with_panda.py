#DATA VISUALISATION

#%matplotlib inline
import numpy as np
import pandas as pd

#Read the csv file of your choice
ver = pd.read_csv("gene_expression.csv")

#Plot counts of a specified column using Pandas
ver.loan_purpose_name.value_counts().plot(kind='barh')

