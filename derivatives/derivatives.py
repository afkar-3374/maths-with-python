import numpy as np
import matplotlib.pyplot as plt

# x values
x = np.linspace(-5, 5, 400)

# function and derivative
y = x**2 + 3
dy = 2*x

# plot
plt.plot(x, y, label="y = x² + 3")
plt.plot(x, dy, label="dy/dx = 2x")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Derivative of y = x² + 3")
plt.show()
