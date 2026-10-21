import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.broken_barh([(1, 2), (4, 1.5), (7, 2)], (10, 5))
ax.set_ylim(5, 20)
ax.set_xlim(0, 10)
ax.set_xlabel("Time")
ax.set_yticks([12.5])
ax.set_yticklabels(["Task A"])
ax.set_title("Broken Bar Graph")
plt.show()
