import pandas as pd 
data = pd.read_csv(r'C:\python\Salary_Data.csv') 
print(data) 

#mean of salary column
print("Mean of the salary column is" ,data['Salary'].mean())

#median of salary column
print("Median of salary column is" ,data['Salary'].median()) 
print("Maximum value in Salary is" ,data['Salary'].max())
 
#minimum value present in salary column
print("Minimum value in Salary is" ,data['Salary'].min())

#maximum value in dataset
print("Standard deviation of Salary column is" ,data['Salary'].std())

#percentile
print("percentile value in Salary is" ,data['Salary'].quantile(0.5))

#groupby the salary column
gk = data.groupby('Salary') 
print(gk.first()) 
