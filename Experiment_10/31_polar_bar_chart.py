import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 4, endpoint=False)
radii = [2, 4, 3, 5]
fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
ax.bar(theta, radii, width=0.6, alpha=0.7)
ax.set_title("Polar Bar Chart")
plt.show()
