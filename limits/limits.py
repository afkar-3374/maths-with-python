import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(1.3, 1.56, 400)
y = np.cos(theta) / (np.pi/2 - theta)

plt.plot(theta, y)
plt.axvline(np.pi/2, linestyle='--')
plt.axhline(1, linestyle='--')

plt.xlabel("θ")
plt.ylabel("Value")
plt.title("Limit of cosθ / (π/2 − θ)")
plt.grid()
plt.show()
