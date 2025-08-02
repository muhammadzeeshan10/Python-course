import numpy as np
address,city,latitude,longitude=np.genfromtxt('C:\\Users\\Zeeshan PC\\Documents\\GitHub\\Python-course\\US Food Restaurant DataSet\\FastFoodRestaurants.csv',delimiter=',',dtype=None,unpack=True,usecols=[0,1,4,5],skip_header=1)
print("Address:")
print(address)
print("City:")
print(city)
print("Latitude:")
print(latitude)
print("Longitutude:")
print(longitude)

