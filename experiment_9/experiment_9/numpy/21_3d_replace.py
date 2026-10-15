import numpy as np

np.random.seed(42)
arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original 3D array:")
print(arr)

arr[arr > 50] = 0

print("\nAfter replacing values greater than 50 with 0:")
print(arr)
