import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)



"""
the output are 
[1 2 3 4]

"""

#  Array  basic functions

print(arr.ndim)    # array ke kitne dimensions hain (1D, 2D, 3D...) → yahan 1D hai
print(arr.shape)   # array ka shape tuple mein (rows, columns) → yahan (4,)
print(arr.size)    # array mein total kitne elements hain → 4
print(arr.dtype)   # array ke elements ka data type → int64 (ya int32 depending on system)


"""
output
1
(4,)
4
int64

"""


# 2D Array (matrix) 

matrix = np.array([[1, 2], [3, 4]])
print(matrix)

"""
output
[[1 2]
 [3 4]]

"""


# most useful functions

print(np.zeros((2, 3)))     # 2 rows × 3 columns wali matrix jisme sab elements 0 hain
print(np.ones((3, 3)))      # 3x3 matrix jisme sab elements 1 hain
print(np.eye(3))            # 3x3 identity matrix (diagonal 1, baaki 0)
print(np.arange(0, 10, 2))  # 0 se start, 10 se pehle tak, step 2
print(np.linspace(0, 1, 5)) # 0 se 1 tak 5 equally spaced numbers

"""
output
[[0. 0. 0.]
 [0. 0. 0.]]

[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]

[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

[0 2 4 6 8]

[0.   0.25 0.5  0.75 1.  ]

"""



# Math operations on arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)    # addition
print(a * b)    # multiplication
print(a ** 2)   # square
print(np.sqrt(a)) # square root


# 3d matxir
matrix = np.array([[1, 2], [3, 4]])  # 2 rows aur 2 columns wali matrix
print(matrix)


"""
Output:
[[1 2]
 [3 4]]

"""