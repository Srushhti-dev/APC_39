import matplotlib.pyplot as plt
import numpy as np

y, x = np.mgrid[-3:3:100j, -3:3:100j]
u = -1 - x**2 + y
v = 1 + x - y**2
plt.streamplot(x, y, u, v, density=1.0)
plt.title("Stream Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
