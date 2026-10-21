import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contourf(X, Y, Z, levels=15, cmap="viridis")
plt.colorbar(label="Z")
plt.title("Filled Contour Plot")
plt.show()
