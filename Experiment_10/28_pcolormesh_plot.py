import matplotlib.pyplot as plt
import numpy as np

data = np.random.default_rng(42).random((10, 10))
plt.pcolormesh(data, cmap="viridis", shading="auto")
plt.colorbar(label="Value")
plt.title("Pseudocolor Plot")
plt.show()
