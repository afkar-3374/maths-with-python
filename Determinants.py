import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 4, 100)

y1 = 5 - 2*x       # 2x + y = 5
y2 = x - 1         # x - y = 1 → y = x - 1

plt.plot(x, y1, label="2x + y = 5")
plt.plot(x, y2, label="x - y = 1")

plt.scatter(2, 1)  # solution point
plt.grid()
plt.legend()
plt.show()
