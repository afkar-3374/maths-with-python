import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
y = x**2 - 4

plt.plot(x, y, 'g')
plt.axhline(0)   # x-axis
plt.axvline(0)   # y-axis
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Quadratic Polynomial : p(x) = x**2 - 4")
plt.show()
