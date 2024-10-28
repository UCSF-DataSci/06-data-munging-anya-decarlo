#import packages
import pandas as pd
import numpy as np 
import argparse 
from tqdm import tqdm

#load data set 
data = pd .read_csv("messy_population_data.csv")

#basic info
data.info()

#unique values for each column 
unique_counts = data.nunique()

#means for each numerical column 
means = data.mean(numeric_only=True)

print("\nUnique Values Per Column",  unique_counts)
print("\nMean Values for Numerical Columns",means)

import pandas as pd

#summarizing basic info neatly 
summary = pd.DataFrame({
    'Column': data.columns,
    'Non-Null Count': data.notnull().sum().values,
    'Dtype': data.dtypes.values,
    'Unique Values': data.nunique().values,
    'Mean': data.mean(numeric_only=True).reindex(data.columns, fill_value='N/A').values
})

#display the formatted table
print(summary)

# unique values for non numerical variables 
print(data['income_groups'].unique())
print(data['gender'].unique())

#missing values for income_group 
print(data[data['income_groups'].isna()][['income_groups']])

#unique value counts for income_groups
print(data['income_groups'].value_counts(dropna=False))

#missing values for age
print(data[data['age'].isna()][['age']])

#unique value counts for age 
print(data['age'].value_counts(dropna=False))

#print unique values for age
print(data['age'].unique())

#any negative values or values over 100 for age 
print(data[(data['age'] < 0) | (data['age'] > 100)])

#unique value counts for gender 
print(data['gender'].value_counts(dropna=False))

#unique value counts for year 
print(data['year'].value_counts(dropna=False))

#unique value counts for population
print(data['population'].value_counts(dropna=False))

#NA values counts in each column 
print(data.isnull().sum())

#duplicated data
print(data.duplicated())

#count duplicated data 
print(data.duplicated().sum())