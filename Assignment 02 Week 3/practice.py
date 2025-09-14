import pandas as pd

# Task 01
df=pd.read_csv('D:\AI\Assignment 02 Week 3\RealEstate-USA.csv')
print(df)

# Task 02
print(df.describe())
print(df.info())
print(df.dtypes)
print(df.shape)

# Task 03

data = {
    "Broker_ID": [101, 102, 103, 104],
    "Price": [250000, 320000, 450000, 380000],
    "City": ["NY", "LA", "SF", "CHI"],
    "House_Size": [1200, 1500, 2000, 1800]
}

dfd=pd.DataFrame(data)
print(dfd.to_string())


# Task 04 & 5
print(dfd.head(2))
print(dfd.tail(3))

price=dfd['Price']

# print whole specific column
print(price)

# task 06
prices=df['street']
print(prices.to_string())

# Task 07
# print Multiple column
multiple=df[['street','price']]
print(multiple)

# Task 08
index5=df.loc[5]
print(index5)

# Task 09
index359=df.loc[[3,5,7]]
print(index359)

# Task 10
# slicing
slicing=df.loc[3:9]
print(slicing)

# Task 11
condition=df.loc[df["price"]>1000000]
print(condition)

# Task 12
condition2=df.loc[df["street"]=='Adjuntas']
print(condition2)

# Task 13
equality=df.loc[df["price"]>180500 & (df["city"]=="adjuntas")]
print(equality)

city=df["city"]
print(city)
# Slicing
print(city[1:9])

# Task 14
multiple2=df[["street","city","state","zip_code"]]
print(multiple2[:7])

# Task 15
# Choose Multiple Column throgh slicing

multiple3=df.loc[:,"city":"zip_code"]
print(multiple3)

# Task 17
# using iloc

df_index=pd.read_csv('D:\AI\Assignment 02 Week 3\RealEstate-USA.csv',index_col='brokered_by')
print(df_index)

row1=df_index['street']
print(row1[:1])

# Task 18
row2=df_index[["street","city"]]
print(row2[:2])

# Task 19
column1=df_index["street"]
print(column1)

