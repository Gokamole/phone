import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(-1, 1, 100)
plt.plot(x, (1 - x**2)**0.5 + (x**2)**0.33, "--", marker='o', markersize=3)
plt.plot(x, -(1 - x**2)**0.5 + (x**2)**0.33,)
plt.show()