import pandas as pd
import numpy as np
# Load Dataset
data = pd.read_csv('Turkey_Home_Price_2024.csv')
data = data.dropna()

data = data[data['Fiyat'] < data['Fiyat'].quantile(0.95)]


x = data[['Net_Metrekare', 'Brüt_Metrekare', 'Oda_Sayısı']]
y = data['Fiyat']


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=25
)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#  Model
from sklearn.linear_model import LinearRegression,LogisticRegression
model = LinearRegression()
model2=LogisticRegression()
model2.fit(x_train,y_train)
model.fit(x_train, y_train)

# Predictions
y_pred = model.predict(x_test)
y_pred2=model2.predict(x_test)


from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

r2 = r2_score(y_test, y_pred)
r22 = r2_score(y_test, y_pred2)
mae = mean_absolute_error(y_test, y_pred)
mae2 = mean_absolute_error(y_test, y_pred2)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
rmse2 = np.sqrt(mean_squared_error(y_test, y_pred2))

print("R2 Score:", r2)
print("R2 Score:", r22)
print("Mean Absolute Error:", mae)
print("Mean Absolute Error:", mae2)
print("RMSE:", rmse)
print("RMSE:", rmse2)



import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(7,5))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices (Linear Regression)")
plt.show()

plt.figure(figsize=(8,6))

corr_matrix = data[['Net_Metrekare', 'Brüt_Metrekare', 'Oda_Sayısı', 'Fiyat']].corr()

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Heatmap of House Price Features")
plt.show()

# Here we Can Apply 2 Algorithm 
# 1 Linear Algorithm
# 2 Logistic ALgorithm

# Here check the Accuracy of Both Algo we used r2 Score ,mae and mse throgh...