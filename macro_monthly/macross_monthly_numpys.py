import numpy as np
year,month,industry=np.genfromtxt('C:\\Users\\Zeeshan PC\\Documents\\GitHub\\Python-course\\macro_monthly\\macro_monthly.csv',delimiter=',',dtype=float,unpack=True,usecols=[0,1,2],skip_footer=1)
print("Year")
print(year)
print("Month")
print(month)
print("Industrial")
print(industry)

# Arithmetic Operarion
addition=year+industry
substraction=year-industry
multiplication=year*industry
division=year/industry

# Addition
print("Addition",addition)
print("substraction",substraction)
print("Multiplication",multiplication)
print("Division",division)

# Mathematical Operation
print("Square",np.square(year))
print("Square Root",np.sqrt(year))
print("Power",np.power(year,2))

# Trignometry Function
yearpi=(year/np.pi)+1

# Cos Function
print("Cos:",np.cos(yearpi))
# sin Function
print("Sin:",np.sin(yearpi))
# tan Function
print("Tan:",np.tan(yearpi))

# Hyperbolic Function
# Cosh Function
print("Cosh:",np.cosh(yearpi))
# Sinh Function
print("sinh:",np.sinh(yearpi))
# Tanh Function
print("tanh:",np.tanh(yearpi))

# Inverse Hyperbolic Function
# Cosh Function
print("Cosh",np.arccosh(yearpi))
# Sin Function
print("Sinh",np.arcsinh(yearpi))
# Tan Function
print("tanh",np.arctanh(yearpi))

# 2D Dimension
d2year_month=np.array([year,month])
print(d2year_month)
print(d2year_month.dtype)
print(d2year_month.shape)
print(d2year_month.size)

# Slicing 
d2year_month1=d2year_month[:2,:5]
print(d2year_month1)
# /
d2year_month1=d2year_month[:9,:11]
print(d2year_month1)

# Through indexing
d2year_month5=d2year_month[0,2]
print(d2year_month5)

#  Finished******************