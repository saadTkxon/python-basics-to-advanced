import numpy as np

# Step 1: Ek simple 1D array banate hain
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original Array:", arr)

# Step 2: Indexing (0-based index hota hai)
print("arr[0] (first element):", arr[0])
print("arr[3] (4th element):", arr[3])

# Step 3: Negative Indexing (right to left)
print("arr[-1] (last element):", arr[-1])
print("arr[-2] (second last):", arr[-2])

# Step 4: Slicing - arr[start:stop]
print("\narr[1:4] -> index 1 to 3:", arr[1:4])  # 20, 30, 40
print("arr[:3] -> start to index 2:", arr[:3])  # 10, 20, 30
print("arr[3:] -> index 3 to end:", arr[3:])    # 40, 50, 60

# Step 5: Step slicing - arr[start:stop:step]
print("arr[::2] -> every 2nd element:", arr[::2])  # 10, 30, 50
print("arr[::-1] -> reverse array:", arr[::-1])    # 60, 50, ...

# Step 6: 2D Array (Matrix) banate hain
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\n2D Matrix:\n", matrix)

# Step 7: Indexing in 2D array
print("Element at row 0, col 0:", matrix[0, 0])  # 1
print("Element at row 2, col 1:", matrix[2, 1])  # 8

# Step 8: Row slicing (row 1 only)
print("Row 1:", matrix[1, :])  # 4 5 6

# Step 9: Column slicing (col 2 only)
print("Column 2:", matrix[:, 2])  # 3 6 9

# Step 10: Sub-matrix slice (center 2x2)
print("Center 2x2 block:\n", matrix[0:2, 1:3])  # [[2,3],[5,6]]

# Step 11: Reshape (1D -> 2D)
a = np.array([1, 2, 3, 4, 5, 6])
reshaped = a.reshape((2, 3))  # 2 rows, 3 columns
print("\nOriginal 1D array:", a)
print("Reshaped to 2x3:\n", reshaped)

# Step 12: Flatten (2D -> 1D)
flat = reshaped.flatten()
print("Flattened array:", flat)



"""
is file mein hum seekhenge:

 Indexing
 Slicing (array ka part nikaalna)
 Negative indexing
 2D indexing
 Array reshape karna
"""