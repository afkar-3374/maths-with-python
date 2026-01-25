import math

print("Vector Projection Calculator")

ax = float(input("Enter ax: "))
ay = float(input("Enter ay: "))

bx = float(input("Enter bx: "))
by = float(input("Enter by: "))

# Dot product
dot = ax*bx + ay*by

# Magnitude of b
mag_b = math.sqrt(bx**2 + by**2)

# Scalar projection
scalar_proj = dot / mag_b

# Vector projection
factor = dot / (mag_b**2)

proj_x = factor * bx
proj_y = factor * by

print("\nScalar Projection =", round(scalar_proj, 2))
print("Vector Projection =", (round(proj_x,2), round(proj_y,2)))
