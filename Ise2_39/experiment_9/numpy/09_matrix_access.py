import numpy as np

matrix = np.arange(1, 17).reshape(4, 4)

print("Matrix:\n", matrix)
print("\nFirst row:", matrix[0])
print("Last column:", matrix[:, -1])
print("Diagonal elements:", np.diag(matrix))
print("Second and third rows:\n", matrix[1:3])
