import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(np.arange(0, 4), np.arange(0, 4))
u = np.ones_like(x) * 2
v = np.ones_like(y)
plt.barbs(x, y, u, v)
plt.title("Barbs Plot")
plt.show()
