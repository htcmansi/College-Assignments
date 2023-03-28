import pandas as pd
import numpy as np
from sklearn import preprocessing
df=pd.DataFrame({'ID':[1,2,3,3],
                 'Name': ['Mansi','Vedant','Tanuja','Abhi'],
                 'age':[19,20,20,22],
                 'marks':[90,'N',56,67]})
print(df)

#calculate avg
c=avg=0
for num in df['marks']:
    if str(num).isnumeric():
        c+=1
        avg +=num
avg /=c

#replacing missing values
df=df.replace(to_replace="N",value=avg)
print(df)
 
data=np.array([56,45,35,45])
#Normalization
Norm_arr=preprocessing.normalize([data])
print(Norm_arr)

#filtering data 
#top scoring student
df=df[df['marks']>=50]
print(df)

#remove the column
df=df.drop(['age'],axis=1)
print(df)

#add row
df.loc[len(df.index)]=[4,'Shweta',70]
print(df)

#merging data frames
details=pd.DataFrame({'ID':[1,2,3,],
                      'Branch':['CS','CS','IT'],
                      'Mobile':['8010150544','5263458654','4568723658']})
print(details)
print(pd.merge(df,details, on='ID'))

#remove duplicates entries
non_duplicates=df[~df.duplicated('ID')]
print(non_duplicates)
