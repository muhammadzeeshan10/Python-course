import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('D:\AI\SK Learn\Week6_#Practice\diabetes.csv')
print(df.columns)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())


x=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
y=df['Outcome']

print(x)
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               train_size=.3,
                                               random_state=14)

from sklearn.linear_model import LogisticRegression
regression=LogisticRegression(max_iter=200)
regression.fit(x_train,y_train)
regression_pred=regression.predict(x_test)

from sklearn import metrics
cnf=metrics.confusion_matrix(y_test,regression_pred)
print(cnf)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

classes_names=[0,1]
mark=np.arange(len(classes_names))

plt.xticks(mark,classes_names)
plt.yticks(mark,classes_names)

sns.heatmap(pd.DataFrame(cnf),annot=True, cmap="YlGnBu" ,fmt='g')
plt.show()

from sklearn.metrics import classification_report
target_names = ['without diabetes', 'with diabetes']
print(classification_report(y_test,regression_pred,target_names=target_names))


