import numpy as np

arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Array:", arr)
print("Even numbers:", even)
print("Odd numbers:", odd)
