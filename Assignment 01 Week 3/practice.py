import numpy as np

broker_id,price,city,house_size=np.genfromtxt('D:\AI\Assignment 01 Week 3\RealEstate-USA.csv',delimiter=',',dtype=None,skip_header=1,usecols=(0,2,7,10),unpack=True)
# Task 01

print(broker_id)
print(price)
print(city)

# Task 02
print("Mean of Price is:",np.mean(price))
print("Median of Price is:",np.median(price))
print("AVG of Price is",np.average(price))
print("Maximum of Price is",np.max(price))
print("Minimum of Price is",np.min(price))  


# Task 03
print(house_size)

print("House Size of Max is:",np.max(house_size))
print("House Size of Min is:",np.min(house_size))
print("House Size of Median is:",np.median(house_size))
print("House Size of SD is:",np.std(house_size))

# Task 04

addition=price + house_size
substraction=price - house_size
Multiplication=price * house_size
Division=price / house_size

print(addition)
print(substraction)
print(Multiplication)
print(Division)

# Task 05
# 2D Array
d2array=np.array([price,house_size])
print("2D Array:",d2array)


# Task 06
# 3D Array
d3array=np.array([[price,house_size,broker_id]])
print(d3array)

# Task 07
# print("NPIDTER:",np.nditer(price))
for var in np.nditer(price):
    print(var)


# Task 08
for var in np.nditer(house_size):
    print(var)

# Task 09

print("NDIM",np.ndim(price))
print("Shape:",np.shape(price))
print("Size:",np.size(price))
print("Dtype:",price.dtype)
print("Info",np.info())

# Task 10

# Slicing
d2array=np.array([price,house_size])
print("2D Array:",d2array[1:2])


# Task 11
# Row : from 1st  value to 3rd  value 
print("Row : from 1st  value to 3rd  value ",d2array[1:3])
print("olumn: from 2nd value to 4th value ",d2array[1,1:4])

# Task 12
print("Geometric Function:")
print("Cos Function:",np.cos(price))
print("Sin Function:",np.sin(price))

