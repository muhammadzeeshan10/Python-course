import pandas as pd

df=pd.read_csv('monthly_milk_production.csv')
print(df)

df['Date']=pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
production=df['Production'].astype(float).values.reshape(-1,1)

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler(feature_range=(0,1))
scaler_data=scaler.fit_transform(production)

window=12
x=[]
y=[]

target_date=df.index[window:]

for i in range(window,len(scaler_data)):
    x.append(scaler_data[i-window:i,0])
    y.append(scaler_data[i,0])

import numpy as np
x=np.array(x)
y=np.array(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test,date_train,date_test=train_test_split(x,
                                                                    y,
                                                                    target_date,
                                                                    test_size=.6,
                                                                    random_state=25)


x_train=x_train.reshape((x_train.shape[0],x_train.shape[1],1))
x_test=x_test.reshape((x_test.shape[0],x_test.shape[1],1))


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense,Dropout

model=Sequential()
model.add(LSTM(units=128,return_sequences=True,input_shape=(x_train.shape[1],1)))
model.add(Dropout(0.2))
model.add(LSTM(units=128))
model.add(Dropout(0.2))
model.add(Dense(1))


from keras.metrics import Precision,Recall
METRICS = ['accuracy', 
                   Precision(name='precision'),
                   Recall(name='recall')]

model.compile(optimizer='adam', loss='mean_squared_error' , 
               metrics = METRICS)

history = model.fit(x_train, y_train, epochs=100, batch_size=32, validation_split=0.1)

predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions).flatten()
y_test = scaler.inverse_transform(y_test.reshape(-1,1)).flatten()

rmse = np.sqrt(np.mean((y_test - predictions)**2))
print(f'RMSE: {rmse:.2f}')
