import numpy as np
import matplotlib.pyplot as plt

print("Visual Solver for Linear Equations")

# Input
a = float(input("Enter coefficient of x in eqn1: "))
b = float(input("Enter coefficient of y in eqn1: "))
c = float(input("Enter constant in eqn1: "))

d = float(input("Enter coefficient of x in eqn2: "))
e = float(input("Enter coefficient of y in eqn2: "))
f = float(input("Enter constant in eqn2: "))

# Convert to y = mx + k form
x = np.linspace(-10, 10, 400)

if b != 0 and e != 0:

    y1 = (c - a*x) / b
    y2 = (f - d*x) / e

    # Plot
    plt.plot(x, y1, label="Equation 1")
    plt.plot(x, y2, label="Equation 2")

    plt.axhline(0)
    plt.axvline(0)
    plt.grid(True)
    plt.legend()

    plt.title("Graphical Solution of Linear Equations")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()

else:
    print("Cannot plot: vertical line detected.")
