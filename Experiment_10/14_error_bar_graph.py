import matplotlib.pyplot as plt

plt.errorbar([1, 2, 3], [10, 20, 15], yerr=[2, 3, 1], fmt="o", capsize=5)
plt.title("Error Bar Graph")
plt.xlabel("X-axis")
plt.ylabel("Value")
plt.show()
