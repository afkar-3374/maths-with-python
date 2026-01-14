import numpy as np
import matplotlib.pyplot as plt

# x values
x = np.linspace(-5, 5, 400)

# given function
y = (-4*x - 3)*(x - 3)

# plot the graph
plt.plot(x, y, label="h(x) = (-4x - 3)(x - 3)")
plt.axhline(0)   # x-axis
plt.axvline(0)   # y-axis
plt.grid(True)

plt.xlabel("x")
plt.ylabel("h(x)")
plt.title("Graph of h(x) = (-4x - 3)(x - 3)")
plt.legend()

plt.show()
