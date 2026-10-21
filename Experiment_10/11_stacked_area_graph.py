import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
plt.stackplot(x, [2, 3, 4, 5], [1, 2, 2, 3], labels=["A", "B"])
plt.legend()
plt.title("Stacked Area Graph")
plt.xlabel("X-axis")
plt.ylabel("Value")
plt.show()
