import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)
flattened = arr.flatten()

print("Original 3D array:")
print(arr)
print("\nFlattened array:")
print(flattened)

print("\nSum:", np.sum(flattened))
print("Average:", np.mean(flattened))
print("Maximum:", np.max(flattened))
print("Minimum:", np.min(flattened))
