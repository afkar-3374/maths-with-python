# Derivative of a Function using Python (Visual Method)

## Given Function
We are given the function:

\[
y = x^2 + 3
\]

---

## Objective
To understand the **derivative of a function** visually by plotting:
- the original function, and  
- its derivative on the same graph using Python.

---

## Mathematical Concept

The derivative of a function represents the **rate of change** or **slope** of the curve.

For the given function:

\[
\frac{d}{dx}(x^2 + 3) = 2x
\]

So:
- Original function: \( y = x^2 + 3 \)
- Derivative: \( \frac{dy}{dx} = 2x \)

---

## Python Code Used

```python
import numpy as np
import matplotlib.pyplot as plt

# x values
x = np.linspace(-5, 5, 400)

# function and derivative
y = x**2 + 3
dy = 2*x

# plot
plt.plot(x, y, label="y = x² + 3")
plt.plot(x, dy, label="dy/dx = 2x")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Derivative of y = x² + 3")
plt.show()
```

---

## Observation from the Graph
- The curve \( y = x^2 + 3 \) is a **parabola**.
- The line \( y = 2x \) represents the **slope of the curve at each point**.
- At \( x = 0 \), the slope is zero, so the curve is flat.
- As \( x \) increases or decreases, the slope increases or decreases accordingly.

---

## Conclusion
Plotting a function and its derivative together helps in understanding:
- how the slope changes,
- how derivatives relate to graphs,
- and the geometric meaning of differentiation.

This visual approach makes calculus concepts clearer and more intuitive.
