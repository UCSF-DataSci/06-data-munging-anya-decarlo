[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/u8FyG16T)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16774994)


## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: [125718]
- **Columns**: [5]

 | Column         | Non-Null Count | Dtype   | Unique Values | Mean           |
|----------------|----------------|---------|---------------|----------------|
| income_groups  | 119412         | object  | 8             | N/A            |
| age            | 119495         | float64 | 101           | 50.007038      |
| gender         | 119811         | float64 | 3             | 1.578578       |
| year           | 119516         | float64 | 169           | 2025.068049    |
| population     | 119378         | float64 | 114925        | 111298303.1544 |



### Identified Issues

1. **[income_groups Data Type]**
   - Description: [The income_groups variable is an object data type. Object data types are used for strings and would be more appropriate for names, addresses, or other related strings. The income_groups variable is instead a tiered categorical variable.]
   - Affected Column(s): [data[['income_groups']]]
   - Example: [print(data['income_groups'].dtype)]
   - Potential Impact: [Less efficient, pandas will perform operations slower if it treats each category as its own object, and any mispelling in the same income_groups won't be recognized. Also, if income_groups has any NAn values, they will be incorrectly handled in certain operations.]


2. **[income_groups Data Typos]**
   - Description: [The income_groups variable has typos in each income category low, lower_middle, upper_middle, and high]
   - Affected Column(s): [data[['income_groups']]]
   - Example: [print(data['income_groups'].unique())]
   - Potential Impact: [Within each income group, there are two reported distinct catgories for each true category. Meaning, each income catgeory has two catgegories due to typos. The population within each income catgory is not accurutely represented. ]

3. **[income_groups Data Has Missing Values]**
   - Description: [The income_groups variable has missing values (NaN)]
   - Affected Column(s): [data[['income_groups']]]
   - Example: [print(data[data['income_groups'].isna()])]
   - Potential Impact: [Incomplete analysis, grouping errors unless NaN values correctly handled, could impact validity of comparison across income groups if too much data missing, and may impact certain models without appropriate handling of NaN values through imputatin or other methods.]

4. **[age Data Type]**
   - Description: [The age variable is a float64 which are used for continuous numerical variables. Age is a discrete numerical variable.]
   - Affected Column(s): [data[['age']]]
   - Example: [print(data['age'].dtype)]
   - Potential Impact: [Age is a whole number and should be represented accurutely, floats take up more memory, 25.0 and 25 are the same but is  treated differenly when age is a float, models may treat age as a continuous variable and not a discrete one.]

5. **[age Data Has Missing Value]**
   - Description: [The age variable has missing values (NaN)]
   - Affected Column(s): [data[['age']]]
   - Example: [print(data[data['age'].isna()][['age']])]
   - Potential Impact: [Incomplete analysis, grouping errors unless NaN values correctly handled, could impact validity of comparison across age if too much data missing, and may impact certain models without appropriate handling of NaN values through imputatin or other methods.]

6. **[gender Data Type]**
   - Description: [The gender variable is float64 data types which are primarly used used for continuous numerical data]
   - Affected Column(s): [data[['gender']]]
   - Example: [print(data['gender'].dtype)]
   - Potential Impact: [Inaccurate representation of a categorical data, models and functions will incorrectly handle the values as continious numerical variable ]

7. **[gender Data Has Missing Values]**
   - Description: [The gender variable has missing values (NaN)]
   - Affected Column(s): [data[['gender']]]
   - Example: [print(data[data['gender'].isna()][['age']])]
   - Potential Impact: [Incomplete analysis, grouping errors unless NaN values correctly handled, could impact validity of comparison across gender if too much data missing, and may impact certain models without appropriate handling of NaN values through imputatin or other methods.]


8. **[year Data Type]**
    - Description: [The year variable is float64 data types which are primarly used used for continuous numerical data. The year variable is a date-time variable.]
    - Affected Column(s): [data[['year']]]
    Example: [print(data['year'].dtype)]
    - Potential Impact: [Inaccurate representation of a date-time data, models and functions will incorrectly interpret the date-time data as continuous values, and operations that rely on date-time foramt will not work ]

9. **[year Data Has Missing Value]**
    - Description: [The gender variable has missing values (NaN)]
    - Affected Column(s): [data[['year']]]
    - Example: [print(data['year'].value_counts(dropna=False))]
    - Potential Impact: [Incomplete analysis, grouping errors unless NaN values correctly handled, could impact validity of comparison across years if too much data missing, and may impact certain models without appropriate handling of NaN values through imputatin or other methods.]

10. **[population Data Type]**
    - Description: [The population variable is float64 data types which are primarly used used for continuous numerical data. Population is a discrete variable.]
    - Affected Column(s): [data[['population']]]
    - Example: [print(data['population'].dtype)]
    - Potential Impact: [Inaccurate representation of a discrete variable, models and functions will incorrectly interpret the discrete variable as continuous values, and operations that rely the correct variable assignment could perform improprely.]

11. **[population Data Has Missing Value]**
    - Description: [The population variable has missing values (NaN)]
    - Affected Column(s): [data[['population']]]
    - Example: [print(data['population'].value_counts(dropna=False))]
    - Potential Impact: [Incomplete analysis, grouping errors unless NaN values correctly handled.]

12. **[Duplicated Data]**
    - Description: [The dataset has duplicated rows which is innacurate.]
    - Affected Column(s): [data.columns]
    - Example: [print(data.duplicated().sum())]
    - Potential Impact: [Means, counts, and sums will be skewed since duplicated values will contribute more to these counts, functions that rely on counts will be incorrect, and models will overfit due to the duplicated data.]


13. **[Handling Outliers]**
    - Description: [The dataset may have outliers in the numerical data]
    - Affected Column(s): [data.columns]
    - Example: [Outliers are values that that fall outside of
    1.5 +- IQR]
    - Potential Impact: [Outliers can skew results, influence models, hide patterns in data, impact predictions,and affect normality assumptions]

14. **[Checking Valid Age Range]**
    - DescriptionL [The dataset has 102 values for age]
    - Affect Column(s): [data[['age']]]
    - Example: [Ages greater less than 1, greater than 100]
    - Potential Impact: [Age is assumed in years and therefore can't be 0]

15. **[Checking Valid Years]**
    -Description: [There are years greater than the present year in the dataset]
    - Affected Columns: [data[['year']]]
    - Example: [ 2.0 2111-01-01   ]
    - Potential Impact: [These are invalid age years.]


    ### Indentified Solutions 

1. **[income_groups Data Type]**
   - Solution Technique: [Convert income groups from object to categorical]
   - Justification: [Operations will perform better, grouping will be faster, and sorting can be based on categories. Logical ordering will also be allowed. ]
   - Impact on Dateset: [Variable type is changed]
   - Any Assumptions: [Assuming the catefories will be grouped by their level, assuming the categories of income are tiered]


2. **[income_groups Data Typos]**
   - Solution Technique: [Define replacements, replace with dictionary, ensure only 4 categories in dataset]
   - Justification: [ Categories need to be represented correctly, each group needs to be accurate]
   - Impact on Dateset: [The amount of categories is now 4]
   - Any Assumptions: [Assuming the catefories will be grouped by their level, assuming the categories of income are tiered]

3. **[income_groups Data Has Missing Values]**
    - Solution Technique: [Add "unknown" catgory to income_groups]
    - Justification: [Allows to do analysis including unknown groups while still maintaing integrity of original 4 groups and other data without removing]
    - Impact on Dataset: [Added a new category to income_groups but no rows deleted]
    - Any Assumptions: [Assumed data was unknown and not missing for any other reason]

4.  **[age Data Type]** 
    - Solution Technique: [Converted data type to int64]
    - Justification [Neccessary for models using discrete values, accurate representation of age]
    - Impact on Data Set [age is not an integer]
    - Any Assumptions [None]

5. **[age Data Has Missing Values]**
    - Soltion Technique: [Imputed missing age with median]
    - Justification: [Preserve data and statistical power of age]
    - Impact on Data Set: [Distribution remained fairly similar. Mean before imputation: 49.9 std before imputation: 29.15, Mean after imputation: 49.9, std after imputation: 28.43]
    - Any Assumptins : [Assumed Normal Distribution]

6. **[gender Data Type]**
    - Solution Technique: [Changed data type to categorical]
    - Justification: [Analyses need categorical variables to provide accurate insight across gender categories]
    - Impact on Data Set: [Changed data type of gender to category]
    - Any Assumptions: [Assumed 3 was the correct category count and not a coding error]

7. **[gender Data Has Missing Values]**
    - Solution Technique: [Changed NaN values to unknown]
    - Justification: Allows data analysis including unknown groups while still maintaing integrity 
    - Impact on Data Set: [Added new category to gender]
    - Any Assumptions: [NA]

8. **[year Data Type]**
    - Solution Technique: [Changed all values to date_time format]
    - Justification: [Date-time format neccessary for accurate models and operations that rely on date-time format]
    - Impact on Data Set: [variables now date time]
    - Any Assumptons: [Assumed format correct and that all months and dates were accurate, example: no Feburary 31st]

9. **[year Data Has Missing Vales]**
    - Solution Technique: [Sentintal Imputation using year 1800 ]
    - Justification: [Allowed date-time format to remain intact]
    - Impact on Data Set: [Averages on year could be impacted without proper handling]
    - Any Assumptions: [Assunmes user knows 1800 is a sentintal imputation and not a valid date]

10. **[population Data Type]**
    - Solution Technique: [Replaced data type with int]
    - Justification: [Neccessary to perform accurate models using population as a discrete value] 
    - Impact on Data Set: [data type now an integer]
    - Any Assumptions: [NA]

11. **[population Data Has Missing Value]**
    - Solution Technique: [Imputation with mean]
    - Justification: [Preserve data and statistical power of population ] 
    - Impact on Data Set: [missing values now are replaced with mean]
    - Any Assumptions: [Normal Distribution of population]

12. **[Duplicated Data]**
    - Solution Technique: [remove duplicated data from the dataset]
    - Justification: [innacurate statistical analysis without removal, functions would be incorrect, models would overfit, bad data practice to keep]
    - Impact on Data Set: [2950 rows were removed]
    - Any Assumptions: [Assume less than 10% of original data]

13. **[Handling Outliers]** 
    - Solution Technique: [Identify and cap outliers]
    - Justification: [Preserve the size of the dataset and do not have sufficient evidence that outliers aren't relevent to the study]
    - Impact on Data Set: []
    - Any Assumptions: [Assuming outliers are due to actual variability in data and are not measurnment errors]

14. **[Checking Valid Age Range]
    - Solution Technique: [Identify ages less than 0 and greater than 100 and remove any matches]
    - Impact on Data Set: []

15. **[Checking Valid Year Range]**
    - Solution Technique: [Identify current date and remove entries greater than current date]
    - Justification: [Years greater than 2023 are invalid. Although it is 2024, we will only include 2024 ]
    - Impact on Dataset: [58% of the rows were removed. This greatly reduced the statistical power of the dataset.]
    - Any assumptions: [We are assuming thsi data set is collected data, rather than simulated data. This data set could be forecasted data, but we are assuming it is population data collected. ] 
### Clean Data Summary

| Column         | Non-Null Count | Dtype            | Unique Values | Mean              |
|----------------|----------------|------------------|---------------|------------------:|
| income_groups  | 105,716        | category         | 4             | N/A               |
| age            | 105,716        | int64            | 101           | 50.037109         |
| gender         | 105,716        | category         | 3             | N/A               |
| year           | 105,716        | datetime64[ns]   | 169           | N/A               |
| population     | 105,716        | int64            | 99,033        | 113,277,972.864921 |


### Final Thoughts

1. The cleaned data set in comparison to the original one has a better handling of missing values, correct income categories, and appropriate data types for the numerical variables. 
2. Checking if the impact of imputating was challenging, making new categories was challenging, and fixing why the categorical variables were still reporting as a Dtype of object was difficult. Challenges were overcome by changing approach to handling NaN values. Instead of trying to keep them in non integer variables, all rows with NaN were removed. 
3. I learned how to organize the process of cleaning data and how to check if data cleaning was actually implemented. Through the checks I wrote in the code, it seemed like it was working, but after importing the cleaned data set and displaying the new formatted table, I found more errors. 
4. Although the date-time format for year has been changed, the Dtype is still reporting sa int64 which needs to be investigated. Further analysis and visualization of the data prior to imputation would allow for better analysis of how imputation impacted the spread of the data. How I handled missing values also needs to be improved. 
*update 10-26-24* 
Handling of missing values was improved. All variabels are reported as correct Dtype. Further improvement includes checking to make sure no years are past 2024, capping outliers, renaming gender categories, and handling the high percent of missing data removed. This is a fun project!






   