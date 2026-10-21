import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)
x = rng.standard_normal(1000)
y = rng.standard_normal(1000)
plt.hexbin(x, y, gridsize=20, cmap="Blues")
plt.colorbar(label="Count")
plt.title("Hexbin Plot")
plt.show()
