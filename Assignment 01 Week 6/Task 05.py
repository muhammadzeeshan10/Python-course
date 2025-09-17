import pandas as pd
df=pd.read_csv('D:\\AI\\Assignment 01 Week 6\\housing(1).csv')
print(df)
print(df.shape)
print(df.describe)
print(df.info())
print(df.columns)
print(df.head())
df = df.fillna(df.mean(numeric_only=True))


x=df[['longitude','latitude','housing_median_age','total_rooms','total_bedrooms']]
y=df['population']

print(x)

from sklearn.model_selection import train_test_split

seed=38
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=.5,
                                               random_state=seed)

print(x_train)
print(x_train.head())

from sklearn.linear_model import LinearRegression
regression=LinearRegression()

regression.fit(x_train,y_train)
y_pred=regression.predict(x_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

print(f"Mean Absolute Error:{mae}")
print(f"Mean Squared Error{mse}")
print(f"R-2 Score,{r2}")

x_coorr=df[['longitude','latitude','housing_median_age','total_rooms','total_bedrooms']]
x_corr=x_coorr.corr()
print(x_corr)

import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(x_corr,annot=True,cmap="coolwarm",center=0)
plt.show()