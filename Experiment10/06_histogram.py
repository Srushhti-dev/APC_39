import matplotlib.pyplot as plt

data = [10, 12, 15, 15, 18, 20, 22, 25, 25, 30]
plt.hist(data, bins=5, edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()