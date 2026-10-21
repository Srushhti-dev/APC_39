import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
sizes = [100, 300, 200, 500]
plt.scatter(x, y, s=sizes, alpha=0.6)
plt.title("Bubble Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
