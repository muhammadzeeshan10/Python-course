# Question No 01
import pandas as pd
data={'x':[40,67,42,77,32,13],'y':[63,42,12,13,64,11],'z':[16,18,19,21,31,53]}
df=pd.DataFrame(data)
print(df.head(2))


# Question No 02

# Sample DataFrame:


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, 9, 20, 14.5, 8, 19,23,56],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2=pd.DataFrame(exam_data,index=labels)
print(df2)

# Task 01
print(df2.info())

# Task 02
# Select frist 3 Rows
row=df2['qualify'].iloc[0:3]
print(row)

# Task 03
multiple=df2[['name','score']]
print(multiple)

# Task 04
multiplerow=df2[['name','score']].iloc[[1,3,5,6]]
print(multiplerow)

# Task 05
attempt=[df2['attempts']>2]
print(attempt)

# Task 06
print(df2.shape)

# task 07
score=[(df2['score']>15) & (df2['score']<=20)]
print(score)

# Task 08
print(df2.shape)
df2=df2.drop('score',axis=1)
print(df2.shape)
