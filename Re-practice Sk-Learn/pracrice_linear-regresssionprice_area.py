import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('D:\AI\SK Learn\Week6_#Practice\petrol_consumption.csv')
print(df)
print(df.columns)
print(df.describe)
print(df.info())
print(df.head())
print(df.tail())

x=df[['Population_Driver_licence(%)']]
y=df['Petrol_Consumption']

print(x.values)
print(x.values.shape)

df.plot.scatter(x='Population_Driver_licence(%)',y='Petrol_Consumption')
plt.show()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               train_size=.2,
                                               random_state=42)

from sklearn.linear_model import LinearRegression
Linear_Regression=LinearRegression()
Linear_Regression.fit(x_train,y_train)
Linear_Regression_pred=Linear_Regression.predict(x_test)

print(Linear_Regression_pred)

df_pred=pd.DataFrame({'Actual':y_test.squeeze(),'Predictice':Linear_Regression_pred})
print(df_pred)



from sklearn.metrics import mean_absolute_error
import numpy as np
mae=mean_absolute_error(y_test,Linear_Regression_pred)

print(f'Mean Absolute error,{mae:.2f}')