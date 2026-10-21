import matplotlib.pyplot as plt

data = [[2, 3, 3, 4, 5], [3, 4, 5, 6, 8]]
plt.violinplot(data, showmedians=True)
plt.title("Violin Plot")
plt.ylabel("Value")
plt.show()
