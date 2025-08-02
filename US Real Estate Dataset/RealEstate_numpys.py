import numpy as np
broker_id,price,city=np.genfromtxt('C:\\Users\\Zeeshan PC\\Documents\\GitHub\\Python-course\\US Real Estate Dataset\\RealEstate-USA.csv',delimiter=',',dtype=None,usecols=[0,2,7],unpack=True,skip_header=1)
print("All Broker Id's Is:")
print(broker_id)
print("All Prices is:")
print(price)
print("All Cities is:")
print(city)

#  Calculate Mean
print("Mean of Price is:")
print(np.mean(price))
# Median
print(np.median(price))
# average
print(np.average(price))
# Standard Deviation
print(np.std(price))

#  Arithmetic Operation
addition=broker_id+price
Division=broker_id/price
Multiplication=broker_id*price
substraction=broker_id-price

# Additiom
print("Sum is:",addition)
# Substraction
print("substraction is:",substraction)
# Multiplication
print("Multiplication is:",Multiplication)
# Division
print("Division is:",Division)


# Operation Mathematics
# Square
print("Square",np.square(price))
# Square Root
print("Square Root",np.sqrt(price))
# power
print("Power Is",np.power(price,2))

# Trignometry Function
pricepie=(price/np.pi)+1

print("Cosine:",np.cos(pricepie))
print("Sine:",np.sin(pricepie))
print("tan:",np.tan(pricepie))

# Hyperbolic Function

print("Cosh:",np.cosh(pricepie))
print("Sineh:",np.sinh(pricepie))
print("tanh:",np.tanh(pricepie))

# Log and Natural Log
print("Log:",np.log(pricepie))
print("log base of 10:",np.log10(pricepie))

# Inverse Hyperbolic Function
print("Hyperbolic of cos is:",np.arccosh(pricepie))
print("Hyperbolic of sin is:",np.arcsinh(pricepie))
print("Hyperbolic of tan is:",np.arctanh(pricepie))


# 2 Dimension Array
d2broker_price=np.array([broker_id,price])
print(d2broker_price)
# Check Number of Dimensions
print(d2broker_price.ndim)
# Check Dimension Size
print(d2broker_price.size)
# Check Dtype
print(d2broker_price.dtype)

# Slicing
print(d2broker_price[:5,:3])
# /
print(d2broker_price[:2,:2])
d2index=d2broker_price[0,1]
d2index1=d2broker_price[0,2]

# indexing
print(d2index)
print(d2index1)