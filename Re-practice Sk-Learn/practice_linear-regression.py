import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('D:\AI\SK Learn\Week6_#Practice\student_scores.csv')

print(df)
print(df.shape)
print(df.describe)
print(df.info())

print(df.head())
print(df.tail())

hours=df['Hours']
scores=df['Scores']

print(hours)
print(scores)

x=df['Hours'].values.reshape(-1,1)
y=df['Scores'].values.reshape(-1,1)

print("Display")
print(x)
print(y)


print(df['Hours'].values)
# Describe Specific values
print(df['Hours'].values.shape)

# Descibe All Row and Column
print(x.shape)

from sklearn.model_selection import train_test_split

x_tain,x_test,y_train,y_test=train_test_split(x,
                                              y,
                                              test_size=.2,
                                               random_state=42)

print(x_tain)
print(y_train)

# Used Linear Regression Model

from sklearn.linear_model import LinearRegression
regression=LinearRegression()

regression.fit(x_tain,y_train)

print(regression.intercept_)
print(regression.coef_)

# Create Function

def cal(intercept,hours,slope):
    return slope*intercept+hours
score=cal(regression.intercept_,regression.coef_,9.5)
print(score)

score=regression.predict([[9.5]])
print(score)

y_pred=regression.predict(x_test)
print(y_pred)

df_pred=pd.DataFrame({'Actual':y_test.squeeze(),'prediction':y_pred.squeeze()})
print(df_pred)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np
mae=mean_squared_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
rmse=np.sqrt(mse)

# Check error like how points demage data***
print(f'mean_absolute_error,{mae:.2f}')
print(f'mean Squared Error,{mse:.2f}')
print(f'r2-Square,{r2:.2f}')
print(f'rmse,{rmse:.2f}')