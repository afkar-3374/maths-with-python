import numpy as np
import matplotlib.pyplot as plt

# Matrix
A = np.array([[2, 1],
              [1, 2]])

# Eigen calculation
values, vectors = np.linalg.eig(A)

# Scale factor to make arrows visible
scale = 2

v1 = vectors[:, 0] * scale
v2 = vectors[:, 1] * scale

# Plot eigenvectors
plt.quiver(0, 0, v1[0], v1[1],
           angles='xy', scale_units='xy', scale=1,
           color='r', width=0.01, label='Eigenvector 1')

plt.quiver(0, 0, v2[0], v2[1],
           angles='xy', scale_units='xy', scale=1,
           color='b', width=0.01, label='Eigenvector 2')

# Axes
plt.axhline(0)
plt.axvline(0)
plt.grid(True)

plt.xlim(-3, 3)
plt.ylim(-3, 3)

plt.legend()
plt.title("Eigenvectors of Matrix")

plt.xlabel("X")
plt.ylabel("Y")

plt.show()
