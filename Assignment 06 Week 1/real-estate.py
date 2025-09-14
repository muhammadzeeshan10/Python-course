import pandas as pd

df=pd.read_csv('D:\AI\Assignment 06 Week 1\RealEstate-USA.csv',delimiter=',',skiprows=0)

print(df.head())
print(df.shape)
print(df.describe())
print(df.dtypes)

accessed_value=df['price']
print(accessed_value)

print(df.head())
print(df.dtypes)

import matplotlib.pyplot as plt
import seaborn as sns
# sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})
sns.set_theme(style='ticks',rc={'axes.facecolor':'red','grid.color':'white'})
g=sns.lineplot(x='city',
             y='price',
             data=df)

g.figure.suptitle("Line-Plot")
plt.show()
sns.set_theme(style='whitegrid',rc={'axes.facecolor':'gray','grid.color':'orange'})
g=sns.catplot(x='city',
                y='price',data=df)
g.figure.suptitle("Cat-plot")
plt.show()

g=sns.kdeplot(x='zip_code',
            y='price',
            data=df)
g.figure.suptitle("KDE-plot")
plt.show()
sns.set_theme(style='white',rc={'axes.facecolor':'orange','grid.color':'purple'})
g=sns.scatterplot(x='zip_code',
                y='price',
                data=df)
g.figure.suptitle("Scatter-plot")
plt.show()

g=sns.barplot(x='zip_code',y='price',
            data=df)
g.figure.suptitle("Bar-plot")
plt.show()

sns.heatmap(df.pivot_table(values='price', index='zip_code', aggfunc='mean'), annot=True, fmt=".0f", cmap="viridis")
plt.show()

sns.lineplot(x='bed',y='price',data=df)
plt.show()

