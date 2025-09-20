import pandas as pd
df=pd.read_csv('D:\\AI\\Assignment 01 Week 6\\50_Startups (1).csv')
print(df)
df.columns = df.columns.str.strip().str.replace(" ", "_")
print(df.shape)
print(df.dtypes)
print(df.info())
print(df.describe)
print(df.columns)

xx=df[['R&D_Spend','Administration','Marketing_Spend','State']]
yy=df['Profit']

print(xx)
print(yy)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='white',rc={'axes.facecolor':'green','grid.color':'red'})
g=sns.regplot(x=['Administration'],
            y=['profit'],
            data=df)
plt.show()

xx_corr=df[['R&D_Spend','Administration','Marketing_Spend','Profit']]
xxy=xx_corr.corr()
print(xxy)

sns.heatmap(xxy, annot=True, cmap="coolwarm", center=0)
plt.show()
