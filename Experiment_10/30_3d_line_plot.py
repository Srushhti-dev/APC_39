import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 200)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(np.sin(t), np.cos(t), t)
ax.set_title("3D Line Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
