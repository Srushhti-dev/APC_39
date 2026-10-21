import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
fig, axes = plt.subplots(2, 2, figsize=(9, 6))
axes[0, 0].plot(x, [1, 4, 2, 5], marker="o")
axes[0, 0].set_title("Line")
axes[0, 1].bar(["A", "B", "C"], [3, 7, 5])
axes[0, 1].set_title("Bar")
axes[1, 0].scatter(x, [5, 2, 4, 1])
axes[1, 0].set_title("Scatter")
axes[1, 1].hist([1, 2, 2, 3, 3, 3, 4], bins=4, edgecolor="black")
axes[1, 1].set_title("Histogram")
plt.tight_layout()
plt.show()
