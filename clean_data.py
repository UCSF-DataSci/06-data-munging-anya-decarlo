#import packages
import pandas as pd
import numpy as np 
import argparse 
from tqdm import tqdm

def clean_data(messy_file, clean_file): 
    #Load Datea
    data = pd.read_csv(messy_file)

    # Save initial value counts 
    initial_value_counts = {
        'income_groups': data['income_groups'].value_counts(dropna=False),
        'age': data['age'].value_counts(dropna=False),
        'gender': data['gender'].value_counts(dropna=False),
        'year': data['year'].value_counts(dropna=False),
        'population': data['population'].value_counts(dropna=False)

    }

    #Initial row count for data 
    initial_row_count = len(data)

    #Drop duplicated data
    data.drop_duplicates(inplace=True)

    #Verify duplicated data was removed 
    if len(data) == initial_row_count:
        print("Error: No duplicates were removed.")
    else:
        print(f"Duplicate removal successful. {initial_row_count - len(data)} rows removed.")

    #Convert "income_group" to categorical data type 
    data['income_groups'] = data['income_groups'].astype('category')

    #Create Replacements for Typos in "income_group"
    income_group_replacements = {
    'low_income_typo': 'low_income',
    'lower_middle_income_typo': 'lower_middle_income',
    'upper_middle_income_typo': 'upper_middle_income',
    'high_income_typo': 'high_income'
}
    #Replace typos 
    data['income_groups'] = data['income_groups'].replace(income_group_replacements)

    #add uknown
    if 'unknown' not in data['income_groups'].cat.categories:
        data['income_groups'] = data['income_groups'].cat.add_categories('unknown')

    #replace NaN missing values with "unknown"
    data['income_groups'].fillna('unknown', inplace=True)  

    #Check for 4 unique values 
    unique_values = data['income_groups'].unique()
    print(f"Unique values in 'income_groups': {unique_values}")

    #Error Handling to ensure only 5 unique categories 
    if len(unique_values) == 5:
        print("Income groups are correctly cleaned.")
    else:
        raise ValueError("Error: Unexpected values found in 'income_groups'.")
    
    #convert age and impute na with mean
    data['age'] = data['age'].fillna(data['age'].median()).astype('Int64')
    
    #Convert 'gender' to categorical data type 
    data['gender'] = data['gender'].astype('category')

    #Add unknown category 
    data['gender'] = data['gender'].cat.add_categories('unknown')

    #Replace NaN missing values with "unknown"
    data['gender'].fillna('unknown', inplace=True)
    
    #Convert 'year' to date-time data type
    data['year'] = pd.to_datetime(data['year'].astype('Int64'), format='%Y', errors='coerce')

    #Convert NaN values to year 1800
    data['year'].fillna(pd.to_datetime('1800', format='%Y'), inplace=True) 

    #Convert 'population' to integer data type and converts NaN to O
    data['population'] = data['population'].fillna(0).astype(int)  

    #Impute 'population' 0 values with mean 
    data['population'].fillna(data['population'].mean(), inplace=True)

    #New value counts for each variable 
    final_value_counts = {
        'income_groups': data['income_groups'].value_counts(dropna=False),
        'age': data['age'].value_counts(dropna=False),
        'gender': data['gender'].value_counts(dropna=False),
        'year': data['year'].value_counts(dropna=False),
        'population': data['population'].value_counts(dropna=False)
    }

#Print Comparison of Value Counts 
    print("\nComparison of Value Counts (Before vs After Cleaning):")
    for col in initial_value_counts:
        print(f"\nColumn: {col}")
        print("Before Cleaning:\n", initial_value_counts[col])
        print("After Cleaning:\n", final_value_counts[col])

    #Save clean data to CSV
    data.to_csv(clean_file, index=False)
    
if __name__ == "__main__":
    clean_data('messy_population_data.csv', 'cleaned_population_data.csv')
