import pandas as pd
# Task 01
df=pd.read_csv('D:\AI\Assignment 04 Week 3\macro_monthly.csv',index_col=None)

# Task 02
print(df.shape)
print(df.info())
print(df.describe)
print(df.columns)

# Task 03
print(df.to_string())

# Task 04
print(df.head(4))

# Task 05
print(df.tail(4))

# Task 06
indsutry=df['Industrial_Production']
print(indsutry)

# Task 07
multiple=df[['Industrial_Production','Year']]
print(multiple)

# Task 08
row=df['Industrial_Production'].loc[2]
print(row)

# Task 09
row1=df['Industrial_Production'].loc[[3,5,7]]
print(row1)

# Task 10
slicing=df['Industrial_Production'].loc[5:15]
print(slicing)

# task 11
year=df['Year'].loc[9]
print(year)

# Task 12
multiple_col=df.loc[:,'Industrial_Production':'Retail_Sales']
print(multiple_col)

# Task 13
condition=df.loc[df['Industrial_Production']<=0.5]
print(condition)

# Task 14
row2=df['Industrial_Production'].iloc[10:23]
print(row2)

