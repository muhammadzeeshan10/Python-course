import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(df.head(1))
print(df.columns)
print(df.info())
print(df.describe())

x=df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
y=df['Survived']

x['Sex'] = x['Sex'].map({'female': 0, 'male': 1})
x['Age'] = x['Age'].fillna(x['Age'].median())

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=.2,
                                               random_state=42)
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=100,random_state=42)
rfc.fit(x_train,y_train)
pred1=rfc.predict(x_test)

from sklearn.metrics import accuracy_score,classification_report
print("Classification Report is:",classification_report(y_test,pred1))
print("Accuracy Score",accuracy_score(y_test,pred1))
