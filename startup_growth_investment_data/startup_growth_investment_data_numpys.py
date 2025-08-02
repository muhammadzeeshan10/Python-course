import numpy as np
startup,funding,investment,country=np.genfromtxt('C:\\Users\\Zeeshan PC\\Documents\\GitHub\Python-course\\startup_growth_investment_data\\startup_growth_investment_data.csv',delimiter=',',usecols=[0,2,3,6],dtype=None,unpack=True,skip_header=1)
print("Startup")
print(startup)
print("Funding")
print(funding)
print("Investment")
print(investment)
print("Country")
print(country)

# Calculate Mean
print("Mean",np.mean(funding))
# MAximum
print("Maximum",np.max(funding))
# Avergae
print("Avergae",np.average(funding))
# Median
print("Median",np.median(funding))
# Minimum
print("Minimum",np.min(funding))


# Arithmetic 
addition=funding+investment
substraction=funding-investment
multiplication=funding*investment
division=funding/investment

# Addition
print("Addition",addition)
print("substraction",substraction)
print("Multipliaction",multiplication)
print("Divivion",division)

# Operation Mathematics 
print("Square",np.square(funding))
print("Square Root",np.sqrt(funding))
print("power",np.power(funding,2))

# Trignometry Function
fundingpi=(funding/np.pi)+1

print("Cos Function is",np.cos(fundingpi))
print("Sin Function is",np.sin(fundingpi))
print("tan Function is",np.tan(fundingpi))

# Hyperbolic Function
print("Hyperbolic of cos",np.cosh(fundingpi))
print("Hyperbolic of sin",np.sinh(fundingpi))
print("Hyperbolic of tan",np.tanh(fundingpi))

# inverse Function
print("Inverse of Cos:",np.arccosh(fundingpi))
print("Inverse of sin:",np.arcsinh(fundingpi))
print("Inverse of tan:",np.arctanh(fundingpi))

# log function
print("Log :",np.log(fundingpi))
print("Log of base 10 is:",np.log10(fundingpi))

# 2D Dimenion Array
d2funding_invetment=np.array([funding,investment])

print(d2funding_invetment.dtype)
print(d2funding_invetment.ndim)
print(d2funding_invetment.shape)
print(d2funding_invetment.size)


# Slicing
print(d2funding_invetment[:2,:2])
# /
print(d2funding_invetment[0:5,5:9])

# through indexing 
print(d2funding_invetment[0,1])
print(d2funding_invetment[0,5])