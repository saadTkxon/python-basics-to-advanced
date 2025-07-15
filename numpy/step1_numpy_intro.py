# Step 1: NumPy ka import
# np short form use hoti hai taake bar bar numpy na likhna pade
import numpy as np

# Step 2: Ek simple 1D array banana (yeh list ki tarah hota hai)
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Step 3: Array ka dimension dekhna (1D, 2D, etc.)
print("Dimension (ndim):", arr.ndim)  # 1 dimension

# Step 4: Array ka shape (kitni rows/columns)
print("Shape:", arr.shape)  # (5,) -> 1 row with 5 elements

# Step 5: Array ka size (total number of elements)
print("Size:", arr.size)  # 5 elements

# Step 6: Data type check karna (int32, float64, etc.)
print("Data type:", arr.dtype)

# Step 7: 2D Array (Matrix) banana
matrix = np.array([[1, 2], [3, 4]])
print("\n2D Matrix:\n", matrix)

# Step 8: Matrix ka shape, dimension, etc. check karna
print("Matrix Dimension:", matrix.ndim)  # 2D
print("Matrix Shape:", matrix.shape)    # (2, 2)
print("Matrix Size:", matrix.size)      # 4 elements

# Step 9: Zeros ka array banana (2 rows, 3 columns)
zeros_arr = np.zeros((2, 3))
print("\nArray of zeros:\n", zeros_arr)

# Step 10: Ones ka array banana (3x3)
ones_arr = np.ones((3, 3))
print("\nArray of ones:\n", ones_arr)

# Step 11: Identity matrix banana (3x3) - diagonal 1
eye_arr = np.eye(3)
print("\nIdentity matrix:\n", eye_arr)

# Step 12: arange use karna (0 se 10 tak step 2)
range_arr = np.arange(0, 10, 2)
print("\nArange (0 to 10 step 2):", range_arr)

# Step 13: linspace - 0 se 1 tak 5 equal numbers
lin_arr = np.linspace(0, 1, 5)
print("\nLinspace (0 to 1, 5 numbers):", lin_arr)

# Step 14: Array operations - addition, multiplication, etc.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nAddition:", a + b)        # [5 7 9]
print("Multiplication:", a * b)    # [4 10 18]
print("Square of a:", a ** 2)      # [1 4 9]
print("Square root of a:", np.sqrt(a))  # [1. 1.41 1.73]
