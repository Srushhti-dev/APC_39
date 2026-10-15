import numpy as np

arr = np.array([25, 60, 45, 80, 30, 95, 55, 40, 75, 20])

print("Original array:", arr)
arr[arr > 50] = 0
print("After replacing values greater than 50 with 0:", arr)
