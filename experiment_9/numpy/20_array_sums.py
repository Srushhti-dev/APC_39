import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nSum of all elements:", np.sum(arr))
print("Sum of each layer:", np.sum(arr, axis=(1, 2)))
print("Sum along rows (axis=1):")
print(np.sum(arr, axis=1))
print("Sum along columns (axis=2):")
print(np.sum(arr, axis=2))
