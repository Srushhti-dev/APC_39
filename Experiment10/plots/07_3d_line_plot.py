import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]
z = [3, 1, 4, 2, 5]

ax.plot(x, y, z)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Line Plot")

plt.show()
