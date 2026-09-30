import numpy as np

arr = np.array([45, 12, 89, 3, 67, 21, 56, 10])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Original array:", arr)
print("Ascending order:", ascending)
print("Descending order:", descending)
