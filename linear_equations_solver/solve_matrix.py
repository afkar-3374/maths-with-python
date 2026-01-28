import numpy as np

print("Solve System of Linear Equations (Matrix Method)")

# Input coefficients
a = float(input("Enter coefficient of x in eqn1: "))
b = float(input("Enter coefficient of y in eqn1: "))
c = float(input("Enter constant in eqn1: "))

d = float(input("Enter coefficient of x in eqn2: "))
e = float(input("Enter coefficient of y in eqn2: "))
f = float(input("Enter constant in eqn2: "))

# Matrix form AX = B
A = np.array([[a, b],
              [d, e]])

B = np.array([c, f])

# Solve
try:
    X = np.linalg.solve(A, B)

    print("\nSolution:")
    print("x =", round(X[0], 2))
    print("y =", round(X[1], 2))

except np.linalg.LinAlgError:
    print("\nNo unique solution (determinant = 0)")
