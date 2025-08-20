import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('D:\AI\SK Learn\Week7_#Practice\diabetes.csv')

print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())


x=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
y=df['Outcome']

print(x.values)
print(x.values.shape)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               train_size=.7,
                                               random_state=14)

from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()

dtc.fit(x_train,y_train)
dtc_pred=dtc.predict(x_test)

from sklearn import metrics
print("Check Accuracy Scores:",metrics.accuracy_score(y_test,dtc_pred))


from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot=StringIO()
export_graphviz(dtc,out_file=dot,filled=True,rounded=True,special_characters=True,class_names=['0','1'],feature_names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
graph=pydotplus.graph_from_dot_data(dot.getvalue())
graph.write_png('DeibetesP1.png')
Image(graph.create_png())







dtc=DecisionTreeClassifier(criterion="entropy",max_depth=3)

dtc =dtc.fit(x_train,y_train)
pred_dtc=dtc.predict(x_test)

print("Check accuracy",metrics.accuracy_score(y_test,pred_dtc))


from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot=StringIO()
export_graphviz(dtc,out_file=dot,filled=True,rounded=True,special_characters=True,class_names=['0','1'],feature_names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
graph=pydotplus.graph_from_dot_data(dot.getvalue())
graph.write_png('DeibetesP2.png')
Image(graph.create_png())
