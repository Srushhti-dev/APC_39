import matplotlib.pyplot as plt

plt.pie([40, 30, 20, 10], labels=["A", "B", "C", "D"],
        autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart")
plt.axis("equal")
plt.show()
