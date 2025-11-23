import pandas as pd

df=pd.read_csv('data.csv',parse_dates=['Date'],index_col='Date')
print(df.head())

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
scaler_data=scaler.fit_transform(df.values)

import numpy as np
def dataset(data,time_step=1):
    x=[]
    y=[]
    for i in range(len(data) - time_step-1):
        x.append(data[i:(i + time_step),0])
        y.append(data[i+time_step,0])
    return np.array(x),np.array(y)

time_step=100
x,y=dataset(scaler_data,time_step)
x=x.reshape(x.shape[0],x.shape[1],1)

from tensorflow.keras.models import Sequential
from keras.layers import GRU,Dense
model=Sequential()

model.add(GRU(units=50, return_sequences=True,input_shape=(x.shape[1],1)))
model.add(GRU(units=50))
model.add(Dense(units=1))

from keras.metrics import Precision,Recall
METRICS=metrics=['accuracy',Precision(name='Precision'),Recall(name='recall')]

from tensorflow.keras.optimizers import Adam
model.compile(optimizer=Adam(learning_rate=0.001),loss='mean_squared_error',metrics=METRICS)

model.fit(x,y,epochs=10,batch_size=32)

input_sequence = scaler_data[-time_step:].reshape(1, time_step, 1)
predicted_values = model.predict(input_sequence)

predicted_values = scaler.inverse_transform(predicted_values)
print(f"The predicted temperature for the next day is: {predicted_values[0][0]:.2f}°C")
