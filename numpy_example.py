
# # Basic Example
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)


# # Example
# print("Enter ID's from 1 to 5")
# import numpy as np
# id=np.array([101,109,110,113,114])
# print("Your ID is:",id)


# # Find the transpose of a 2D matrix.
# print("Enter Matrix which you want Transpose")
# import numpy as np
# matrix=np.array([[2,4,6],[3,6,9]])
# transposed=matrix.T
# print(matrix)
# print(transposed)


# #  Transpose of 3*3 Matrix
# print("Enter 3*3 MAtrix")
# import numpy as np
# matrix=np.array([[3,4,5],[5,6,7],[7,8,9]])
# transpose=matrix.T
# print(matrix)
# print(transpose)


# # find Determinant
# print("Find Determinant")
# import numpy as np
# matrix=np.array([[2,4],[6,8]])
# Determinant=np.linalg.det(matrix)
# print(Determinant)


# Generate 100 random values and compute their mean and standard deviation.import numpy as np

# Generate 100 random values between 0 and 1
import numpy as np
data = np.random.rand(100)

# Calculate mean
mean_value = np.mean(data)

# Calculate standard deviation
std_deviation = np.std(data)

# Print results
print("Random Values:\n", data)
print("\nMean:", mean_value)
print("Standard Deviation:", std_deviation)
