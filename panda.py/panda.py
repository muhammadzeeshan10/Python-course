import pandas as pd
zee=pd.read_csv('E:\Week3\zameencom-property-data-By-Kaggle-Short.csv',delimiter=";",parse_dates=[14],date_format={'Date and time':'%d-%m-%Y'})
print(zee)
print(zee.info())

# Display Last 3 Rows
print("display Last 3 Rows:")
print(zee.tail(3))

# Display first 3 Rows
print("display First 3 Rows:")
print(zee.head(3))

# Choose Specific
print(zee[87:89])

# Get Summary
print("Summary describe:",zee.describe())

print(zee.shape)

# Call specific one  Column
city=zee['city']
print("your City All Record is:")
print(city)

agency=zee['agency']
print("Your All Agency Name is:")
print(agency)


# Call Multiple Column 
print("Here Given below Agency and City data is:")
agency_city=zee[['agency','city']]
print(agency_city)


print("call Multiple Column:")
longitude_latitude=zee[['latitude','longitude']]
print(longitude_latitude)


# Select Specific Row 
row1=zee.loc[1]
print("Get Specific Row:")
print(row1)

# Select Row splicing
row1to5=zee.loc[0:5]
print("You can see only 1st five row:")
print(row1to5)

# see column
location=zee['location']
print("you see Location Column")
print(location)

# see specific Row 

row55to89=zee.loc[55:89]
print(row55to89)

secondrow4=zee.loc[zee['agency']=='gateway properties']
print("conditional statement using lock")
print(secondrow4)

# selecting column using lock

column2=zee.loc[:1,'agency']
print("your first column is for agency:")
print(column2)

column3=zee.loc[:1,'location']
print("Location column is:")
print(column3)


# print("Here Given below Agency and City data is:")
# agency_city=zee[['agency','city']]
# print(agency_city)


location=zee['location']
agency=zee['agency']
column4=zee[['agency','location']]
print(column4)


# Show any two  Column 
select4column=zee.loc[:1,'location':'agency']
print("********************")
print(select4column)

print("Display any two column:")
print(zee[['agency','location']])

# show two column with only two rows
print("************")
print(zee.loc[:2,['agency','location']])

# show all column only 0 to 2 rows
print(zee.loc[:1,'property_id':'agent'])


# -----------------------------------
# case 2
print("Case 2 start with Loc and index here:")
zee_index_col=pd.read_csv('E:\Week3\zameencom-property-data-By-Kaggle-Short.csv',delimiter=";",parse_dates=[14],date_format={'Date Added':'%d-%m-%Y'},index_col='property_id')
print(zee_index_col)
print(zee_index_col.ndim)
print(zee_index_col.dtypes)
print(zee_index_col.info())


# Select Specific Row:
specific_row=zee_index_col.loc[482892]
print(specific_row)

specific_row2=zee_index_col.loc[785289:1646880]
print(specific_row2)
# select Specific Data from sheet of column
selectcolumn=zee_index_col.loc[:785289,'agency']
print("print Single Column using loc")
print(selectcolumn)

# ************************************************************
# Select one or Multiple Column 
selectcolumn2=zee_index_col.loc[:785289,['agency','location']]
print(selectcolumn2)

# Select Specific row or multiple
selectcolumn3=zee_index_col.loc[:785289,'location':'agency']
print(selectcolumn3)

# *************************************************************
# Case 3
# iloc Method
# Single row
selectrow0=zee_index_col.iloc[0]
print("Print 0 index row:")
print(selectrow0)
# Multiple Rows
selectrow=zee_index_col.iloc[[0, 1,5]]
print("Specific Row:")
print(selectrow)

# slicing 
selectrow2=zee_index_col.iloc[0:9]
print("0 to 9 index rows is:")
print(selectrow2)
# Select column
selectcolumn4=zee_index_col.iloc[:,9]
print(selectcolumn4)
# select Multiple column
selectcolumn5=zee_index_col.iloc[:,[9,12]]
print(selectcolumn5)
# select column through slicing
selectcolumn6=zee_index_col.iloc[:,9:12]
print(selectcolumn6)
# pick combined both row and column
selectcolumn7=zee_index_col.iloc[2:9:2,1:9:2]
print(selectcolumn7)
# end iloc
# print(zee.info())
zee.loc[len(zee.index)]=[3477952,22,"https://www.zameen.com/Property/lahore_model_town_6_kanal_excellen_wah","House2",2200000002,"Model Town2","Lahore2","Punjab2",312.483868658082,742.325685501099,2,"6 Kanal2","For Sale2",2,"07-17-2019","Real Biz International2","Usama Khan2"]
print(zee)
print()

# rows=zee_index_col.loc[3477952]
# print(rows)

# specific_row=zee_index_col.loc[482892]
# print(specific_row)


# Delete Row
zee.drop(1,axis=0,inplace=True)
print(zee)

# Delete Multiple Row
zee.drop([2,5],inplace=True,axis=0)
print(zee)

# delete through slpicing
zee.drop(zee.index[2:5],axis=0,inplace=True)
print(zee)

# Now Delete Column
zee.drop('location_id',axis=1,inplace=True)
print(zee)

# Delete Multiple Column
zee.drop(['area','purpose'],axis=1,inplace=True)
print(zee.info(memory_usage=bool()))


# Now Rename function used
zee.rename(mapper={'property_Trscking_id':'property_id'},inplace=True,axis=1)
print(zee)

zee.rename(mapper={'location':'Loaction','city':'CITY'},inplace=True,axis=1)
print(zee.info())

# Rename row labels
zee.rename(mapper={0:10},inplace=True)
print(zee)

zee.drop(10,axis=0,inplace=True)


price=zee['price']
print(price)

# Ascending order
zee.sort_values('price',inplace=True)
zee.sort_index(axis=1,inplace=True)