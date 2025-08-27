import pandas as pd
from sklearn.datasets import fetch_california_housing
california=fetch_california_housing()
df=pd.DataFrame(california.data,columns=california.feature_names)
print(df.columns)
print(df.head())

df['MEDV']=california.target

x=df.drop('MEDV',axis=1)
y=df['MEDV']


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=.2,
                                               random_state=42)


from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor(n_estimators=100,random_state=42)
rfr.fit(x_train,y_train)
pred=rfr.predict(x_test)


from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
print("Mean Square Error:",mean_squared_error(y_test,pred))
print("R2 -Score:",r2_score(y_test,pred))
print("Mean Absolute Error:",mean_absolute_error(y_test,pred))