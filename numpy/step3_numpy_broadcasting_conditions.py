import numpy as np

# Step 1: Broadcasting
# Jab arrays ka shape same na ho, to chhoti array ko auto expand karke calculation hoti hai
a = np.array([1, 2, 3])
b = 5  # scalar (single value)
print("Array a:", a)
print("Array b (scalar):", b)

# Broadcasting: b ko [5,5,5] treat karega
print("a + b:", a + b)  # [6 7 8]

# Broadcasting with 2D
x = np.array([[1, 2, 3],
              [4, 5, 6]])
y = np.array([10, 20, 30])  # shape: (3,)
print("\nBroadcasting 2D + 1D:\n", x + y)
# Each row mein y add ho jaayega

# Step 2: Conditions (Boolean masks)
arr = np.array([5, 10, 15, 20])
print("\nOriginal Array:", arr)

# Condition check karo
mask = arr > 10
print("Condition (arr > 10):", mask)  # [False False  True  True]

# Filter values jahan condition true ho
print("Filtered:", arr[mask])  # [15 20]

# Ek line mein
print("Direct Filter:", arr[arr > 10])
