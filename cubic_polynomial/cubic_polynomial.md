# Cubic Polynomial – Graph using Python

## Polynomial
We are given the cubic polynomial:

p(x) = x³ − x

---

## Objective
To plot the graph of a **cubic polynomial** using Python and understand its shape and zeros visually.

---

## Mathematical Concept
A cubic polynomial is a polynomial of **degree 3**.

General form:
p(x) = ax³ + bx² + cx + d

- Its graph is **curved with a bend (S-shape)**
- It can have **at most three zeros**

---

## Python Code Used

```python
import numpy as np
import matplotlib.pyplot as plt

# x values
x = np.linspace(-3, 3, 400)

# cubic polynomial
y = x**3 - x

plt.plot(x, y, 'm')
plt.axhline(0)   # x-axis
plt.axvline(0)   # y-axis
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Cubic Polynomial : p(x) = x^3 - x")
plt.show()
