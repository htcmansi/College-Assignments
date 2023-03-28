import pandas as pd
import numpy as np
import csv
from scipy import stats
from scipy.stats import boxcox
data = pd.read_csv(r'C:\python\employees.csv')
#print(data)

# check for missing values
if data.isnull().values.any():
    print("There are missing values in the DataFrame.")
else:
    print("No")
    
# replace missing values with mean or median
    for col in data.columns:
        if data[col].isnull().values.any():
            if data[col].dtype != 'object':
                median = data[col].median()
                data[col].fillna(median, inplace=True)
            else:
                mode = data[col].mode().iloc[0]
                data[col].fillna(mode, inplace=True)
print(data)

# check for inconsistencies
for col in data.columns:
    if data[col].dtype == 'object':
        unique_vals = data[col].unique()
        if len(unique_vals) > 2:
            print(f"Inconsistent values found in {col}: {unique_vals}")

# replace inconsistent values with mode
mode = data[col].mode().iloc[0]
data[col].replace(unique_vals, mode, inplace=True)

# detect and deal with outliers in numeric variables
for col in data.select_dtypes(include=[np.number]).columns:
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)][col]
    if not outliers.empty:
        print(f"Outliers found in {col}: {outliers.values}")

# replace outliers with the median
median = data[col].median()
data.loc[(data[col] < lower_bound) | (data[col] > upper_bound), col] = median

# apply Box-Cox transformation on income variable to reduce skewness
transformed_income, lambda_value = boxcox(data['income'])
data['income_transformed'] = transformed_income


# print the cleaned DataFrame
print(data)




