import matplotlib.pyplot as plt

# Vectors
a = (4, 2)
b = (2, 3)

# Dot product
dot = a[0]*b[0] + a[1]*b[1]

# Plot arrows (FIXED scale + width)
plt.quiver(
    0, 0, a[0], a[1],
    angles='xy', scale_units='xy', scale=1,
    color='r', width=0.008, label='Vector A'
)

plt.quiver(
    0, 0, b[0], b[1],
    angles='xy', scale_units='xy', scale=1,
    color='b', width=0.008, label='Vector B'
)

# Text
plt.text(1, 1, f"A·B = {dot}", fontsize=12)

# Axis settings
limit = max(a[0], a[1], b[0], b[1]) + 2

plt.xlim(0, limit)
plt.ylim(0, limit)

plt.axhline(0)
plt.axvline(0)
plt.grid(True)

plt.legend()
plt.title("Dot Product Visualization")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
