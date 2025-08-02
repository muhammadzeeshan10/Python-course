import pandas as pd
df=pd.read_csv('C:\\Users\\Zeeshan PC\\Documents\\GitHub\\Python-course\\US Real Estate Dataset\\RealEstate-USA.csv',delimiter=",",parse_dates=[4],date_format={'date_time':'%d-%m-%y'})
print(df.info())
# get discribe
print(df.describe)
# get dtypes
print(df.dtypes)

# take first 5 row 
print(df.head(5))

# take last 5 row
print(df.tail(5))

# Get Shape
print("Shape:",df.shape)

# Get Specific Column
year=df['brokered_by']
print(year)

# Get Multiple Column
column2=df[['brokered_by','status']]
print(column2)


# Loc Method
# pick specific row
secondrow=df.loc[2]
print(secondrow)

# pick Multiple Column
secondrow3=df.loc[[1,2]]
print(secondrow3)

# pick specific row in slicing
secondrow1=df.loc[2:5]
print(secondrow1)

#Selecting a single column using .loc
secondrow2=df.loc[:1,'status']
print(secondrow2)
print()

# Select Multiple Column through slicing
secondrow4=df.loc[:3,['brokered_by','status']]
print(secondrow4)

# throgh range
secondrow5=df.loc[:3,'price':'bath']
print(secondrow5)

# Now through indexing
index_column=pd.read_csv('C:\\Users\\Zeeshan PC\\Documents\\GitHub\\Python-course\\macro_monthly\\macro_monthly.csv',delimiter=",",parse_dates=[4],date_format={'date_time':'%d-%m-%y'},index_col='Year')
# Whole Table
print(index_column)
# Dtype
print(index_column.dtypes)
# Shape
print(index_column.shape)
# info
print(index_column.info())

# using Loc 
xli=index_column.loc[1993]
print(xli)

# using Loc and Pick Multiple
xlii=index_column.loc[[1993,1994]]
print(xlii)

# throgh range
xliii=index_column.loc[1993:1995]
print(xliii)

# selecting a single column using Loc Method
xliiii=index_column.loc[:1993,'Consumer_Price Index']
print(xliiii)

# using I-Loc Method

od=index_column.iloc[1]
print(od)

od1=index_column.iloc[1,3]
print(od1)

od2=index_column.iloc[[1,3,5]]
print(od2)
# throgh Range
od3=index_column.iloc[1:3]
print(od3)

od4=index_column.iloc[:2,:3]
print(od4)

od5=index_column.iloc[:,[2,4]]
print(od5)

# add new line
#  df.loc[len(df.index)]=[.........]
