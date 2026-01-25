import matplotlib.pyplot as plt

# Vectors
a = (4, 3)
b = (5, 1)

# Dot product
dot = a[0]*b[0] + a[1]*b[1]
mag_b_sq = b[0]**2 + b[1]**2

# Projection
factor = dot / mag_b_sq
proj = (factor*b[0], factor*b[1])

# Plot
plt.quiver(0,0,a[0],a[1],color='r',scale=1,scale_units='xy',label='Vector A')
plt.quiver(0,0,b[0],b[1],color='b',scale=1,scale_units='xy',label='Vector B')
plt.quiver(0,0,proj[0],proj[1],color='g',scale=1,scale_units='xy',label='Projection')

plt.axhline(0)
plt.axvline(0)
plt.grid(True)

plt.xlim(0,7)
plt.ylim(0,7)

plt.legend()
plt.title("Vector Projection")

plt.xlabel("X")
plt.ylabel("Y")

plt.show()
