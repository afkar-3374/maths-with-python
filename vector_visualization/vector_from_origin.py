import matplotlib.pyplot as plt

# Vector from origin
x, y = 4, 3

plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='r')

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.title("Vector from Origin")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
