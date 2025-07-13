#  Example Check Datatype
name="50"
print(type(name))
n=type(name)
print("Your data Type is:",n)

# Example 
stri="pakistanis"
print("Trace IS")
print(stri[8:10:])
print(stri[6:8])
print(len(stri))


#  Another Example
print("find Substring")
name="Zeeshan"
print(name)
print(len(name))
print(name[0:3])
print(type(name))


# print("Enter Name in Loop And run Loop 5 times:")
name=str(input("Enter Your Name:"))
for i in range(5):
    print(name)
print("Check data type [Name]")
print(type(name))
print(len(name))
print(name[3:7:])



# using List Method and find datatype,using for loop
# year,name,ceo,distance
# List
data=[2007,"Zeeshan","QAMAR ABBASS",12.5]
print(data)
print(type(data))
for i in range(4):
    print(data[i])
    print(i)

# Tuple
dataT=(2007,"Zeeshan","QAMAR ABBASS",12.5)
print(dataT)
print(type(dataT))
for i in range(4):
    print(dataT[i])


# Set
dataS={2007,"Zeeshan","QAMAR ABBASS",12.5}
print(dataS)
print(type(dataS))
for ii in dataS:
    print(ii)

# Dictionary
dataD={'a':2007,'b':"Zeeshan",'c':"QAMAR_ABBASS",'d':12.5}
print(dataD)
print(type(dataD))
for i in dataD: 
    print(dataD[i])
