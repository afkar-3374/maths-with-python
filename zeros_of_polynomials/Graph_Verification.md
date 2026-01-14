# Graphical Verification of Zeros of a Polynomial

## Given Function
We are given the polynomial function:

**h(x) = (-4x - 3)(x - 3)**

---

## Objective
To **verify the zeros of the polynomial graphically** using Python.

The zeros of a polynomial are the **values of x where the graph cuts the x-axis**,  
that is, where **h(x) = 0**.

---

## Concept Used
In the graphical method:
- The x-axis represents all points where y = 0
- The points where the graph intersects the x-axis are called **zeros of the polynomial**

---

## Python Code Used

```python
import numpy as np
import matplotlib.pyplot as plt

# x values
x = np.linspace(-5, 5, 400)

# polynomial function
y = (-4*x - 3)*(x - 3)

# plot the graph
plt.plot(x, y, label="h(x) = (-4x - 3)(x - 3)")
plt.axhline(0)   # x-axis
plt.axvline(0)   # y-axis
plt.grid(True)

plt.xlabel("x")
plt.ylabel("h(x)")
plt.title("Graph of h(x) = (-4x - 3)(x - 3)")
plt.legend()
plt.show()
