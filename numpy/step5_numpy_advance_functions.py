import numpy as np

# Step 1: Axis-wise operations
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Array:\n", arr)
print("Sum of all:", np.sum(arr))
print("Row-wise sum (axis=1):", np.sum(arr, axis=1))  # [6, 15]
print("Column-wise sum (axis=0):", np.sum(arr, axis=0))  # [5,7,9]

# Step 2: Transpose
print("\nOriginal:\n", arr)
print("Transposed:\n", arr.T)

# Step 3: Unique values and counts
vals = np.array([1, 2, 2, 3, 3, 3, 4])
unique_vals = np.unique(vals)
print("\nUnique values:", unique_vals)

# Step 4: Sorting
unsorted = np.array([5, 3, 8, 1])
print("Unsorted:", unsorted)
print("Sorted:", np.sort(unsorted))

# Step 5: Save and Load
np.save("my_array.npy", arr)  # Save to file
loaded = np.load("my_array.npy")
print("Loaded from file:\n", loaded)
