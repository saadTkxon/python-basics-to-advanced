import numpy as np

# 1D Array
arr = np.array([1, 2, 3, 4])  # ek simple 1D array
print(arr)  # Output: [1 2 3 4]

# Array basic properties
print(arr.ndim)     # 1 dimension
print(arr.shape)    # shape = (4,)
print(arr.size)     # total elements = 4
print(arr.dtype)    # data type, e.g., int64

# 2D Array (Matrix)
matrix = np.array([[1, 2], [3, 4]])
print(matrix)
# Output:
# [[1 2]
#  [3 4]]

# Useful NumPy functions
print(np.zeros((2, 3)))      # 2x3 matrix of 0s
print(np.ones((3, 3)))       # 3x3 matrix of 1s
print(np.eye(3))             # 3x3 identity matrix
print(np.arange(0, 10, 2))   # 0, 2, 4, 6, 8
print(np.linspace(0, 1, 5))  # 0. , 0.25, ..., 1.0

# Math operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)         # [5 7 9]
print(a * b)         # [4 10 18]
print(a ** 2)        # [1 4 9]
print(np.sqrt(a))    # [1. 1.41 1.73...]
