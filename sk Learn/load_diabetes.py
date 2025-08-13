import pandas as pd
from sklearn.datasets import load_diabetes
load_data=load_diabetes()

load_data_as_frame=load_diabetes(as_frame=True)
print(load_data_as_frame)

load_df=pd.DataFrame(load_data.data,columns=load_data.feature_names)

print(load_df)
print(load_df.shape)
print(load_df.describe())
# print(load_df.info())
print(load_df.head())
print(load_df.tail())

load_df["target"]=load_data.target

x=load_df[load_data.feature_names].copy()
# y=load_df["target"].copy
y=load_df['target'].values.reshape(-1,1)

print(x)
print(y)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(x)
x_scaler=scaler.transform(x.values)
print(x_scaler)

from sklearn.model_selection import train_test_split

x_train_scaler,x_test_scaler,y_train,y_test=train_test_split(x_scaler,
                                                             y,
                                                             train_size=.7,
                                                             random_state=25)

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
Logistic_Regression=LogisticRegression()
Decision_TreeClassifier=DecisionTreeClassifier()
svc=SVC()
svc.fit(x_train_scaler,y_train)
Logistic_Regression.fit(x_train_scaler,y_train)
Decision_TreeClassifier.fit(x_train_scaler,y_train)



LogisticRegression_pred=Logistic_Regression.predict(x_test_scaler)
DecisionTreeClassifier_pred=Decision_TreeClassifier.predict(x_test_scaler)
svc_pred=svc.predict(x_test_scaler)

from sklearn.metrics import classification_report
print("svc")
print(classification_report(y_test,svc_pred))
print(classification_report(y_test,LogisticRegression_pred))
print(classification_report(y_test,DecisionTreeClassifier_pred))