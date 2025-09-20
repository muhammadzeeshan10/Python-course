import pandas as pd
# Task 01

df=pd.read_csv('D:\AI\Assignment 01 Week 6\Real_Estate_Sales_2001-2022_GL-Short (1).csv')
print(df)
print(df.shape)
print(df.info())
print(df.describe)
print(df.dtypes)

df.columns = df.columns.str.strip().str.replace(" ", "_")
x=df[['Assessed_Value']]
y=df['Sale_Amount']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=.2,
                                               random_state=44)

from sklearn.linear_model import LinearRegression
LinearRegressions=LinearRegression()
LinearRegressions.fit(x_train,y_train)
y_pred=LinearRegressions.predict(x_test)


print("Intercept",LinearRegressions.intercept_)
print("COorelation:",LinearRegressions.coef_)

def calc(slope, intercept, hours):
    return slope*hours+intercept

score = calc(LinearRegressions.coef_, LinearRegressions.intercept_, 9.5)
print(score) # [[94.80663482]]


score = LinearRegressions.predict([[9.5]])
print(score) # 94.80663482


from sklearn.metrics import mean_absolute_error,r2_score
mae=mean_absolute_error(y_pred,y_test)
print("Mean Absolute Error:",mae)
scores=r2_score(y_test,y_pred)
print("R-2 Score:",scores)


