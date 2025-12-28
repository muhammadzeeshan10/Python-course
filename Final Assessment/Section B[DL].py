import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, GRU, Dense
import matplotlib.pyplot as plt


data = pd.read_csv(
    'USA-Redfin-Monthly-Housing-Market-Data.csv',
    encoding='utf-16',
    sep='\t'
)

# Strip column names to remove extra spaces
data.columns = [c.strip() for c in data.columns]


data['Median Sale Price'] = data['Median Sale Price'].str.replace('$','', regex=False)
data['Median Sale Price'] = data['Median Sale Price'].str.replace('K','', regex=False)
data['Median Sale Price'] = data['Median Sale Price'].astype(float) * 1000


data['Month of Period End'] = pd.to_datetime(data['Month of Period End'])
data = data.sort_values('Month of Period End')


target = data['Median Sale Price'].values.reshape(-1,1)


scaler = MinMaxScaler()
scaled_target = scaler.fit_transform(target)

def create_sequences(data, time_steps=12):
    X, y = [], []
    for i in range(len(data)-time_steps):
        X.append(data[i:i+time_steps])
        y.append(data[i+time_steps])
    return np.array(X), np.array(y)

time_steps = 12  
X, y = create_sequences(scaled_target, time_steps)


X = X.reshape(X.shape[0], X.shape[1], 1)


split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]


model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    GRU(32),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.summary()


history = model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=16,
    validation_split=0.1,
    verbose=1
)


# Predictions

y_pred = model.predict(X_test)

# Inverse scaling to original prices
y_test_actual = scaler.inverse_transform(y_test)
y_pred_actual = scaler.inverse_transform(y_pred)


# Evaluate Model

mae = mean_absolute_error(y_test_actual, y_pred_actual)
mse = mean_squared_error(y_test_actual, y_pred_actual)
rmse = np.sqrt(mse)

print(f"MAE: {mae}")
print(f"RMSE: {rmse}")


# Plot Results

plt.figure(figsize=(12,6))
plt.plot(data['Month of Period End'][split+time_steps:], y_test_actual, label='Actual Prices')
plt.plot(data['Month of Period End'][split+time_steps:], y_pred_actual, label='Predicted Prices')
plt.title('Median House Price Prediction - LSTM + GRU')
plt.xlabel('Month')
plt.ylabel('Median Sale Price ($)')
plt.legend()
plt.show()

# -------- Future (Next Month) Prediction --------

# Last 12 months data
last_sequence = scaled_target[-time_steps:]

last_sequence = last_sequence.reshape(1, time_steps, 1)
future_pred_scaled = model.predict(last_sequence)


future_pred = scaler.inverse_transform(future_pred_scaled)
print("Predicted Median Sale Price for NEXT Month:")
print(f"${future_pred[0][0]:,.0f}")
