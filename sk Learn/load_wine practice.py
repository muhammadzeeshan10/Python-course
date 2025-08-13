import pandas as pd
from sklearn.datasets import load_wine

wine_data=load_wine()

wine_data_as_frame=load_wine(as_frame=True)
print(wine_data_as_frame)

wine_df=pd.DataFrame(wine_data.data,columns=wine_data.feature_names)
print(wine_df)

wine_df["target"]=wine_data.target

print(wine_df.head())
print(wine_df.tail())

x=wine_df[wine_data.feature_names].copy()
y=wine_df["target"].copy()

print(x)
print(y)
# tarin X values and divide into diff pieces
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
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

Logistic_Regression=LogisticRegression()
svc=SVC()
Decision_Tree_Classifier=DecisionTreeClassifier()

Logistic_Regression.fit(x_train_scaler,y_train)
svc.fit(x_train_scaler,y_train)
Decision_Tree_Classifier.fit(x_train_scaler,y_train)

LogisticRegression_pred=LogisticRegression_pred=Logistic_Regression.predict(x_test_scaler)
svc_pred=svc_pred=svc.predict(x_test_scaler)
DecisionTreeClassifier_pred=Decision_Tree_Classifier.predict(x_test_scaler)

from sklearn.metrics import classification_report
print("LogisticRegression")
print(classification_report(y_test,LogisticRegression_pred))