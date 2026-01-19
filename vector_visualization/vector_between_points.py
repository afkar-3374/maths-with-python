import matplotlib.pyplot as plt

# Points
x1, y1 = 1, 2
x2, y2 = 5, 6

# Vector from A to B
vx = x2 - x1
vy = y2 - y1

plt.quiver(x1, y1, vx, vy, angles='xy', scale_units='xy', scale=1, color='m')

plt.scatter([x1, x2], [y1, y2])
plt.text(x1, y1, "A")
plt.text(x2, y2, "B")

plt.xlim(0, 7)
plt.ylim(0, 7)
plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.title("Vector Between Two Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
