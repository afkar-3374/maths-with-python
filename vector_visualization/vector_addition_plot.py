import matplotlib.pyplot as plt

# Vectors
a = (3, 2)
b = (1, 4)

# Resultant
r = (a[0] + b[0], a[1] + b[1])

plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1,
           color='r', label='Vector a')
plt.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1,
           color='b', label='Vector b')
plt.quiver(0, 0, r[0], r[1], angles='xy', scale_units='xy', scale=1,
           color='g', label='Resultant')

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.legend()
plt.title("Vector Addition Visualization")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
