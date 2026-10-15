import numpy as np

np.random.seed(42)
arr = np.random.randint(1, 101, size=(3, 4, 5))
flattened = arr.flatten()
average = np.mean(flattened)

print("Random 3D array:")
print(arr)
print("\nFlattened array:")
print(flattened)
print("\nAverage value:", average)

print("\nElements greater than 50:")
print(flattened[flattened > 50])

print("\nEven elements:")
print(flattened[flattened % 2 == 0])

print("\nElements less than average:")
print(flattened[flattened < average])
