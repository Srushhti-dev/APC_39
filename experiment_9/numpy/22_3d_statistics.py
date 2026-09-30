import numpy as np

np.random.seed(42)
arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Random 3D array:")
print(arr)

print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
