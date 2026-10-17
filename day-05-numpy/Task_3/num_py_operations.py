
import numpy as np

# 1. Create a sample matrix
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Matrix:")
print(arr)

# 2. Array properties
print("\nNumber of dimensions:", arr.ndim)
print("Matrix shape:", arr.shape)
print("Total elements:", arr.size)

# 3. Indexing
print("\nFirst element:", arr[0, 0])
print("Element at row 2, column 3:", arr[1, 2])

# 4. Slicing
print("\nFirst row:", arr[0, :])
print("First column:", arr[:, 0])
print("First two rows:")
print(arr[:2, :])

# 5. Mathematical operations
print("\nAddition (+10):")
print(arr + 10)

print("\nMultiplication (*2):")
print(arr * 2)

print("\nSubtraction (-5):")
print(arr - 5)

# 6. Statistical operations
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 7. Row-wise and column-wise sums
print("\nRow-wise sum:", np.sum(arr, axis=1))
print("Column-wise sum:", np.sum(arr, axis=0))

# 8. Filter values greater than 50
print("\nElements greater than 50:")
print(arr[arr > 50])
