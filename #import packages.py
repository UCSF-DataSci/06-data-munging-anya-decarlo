#import packages
import pandas as pd
import numpy as np 
import argparse 
from tqdm import tqdm


data = pd .read_csv("cleaned_population_data.csv")


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

print(data['income_groups'].dtype) 