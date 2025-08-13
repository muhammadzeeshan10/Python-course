import pandas as pd
from sklearn.datasets import load_iris

load_data=load_iris()

load_data_as_frame=load_iris(as_frame=True)
print(load_data_as_frame)

load_df=pd.DataFrame(load_data.data,columns=load_data.feature_names)
print(load_df)

# Display Info
print(load_df.info())
# print Description
print(load_df.describe)
# Head
print(load_df.head())
# tail
print(load_df.tail())



x=load_df[load_data.feature_names].copy()
load_df["target"]=load_data.target
y=load_df['target'].values.reshape(-1,1)
# y=load_df['target'].copy()


from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(x)
x_scaler=scaler.transform(x.values)
print(x_scaler)

from sklearn.model_selection import train_test_split
x_train_scaler,x_test_train,y_train,y_test=train_test_split(x_scaler,
                                                            y,
                                                            train_size=.7,
                                                            random_state=25)

from sklearn.svm import SVC
svc=SVC()

svc.fit(x_train_scaler,y_train)
svc_pred=svc.predict(x_test_train)

from sklearn.metrics import classification_report
print("svc")
print(classification_report(y_test,svc_pred))