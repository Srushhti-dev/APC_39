import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
a = [10, 20, 15]
b = [5, 10, 8]
plt.bar(x, a, label="A")
plt.bar(x, b, bottom=a, label="B")
plt.xticks(x, ["X", "Y", "Z"])
plt.legend()
plt.title("Stacked Bar Graph")
plt.show()
