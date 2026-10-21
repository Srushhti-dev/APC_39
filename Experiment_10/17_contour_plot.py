import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
plt.contour(X, Y, Z, levels=12)
plt.colorbar(label="Z")
plt.title("Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
