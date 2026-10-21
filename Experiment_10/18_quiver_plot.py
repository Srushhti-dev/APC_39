import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(np.arange(0, 3), np.arange(0, 3))
u = np.ones_like(x)
v = np.ones_like(y)
plt.quiver(x, y, u, v)
plt.title("Quiver Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
