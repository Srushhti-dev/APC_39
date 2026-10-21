import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]
plt.fill_between(x, y, alpha=0.5)
plt.plot(x, y, marker="o")
plt.title("Area Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
