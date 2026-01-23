import math

print("Vector Dot Product Calculator")

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Dot product
dot = x1*x2 + y1*y2

# Magnitudes
mag1 = math.sqrt(x1**2 + y1**2)
mag2 = math.sqrt(x2**2 + y2**2)

# Angle between vectors
cos_theta = dot / (mag1 * mag2)
theta = math.degrees(math.acos(cos_theta))

print("\nVector A:", (x1, y1))
print("Vector B:", (x2, y2))

print("Dot Product =", dot)
print("Angle between vectors =", round(theta, 2), "degrees")
