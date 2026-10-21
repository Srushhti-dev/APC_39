import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)
x = rng.standard_normal(1000)
y = rng.standard_normal(1000)
plt.hist2d(x, y, bins=20, cmap="viridis")
plt.colorbar(label="Count")
plt.title("2D Histogram")
plt.show()
