import pandas as pd
# /01
df=pd.read_csv('D:\\AI\Assignment 01 Week 6\\number-of-registered-medical-and-dental-doctors-by-gender-in-pakistan (1).csv')
# /02


df['Female Doctors'] = df['Female Doctors'].replace({',': ''}, regex=True).astype(float)
df['Female Dentists'] = df['Female Dentists'].replace({',': ''}, regex=True).astype(float)
print(df)
print(df.shape)
print(df.describe)
print(df.info())
print(df.columns)

# /03
x=df[['Female Doctors']]
y=df['Female Dentists']

seed=42
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               train_size=.5,
                                               random_state=seed)

print(x_train)

from sklearn.linear_model import LinearRegression
regressors=LinearRegression()
regressors.fit(x_train,y_train)
y_pred=regressors.predict(x_test)

print("COEF",regressors.coef_)
print("Intercept",regressors.intercept_)

regression=regressors.coef_
cooeffiect=regressors.intercept_

def hadi(slope,intercept,female_doctors):
    return slope*female_doctors+intercept

print("Predicted Dentists for 5000 Doctors:", hadi(5000, regressors.coef_[0], regressors.intercept_))
print("Predicted Dentists for 10000 Doctors:", hadi(10000, regressors.coef_[0], regressors.intercept_))




from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
score=r2_score(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
mqe=mean_squared_error(y_test,y_pred)
print("Mean Absolute Error:",mae)
print("Mean Square Error:",mqe)
print("R-2 Score:",score)
