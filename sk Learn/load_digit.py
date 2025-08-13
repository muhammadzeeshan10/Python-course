import pandas as pd
from sklearn.datasets import load_digits

load_date=load_digits()

load_date_as_frame=load_digits(as_frame=True)
print(load_date_as_frame)

load_df=pd.DataFrame(load_date.data,columns=load_date.feature_names)
print(load_df)

print(load_df.shape)
print(load_df.head())
print(load_df.tail())
print(load_df.describe)
print(load_df.info())

load_df["target"]=load_date.target

x=load_df[load_date.feature_names].copy()
y=load_df["target"].copy()
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
svc=SVC()
svc.fit(x_train_scaler,y_train)

svc_pred=svc.predict(x_test_scaler)

from sklearn.metrics import classification_report
print("svc")
print(classification_report(y_test,svc_pred))