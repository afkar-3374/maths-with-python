# Linear Polynomial – Graph using Python

## Polynomial
We are given the linear polynomial:

\[
p(x) = 2x + 1
\]

---

## Objective
To plot the graph of a **linear polynomial** using Python and understand its graphical properties.

---

## Mathematical Concept
A linear polynomial is a polynomial of **degree 1**.

General form:
\[
p(x) = ax + b
\]

- Its graph is a **straight line**
- It has **only one zero** (at most)

---

## Python Code Used

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = 2*x + 1

plt.plot(x, y, 'b')
plt.axhline(0)   # x-axis
plt.axvline(0)   # y-axis
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Polynomial : p(x) = 2x + 1")
plt.show()
```

---

## Observation from the Graph
- The graph is a **straight line**.
- It cuts the **x-axis only once**.
- The zero of the polynomial is at:
\[
2x + 1 = 0 \Rightarrow x = -\frac{1}{2}
\]

---

## Conclusion
This graph confirms that a linear polynomial has:
- a straight-line graph, and  
- only **one zero**.

Plotting linear polynomials using Python helps in understanding their behavior clearly and visually.
