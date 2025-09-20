from sklearn.datasets import load_wine
load_data=load_wine()

import pandas as pd

load_df=pd.DataFrame(load_data.data,columns=load_data.feature_names)
print(load_df)

load_df['target']=load_data.target

x=load_df[load_data.feature_names].copy()
y=load_df['target'].values.reshape(-1,1)

print(x)

seed=44

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=.4,
                                               random_state=seed)

from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(x_train,y_train)
y_pred=regression.predict(x_test)

print(y_pred)

x_corr=x.corr()

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()

g=sns.heatmap(x_corr,annot=True,center=0,cmap="coolwarm")
g.figure.suptitle("Heat Map")
plt.show()