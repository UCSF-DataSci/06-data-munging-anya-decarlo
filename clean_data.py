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

    #Drop duplicates with loading bar
    print("Removing duplicates...")
    with tqdm(total=1) as pbar:
        data.drop_duplicates(inplace=True)
        pbar.update(1)

    #Verify duplicated data was removed 
    if len(data) == initial_row_count:
        print("Error: No duplicates were removed.")
    else:
        print(f"All duplicates removed. {initial_row_count - len(data)} rows removed.")

    #Track Current Row Count after duplication removal 
    current_row_count=len(data)

    #Replace age empty strings with NaN 
    data['age'] = data['age'].replace(['', ' '], pd.NA)

    #Check for age NaN values before imputation 
    age_nans = data['age'].isna().sum()

    #Impute age NaN values with the mean 
    data['age'] = data['age'].fillna(data['age'].mean())

    #Convert 'age' to integer 
    data['age'] = data['age'].round().astype(int)

    #Checking Ages are in Valid Range 
    print("\nChecking for invalid ages (outside 0-100 range)...")
    invalid_ages = data[(data['age'] < 0) | (data['age'] > 100)]
    if not invalid_ages.empty:
        print(f"Invalid ages found:\n{invalid_ages}")
    else:
        print("All ages are within the valid range (0-100).")
    
    #Remove any non valid ages 
    print("\nFiltering out invalid ages...")
    valid_data = data[(data['age'] >= 0) & (data['age'] <= 100)]
    print(f"Row count after filtering invalid ages: {len(valid_data)} "
          f"(removed {len(data) - len(valid_data)} rows)")


    #Convert empty strings and spaces in'population' to NaN
    data['population'] = data['population'].replace(['', ' '], pd.NA)  

    #Check for NaN before imputation 
    population_nans = data['population'].isna().sum()

    #Impute 'population' NaN values with mean 
    data['population'] = data['population'].fillna(data['population'].mean())

    #Convert 'population" to integer 
    data['population'] = data['population'].round().astype(int)

    #Check if any NaN after imputation 
    population_nans_left = data['population'].isna().sum()
    age_nans_left = data['age'].isna().sum()    

    #Print statement to ensure no NaN values after imputation 
    if population_nans_left == 0:
        print("All NaN values in 'population' have been imputed.")
    else:
        print(f"Warning: {population_nans_left} NaN values remain in 'population'.")
    if age_nans_left == 0:
        print("All NaN values in 'age' have been imputed.")
    else:
        print(f"Warning: {age_nans_left} NaN values remain in 'age'.")

    #Replace empty strings with NaN 
    data.replace('', pd.NA, inplace=True)

    #Drop missing values
    data.dropna(inplace=True)

    #Check if too many rows were removed 
    rows_after_nan_removal = len(data)
    rows_removed_due_to_nan = current_row_count - rows_after_nan_removal

    if rows_removed_due_to_nan == 0:
        print("No rows with NaN or missing values were removed.")
    elif rows_removed_due_to_nan / current_row_count > 0.1: 
        print(f"Warning: {rows_removed_due_to_nan} rows removed due to missing values, "
            f"which is {rows_removed_due_to_nan / current_row_count:.2%} of the data.")
    else:
        print(f"Missing value removal successful. {rows_removed_due_to_nan} rows removed.")

    print(f"Initial row count: {initial_row_count}")
    print(f"Final row count: {rows_after_nan_removal}")
    print(f"Total rows removed: {initial_row_count - rows_after_nan_removal}")

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
    
    #Convert 'gender' to categorical data type 
    data['gender'] = data['gender'].astype('category')

    #Convert 'year' to date-time data type
    data['year'] = pd.to_datetime(data['year'].astype(int).astype(str), format='%Y', errors='coerce')

    #Summarize cleaned data 
    summarize_new = pd.DataFrame({
        'Column': data.columns,
        'Non-Null Count': data.notnull().sum().values,
        'Dtype': data.dtypes.values,
        'Unique Values': data.nunique().values,
        'Mean': data.mean(numeric_only=True).reindex(data.columns, fill_value='N/A').values
    })

    #Display the cleaned data table   
    print(summarize_new)
    
    #Save clean data to CSV
    data.to_csv(clean_file, index=False)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean messy data file.")
    parser.add_argument('messy_file', help='Path to the messy input CSV file')
    parser.add_argument('clean_file', help='Path to the cleaned output CSV file')
    args = parser.parse_args()
    
    clean_data(args.messy_file, args.clean_file)