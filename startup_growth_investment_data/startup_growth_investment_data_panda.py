import pandas as pd
df=pd.read_csv('C:\\Users\\Zeeshan PC\\Documents\\GitHub\\Python-course\\startup_growth_investment_data\\startup_growth_investment_data.csv',delimiter=",",parse_dates=[4],date_format={'date_time':'%d-%m-%y'})
# Get Info
print(df.info())
# get Decribe
print(df.describe)
# get shape
print(df.shape)
# head 20
print(df.head(20))
# tail 20
print(df.tail(20))

# Get Specific Column
Industry=df['Industry']
print(Industry)

# Mutiple Column
Industry1=df[['Industry','Funding Rounds']]
print(Industry1)

# using Loc Method
Industry2=df.loc[1]
print(Industry2)
# get Multple row through Loc Method
Industry3=df.loc[[1,3]]
print(Industry3)
# through Range
Industry4=df.loc[1:3]
print(Industry4)

# through Range & Slicing
Industry5=df.loc[:2,'Funding Rounds']

# through Range & Slicing and Multiple Column
Industry6=df.loc[:2,['Funding Rounds','Industry']]
print(Industry6)

# using I-Lock Method

oop=pd.read_csv('C:\\Users\Zeeshan PC\\Documents\\GitHub\\Python-course\\startup_growth_investment_data\\startup_growth_investment_data.csv',parse_dates=[4],date_format={'date_time':'%d-%m-%y'},index_col='Startup Name')
print(oop)
# Get Info
print(oop.info())
# Get Describe
print(oop.describe)
# Get Shape
print(oop.info())

# Get Single Column
column1=oop.loc['Startup_37']
print(column1)
# Get Multiple Column
column2=oop.loc[['Startup_37','Startup_39']]
print(column2)
# Throgh Range
column3=oop.loc['Startup_37':'Startup_50']
print(column3)
# Throgh Slicing
column5='Startup_37'
print(column5)

#  Using I-Loc Method 
new=oop.iloc[37]
print(new)

new1=oop.iloc[[37,40]]
print(new1)

new2=oop.iloc[:22]
print(new2)

new3=oop.iloc[:2,:3]
print(new3)

# add new Line

# oop.loc[len(oop.index)]=...........