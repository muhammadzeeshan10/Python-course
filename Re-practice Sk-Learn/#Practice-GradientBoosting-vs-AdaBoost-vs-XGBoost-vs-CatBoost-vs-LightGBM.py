from sklearn.datasets import make_regression
x,y=make_regression(n_samples=100,
                    n_features=5,
                    n_informative=10,
                    n_targets=1,
                    random_state=42)
print(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=0.2)

from sklearn.ensemble import GradientBoostingRegressor
gbr=GradientBoostingRegressor()
gbr.fit(x_train,y_train)
pred1=gbr.predict(x_test)

from sklearn.metrics import r2_score
print("R2 :",r2_score(y_test,pred1))


from xgboost import XGBRegressor
xgb=XGBRegressor()
xgb.fit(x_train,y_train)
pred2=xgb.predict(x_test)
print("XGB",r2_score(y_test,pred2))

from sklearn.ensemble import AdaBoostRegressor
abr=AdaBoostRegressor()
abr.fit(x_train,y_train)
pred3=abr.predict(x_test)

print("AdaBoostRegressor",r2_score(y_test,pred3))

from catboost import CatBoostRegressor
cat=CatBoostRegressor()

cat.fit(x_train,y_train)
pred4=cat.predict(x_test)
print("CatBoostRegression",r2_score(y_test,pred4))


import lightgbm as lgb
from lightgbm import LGBMRegressor
lgb=LGBMRegressor()

lgb.fit(x_train,y_train)
pred5=lgb.predict(x_test)
print("lightGBM",r2_score(y_test,pred5))

import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x=y_test,y=pred1)
sns.lineplot(x=y_test,y=pred2)
sns.lineplot(x=y_test,y=pred3)
sns.lineplot(x=y_test,y=pred4)
sns.lineplot(x=y_test,y=pred5)
plt.show()