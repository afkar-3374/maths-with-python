import numpy as np
import matplotlib.pyplot as plt

# x values
x = np.linspace(-3, 3, 400)

# cubic polynomial
y = x**3 - x

plt.plot(x, y, 'm')
plt.axhline(0)   # x-axis
plt.axvline(0)   # y-axis
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Cubic Polynomial : p(x) = x^3 - x")
plt.show()
