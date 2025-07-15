import numpy as np

# Step 1: Random values
rand_arr = np.random.rand(3, 3)  # 3x3 matrix with random floats (0 to 1)
print("Random float array (0-1):\n", rand_arr)

rand_int = np.random.randint(1, 100, size=(2, 4))  # Random integers between 1-100
print("\nRandom int matrix (2x4):\n", rand_int)

# Step 2: Seed (repeatable results)
np.random.seed(42)
same_rand = np.random.rand(2, 2)
print("\nSeeded random values:\n", same_rand)

# Step 3: Basic Statistics
stats_arr = np.array([10, 20, 30, 40, 50])
print("\nArray:", stats_arr)

print("Mean:", np.mean(stats_arr))   # Average
print("Median:", np.median(stats_arr))  # Middle value
print("Standard Deviation:", np.std(stats_arr))
print("Max:", np.max(stats_arr))
print("Min:", np.min(stats_arr))
