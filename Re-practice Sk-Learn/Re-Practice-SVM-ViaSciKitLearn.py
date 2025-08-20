import pandas as pd
import matplotlib.pyplot as plt

url="https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt"
use_cols=["variance", "skewness", "curtosis", "entropy", "class"]

df=pd.read_csv(url,names=use_cols,delimiter=',')

print(df.head())
print(df.shape)
print(df.tail())
print(df.info())
print(df.describe())
print(df.dtypes)


print(df['class'].unique())
print(df.shape)

print("Check how many time unique value apear:",df["class"].value_counts())
print(df["class"].value_counts(normalize=True))

df["class"].plot.hist();
plt.show()

print(df.describe().T)

import matplotlib.pyplot as plt

for col in df.columns[:-1]:
    plt.title(col)
    df[col].plot.hist()
    plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df,hue='class');
plt.show()


x=df.drop('class',axis=1)
y=df['class']

print(y.values.shape)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               train_size=.7,
                                               random_state=14)

from sklearn.svm import SVC
svc=SVC(kernel='linear')

svc.fit(x_train,y_train)
svc_pred=svc.predict(x_test)

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,svc_pred))

cm=confusion_matrix(y_test,svc_pred)
sns.heatmap(cm,annot=True,fmt='d')
plt.show()