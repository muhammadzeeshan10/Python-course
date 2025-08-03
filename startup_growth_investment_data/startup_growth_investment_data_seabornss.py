import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('C:\\Users\\Zeeshan PC\\Documents\\GitHub\\Python-course\\startup_growth_investment_data\\startup_growth_investment_data.csv',delimiter=",",parse_dates=[4],date_format={'date_time':'%d-%m-%y'})
print(data.dtypes)
print(data.info())
print(data.describe())

# print first 40 lines
first40=data.head(40)
print(first40)
first20=data.head(20)
print(first20)

sns.set_style('whitegrid')

sns.displot(data=first20,x='Number of Investors',y='Growth Rate (%)',bins=20)
plt.title("displot")
plt.show()

sns.kdeplot(data=first40,x='Growth Rate (%)')
plt.title("kdeplot")
plt.show()

sns.histplot(data=first20,x='Growth Rate (%)',y='C',hue='C')
plt.title("histplot")
plt.show()

sns.scatterplot(data=first20,x='Growth Rate (%)',y='C',hue='C')
plt.title("scatterplot")
plt.show()

sns.catplot(data=first40,x='Valuation (USD)',kind='bar')
plt.title("catplot")
plt.show()

sns.barplot(data=first20,x='Startup Name',y='C')
plt.title("Barplot")
plt.show()