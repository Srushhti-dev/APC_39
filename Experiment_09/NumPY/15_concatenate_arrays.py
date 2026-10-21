import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

print("Array A:\n", a)
print("\nArray B:\n", b)

print("\nHorizontal concatenation:")
print(np.hstack((a, b)))

print("\nVertical concatenation:")
print(np.vstack((a, b)))
