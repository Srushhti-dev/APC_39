import numpy as np

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

print("Matrix:\n", matrix)
print("\nSum of each row:", np.sum(matrix, axis=1))
print("Sum of each column:", np.sum(matrix, axis=0))
