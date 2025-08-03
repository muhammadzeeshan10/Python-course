import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('C:\\Users\Zeeshan PC\Documents\GitHub\Python-course\macro_monthly\macro_monthly.csv',delimiter=",",parse_dates=[4],date_format={'date_time':'%d-%m-%y'})
print(data.dtypes)
print(data.info())
print(data.describe())

# print first 40 lines
first40=data.head(40)
print(first40)
first20=data.head(20)
print(first20)

sns.set_style('whitegrid')

sns.displot(data=first20,x='Year')
plt.title("Displot")
plt.show()

sns.kdeplot(data=first20,x='Month')
plt.title("kdeplot")
plt.show()

sns.histplot(data=first20,x='Month',y='Year',hue='Year')
plt.title("histplot")
plt.show()

sns.scatterplot(data=first20,x='Month',y='Year',hue='Year')
plt.title("scatterplot")
plt.show()

sns.catplot(data=first40,x='Month',kind='bar')
plt.title("catplot")
plt.show()

sns.barplot(data=first20,x='Month',y='Year')
plt.title("Barplot")
plt.show()