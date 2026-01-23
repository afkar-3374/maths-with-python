import matplotlib.pyplot as plt
import math

# Vector values
x = float(input("Enter x component: "))
y = float(input("Enter y component: "))

# Calculations
magnitude = math.sqrt(x**2 + y**2)
angle = math.degrees(math.atan2(y, x))

# Plot vector
plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='b')

# Display text
plt.text(x/2, y/2,
         f"|v| = {round(magnitude,2)}\nθ = {round(angle,2)}°",
         fontsize=10)

# Graph settings
limit = max(abs(x), abs(y)) + 2

plt.xlim(-limit, limit)
plt.ylim(-limit, limit)

plt.axhline(0)
plt.axvline(0)
plt.grid(True)

plt.title("Vector Magnitude and Direction")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
