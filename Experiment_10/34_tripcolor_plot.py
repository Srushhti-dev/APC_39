import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 0, 1, 0.5])
y = np.array([0, 0, 1, 1, 0.5])
z = np.array([1, 2, 3, 4, 2.5])
plt.tripcolor(x, y, z, shading="gouraud", cmap="viridis")
plt.colorbar(label="Value")
plt.title("Tripcolor Plot")
plt.show()
