#import packages
import pandas as pd
import numpy as np 
import argparse 
from tqdm import tqdm

def clean_data(messy_file, clean_file): 
    #Load Datea
    data = pd.read_csv(messy_file)

    #Drop duplicated data
    data.drop_duplicates(inplace=True)
    
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

    #Check for 4 unique values 
    unique_values = data['income_groups'].unique()
    print(f"Unique values in 'income_groups': {unique_values}")

    #Error Handling to ensure only 4 unique categories 
    if len(unique_values) == 4:
        print("Income groups are correctly cleaned.")
    else:
        raise ValueError("Error: Unexpected values found in 'income_groups'.")
    
    #replace NaN missing values with "unknown"
    data['income_groups'].fillna('unknown', inplace=True)  

    #Convert 'age' to integer data type 
    data['age'] = data['age'].astype(int)

    #Impute NaN with median age 
    data['age'].fillna(data['age'].median(), inplace=True)

    #Convert 'gender' to categorical data type 
    data['gender'] = data['gender'].astype('category')

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

    data.to_csv(clean_file, index=False)
    
    if __name__ == "__main__":
        clean_data('messy_population_data.csv', 'cleaned_population_data.csv')





                                  
                                  



















   











#income group incorrect data type 
