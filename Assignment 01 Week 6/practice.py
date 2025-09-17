import numpy as np

price,acre_lot,city,house_size = np.genfromtxt("C:\\Users\\AA laptops\\Documents\\GitHub\\My-AI-course\\RealEstate-USA.csv", delimiter=',',usecols=(2,5,7,10),dtype=None,skip_header=0,unpack=True)


print(price)
print(acre_lot)
print(city)
print(house_size)