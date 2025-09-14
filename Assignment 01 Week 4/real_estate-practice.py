import pandas as pd
# Task 01
df=pd.read_csv('D:\AI\Assignment 01 Week 4\RealEstate-USA.csv')
# Task 02
print(df.to_string)
print(df.shape)
print(df.info())
print(df.describe)
# Task 03
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
sns.lineplot(x='city',
             y='price',data=df)
plt.show()

