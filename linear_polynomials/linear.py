import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = 2*x + 1

plt.plot(x, y, 'b')
plt.axhline(0)   # x-axis
plt.axvline(0)   # y-axis
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Polynomial : p(x) = 2x + 1")
plt.show()
