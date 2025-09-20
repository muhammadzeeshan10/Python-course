import pandas as pd
df=pd.read_csv('D:\AI\Assignment 01 Week 6\mtcars.csv')
print(df)
df.columns=df.columns.str.strip().str.replace(" ","_")
print(df.head())
print(df.info())
print(df.describe())
print(df.dtypes)

x=df[['cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']]
y=df['mpg']

print(x)
seed=35
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               train_size=.6,
                                               random_state=seed)

print(x_train)

from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(x_train,y_train)
y_pred=regression.predict(x_test)

print(y_pred)

x_coor=df[['cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']]
x_cor=x_coor.corr()

import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(x_cor,annot=True,cmap="coolwarm",center=0)
plt.show()

