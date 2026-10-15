import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
z = [2, 3, 5, 4, 6]

ax.scatter(x, y, z)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Scatter Plot")

plt.show()
