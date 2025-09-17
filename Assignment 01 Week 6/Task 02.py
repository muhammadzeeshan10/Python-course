import pandas as pd
df=pd.read_csv('D:\AI\Assignment 01 Week 6\zameencom-property-data-By-Kaggle-Short.csv',delimiter=';')
print(df)
print(df.dtypes)
print(df.describe)
print(df.info())
print(df.columns)
print(df.shape)


from sklearn.model_selection import train_test_split





x=df[['bedrooms']]
y=df['price']



print(x)
print(y)


x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=.25,
                                               random_state=44)
print(x_train)
from sklearn.linear_model import LinearRegression
LinearRegressions=LinearRegression()

LinearRegressions.fit(x_train,y_train)
y_pred=LinearRegressions.predict(x_test)
intercept=LinearRegressions.intercept_
slope=LinearRegressions.coef_[0]

print("Intercept",LinearRegressions.intercept_)
print("Coorelation",LinearRegressions.coef_)

def predict_price(bedrooms,intercept,slope):
    return slope*bedrooms+intercept

print("Price for 2 bedrooms:", predict_price(2, intercept, slope))
print("Price for 3 bedrooms:", predict_price(3, intercept, slope))
print("Price for 5 bedrooms:", predict_price(5, intercept, slope))




from sklearn.metrics import mean_absolute_error,r2_score
mea=mean_absolute_error(y_pred,y_test)
r2_scores=r2_score(y_pred,y_test)

print("Mean Absolute Error:",mea)
print("R-2 Score ",r2_scores)