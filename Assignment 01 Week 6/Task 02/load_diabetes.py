from sklearn.datasets import load_diabetes
diabetes=load_diabetes()

load_data=load_diabetes(as_frame=True)
print(load_data)
import pandas as pd
load_df=pd.DataFrame(load_data.data,columns=load_data.feature_names)
print(load_df)

print(load_df.columns)
print(load_df.head())

load_df["target"]=load_data.target

x=load_df[load_data.feature_names].copy()
y=load_df['target'].values.reshape(-1,1)

print(x)
print(y)

seed=54
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=.4,
                                               random_state=seed)

print(x_train)

from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(x_train,y_train)
y_pred=regression.predict(x_test)
print(y_pred)

x_coor=x.corr()
print(x_coor)

import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(x_coor,center=0,cmap="coolwarm",annot=True)
plt.show()

