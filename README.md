[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/u8FyG16T)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16774994)


## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: [125718]
- **Columns**: [5]

          Column  Non-Null Count    Dtype  Unique Values              Mean
0  income_groups          119412   object              8               N/A
1            age          119495  float64            101         50.007038
2         gender          119811  float64              3          1.578578
3           year          119516  float64            169       2025.068049
4     population          119378  float64         114925  111298303.154375


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

7. **[age Data Has Missing Value]**
   - Description: [The age variable has missing values (NaN)]
   - Affected Column(s): [data[['age']]]
   - Example: [print(data[data['age'].isna()][['age']])]
   - Potential Impact: [Incomplete analysis, grouping errors unless NaN values correctly handled, could impact validity of comparison across age if too much data missing, and may impact certain models without appropriate handling of NaN values through imputatin or other methods.]


8. **[gender Data Type]**
   - Description: [The gender variable is float64 data types which are primarly used used for continuous numerical data. Gender is a categorical variable.]
   - Affected Column(s): [data[['gender']]]
   - Example: [print(data['gender'].dtype)]
   - Potential Impact: [Inaccurate representation of a categorical data, models and functions will incorrectly handle the values as continious numerical variable ]

9. **[gender Data Has Missing Value]**
   - Description: [The gender variable has missing values (NaN)]
   - Affected Column(s): [data[['gender']]]
   - Example: [print(data[data['gender'].isna()][['age']])]
   - Potential Impact: [Incomplete analysis, grouping errors unless NaN values correctly handled, could impact validity of comparison across gender if too much data missing, and may impact certain models without appropriate handling of NaN values through imputatin or other methods.]


10. **[year Data Type]**
   - Description: [The year variable is float64 data types which are primarly used used for continuous numerical data. The year variable is a date-time variable.]
   - Affected Column(s): [data[['year']]]
   - Example: [print(data['year'].dtype)]
   - Potential Impact: [Inaccurate representation of a date-time data, models and functions will incorrectly interpret the date-time data as continuous values, and operations that rely on date-time foramt will not work ]

11. **[year Data Has Missing Value]**
   - Description: [The gender variable has missing values (NaN)]
   - Affected Column(s): [data[['year']]]
   - Example: [print(data['year'].value_counts(dropna=False))]
   - Potential Impact: [Incomplete analysis, grouping errors unless NaN values correctly handled, could impact validity of comparison across years if too much data missing, and may impact certain models without appropriate handling of NaN values through imputatin or other methods.]

12. **[population Data Type]**
   - Description: [The population variable is float64 data types which are primarly used used for continuous numerical data. Population is a discrete variable.]
   - Affected Column(s): [data[['population']]]
   - Example: [print(data['population'].dtype)]
   - Potential Impact: [Inaccurate representation of a discrete variable, models and functions will incorrectly interpret the discrete variable as continuous values, and operations that rely the correct variable assignment could perform improprely.]

13. **[population Data Has Missing Value]**
   - Description: [The population variable has missing values (NaN)]
   - Affected Column(s): [data[['population']]]
   - Example: [print(data['population'].value_counts(dropna=False))]
   - Potential Impact: [Incomplete analysis, grouping errors unless NaN values correctly handled.]


14 **[Duplicated Date]**
   - Description: [The dataset has duplicated rows which is innacurate.]
   - Affected Column(s): [data.columns]
   - Example: [print(data.duplicated().sum())]
   - Potential Impact: [Means, counts, and sums will be skewed since duplicated values will contribute more to these counts, functions that rely on counts will be incorrect, and models will overfit due to the duplicated data.]
   



 
