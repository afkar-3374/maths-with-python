import math

print("Vector Magnitude and Direction Calculator")

x = float(input("Enter x component: "))
y = float(input("Enter y component: "))

# Magnitude
magnitude = math.sqrt(x**2 + y**2)

# Direction (angle in degrees)
angle = math.degrees(math.atan2(y, x))

print("\nVector:", (x, y))
print("Magnitude |v| =", round(magnitude, 2))
print("Direction θ =", round(angle, 2), "degrees")
