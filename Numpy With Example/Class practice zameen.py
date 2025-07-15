import numpy as np
ids,price,latitude,longitude,property_type=np.genfromtxt('E:\Week3\zameencom-property-data-By-Kaggle-Short.csv',delimiter=';',usecols=(0,4,8,9,3),dtype=None,unpack=True,skip_header=1)
print(ids)
print(price)
print(longitude)
print(latitude)
print(property_type)

#  Statistics operation
print("Means is",np.mean(price))
print("Average of price is:",np.average(price))
print("Standard deviation of price is:",np.std(price))
print("Median of priece is:",np.median(price))
print("Min is:",np.min(price))
print("Max is:",np.max(price))

# Math operation
print("Square Root is:",np.sqrt(price))
print("Square is:",np.square(price))
print("Power is:",np.power(price,price))
print("ABS is",np.abs(price))

# Basic Arithmetic Operation
add=longitude+latitude
mul=longitude*latitude
sub=longitude-latitude
div=longitude/latitude

print("The Addition of Long And lati is:",add)
print("The Substraction of Long And lati is:",sub)
print("The Multiplication of Long And lati is:",mul)
print("The Division of Long And lati is:",div)

# Trignometry Function
pricepie=(price/np.pi)+1

# Calculate Sin , Cos ,Tan function
print("The Cos Function is:",np.cos(pricepie))
print("The Sin Function is:",np.sin(pricepie))
print("The Tan Function is:",np.tan(pricepie))

# Calculate Hyperbolic Trignometry Function
print("The Cos Hyperbolic Fucntion is:",np.cosh(pricepie))

# Calculate Inverse Hyperbolc Function
print("The Inverse Hyperbolic of Cos is:",np.arccosh(pricepie))


# Dimension Array
d2longlat=np.array([longitude,latitude])
print("2 Dimension Array is:",d2longlat)

# Check the dimension Array
print("Check dimension Array is:",d2longlat.ndim) 

# check the size in dimension
print("Check the Size of Dimension is:",d2longlat.size)

# Check Only longitutde size
d1long=np.array([longitude])
print("Check the size of longitute Array is",longitude.size)

# check shape
print("Check Shape",d2longlat.shape)

# check Dtype
print("Check Datatype:",d2longlat.dtype)

d2slpicing=d2longlat[:2:5,:1]
# Splicing Array
print(" Splicing",d2slpicing)

# indexing Array
for elem in np.nditer(d2longlat):
    print(d2longlat)