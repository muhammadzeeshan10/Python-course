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

# using displot with kind kde
g=sns.displot(data=first20,x='Funding Rounds',hue='Funding Rounds')
g.figure.show()
g.figure.suptitle("using Displot")
read=input("Waiting for some time...")

# using kdeplot
g=sns.kdeplot(data=first20,x="Year Founded")
g.figure.show()
g.figure.suptitle("using kdeplot")
means=input("wait for some time")

# using histplot
g=sns.histplot(data=first20,x='Startup Name',y='Funding Round',multiple="stack",hue='Funding Round')
g.figure.suptitle("using histplot")
g.figure.show()
read=input("Waiting for some time...")

# using Scaterplot
f=sns.scatterplot(x='agency',y='price',data=first20)
f.figure.show()
read=input("Waiting for some time...")

# using Barplot
f=sns.barplot(data=first20,x='agency',y='price')
f.figure.suptitle("f=sns.barplot(data=first20,x='agency',y='price')")
f.figure.show()
read=input("Waiting for some time...")


