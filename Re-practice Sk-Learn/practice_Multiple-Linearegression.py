import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('D:\AI\SK Learn\Week6_#Practice\petrol_consumption.csv')

print(df)
print(df.describe)
print(df.info())
print(df.head())
print(df.tail())

import seaborn as sns
variable=['Petrol_tax','Average_income','Paved_Highways','Population_Driver_licence(%)','Petrol_Consumption']
for var in variable:
    plt.figure
    sns.regplot(x=var,y='Petrol_Consumption',data=df)
    g=plt.suptitle(var)
    plt.show()

plt.figure()
coorelation=df.corr()
g=sns.heatmap(coorelation,annot=True)
plt.suptitle('Heat-plot of Coorelation')
plt.show()

x=df[['Petrol_tax','Average_income','Paved_Highways','Population_Driver_licence(%)']]
y=df['Petrol_Consumption']


print(x.values)
print(x.values.shape)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                              y,
                                              train_size=.7,
                                              random_state=25)

from sklearn.linear_model import LinearRegression

regression=LinearRegression()

regression.fit(x_train,y_train)
# regression_pred=regression.predict(x_test)

regression_pred=regression.predict(x_test)
print("Regression.intercept",regression.intercept_)
print("regression.coef_",regression.coef_)

result=pd.DataFrame({'Actual':y_test,'Prediction':regression_pred})
print(result)


from sklearn.metrics import mean_absolute_error
mae=mean_absolute_error(y_test,regression_pred)
print(mae)