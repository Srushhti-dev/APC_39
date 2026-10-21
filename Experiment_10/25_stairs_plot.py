import matplotlib.pyplot as plt

values = [2, 4, 3, 6]
edges = [0, 1, 2, 3, 4]
plt.stairs(values, edges)
plt.title("Stairs Plot")
plt.xlabel("Interval")
plt.ylabel("Value")
plt.show()
