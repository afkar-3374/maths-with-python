# Vector Representation and Addition (All Cases)

## Topic
Vectors – Representation and Addition in 2D and 3D

---

## Objective
To understand all standard cases of vector representation and vector addition, and to implement them using Python by directly applying mathematical formulas.

---

## Introduction
A vector is a quantity that has both **magnitude and direction**.  
Vectors can be represented using coordinates and can be added by adding their corresponding components.

Vectors are commonly represented in:
- **Two dimensions (2D)** → (x, y)
- **Three dimensions (3D)** → (x, y, z)

---

## Case 1: Vector from Origin in 2D  
**Origin O(0, 0) → A(x, y)**

\[
\vec{OA} = (x, y)
\]

```python
x = int(input("Enter x: "))
y = int(input("Enter y: "))

vector = (x, y)
print("Vector from origin:", vector)
```

---

## Case 2: Vector from Origin in 3D  
**Origin O(0, 0, 0) → A(x, y, z)**

\[
\vec{OA} = (x, y, z)
\]

```python
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

vector = (x, y, z)
print("Vector from origin:", vector)
```

---

## Case 3: Vector Between Two Points in 2D  
**A(x₁, y₁) → B(x₂, y₂)**

\[
\vec{AB} = (x_2 - x_1,\; y_2 - y_1)
\]

```python
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

vector = (x2 - x1, y2 - y1)
print("Vector from A to B:", vector)
```

---

## Case 4: Vector Between Two Points in 3D  
**A(x₁, y₁, z₁) → B(x₂, y₂, z₂)**

\[
\vec{AB} = (x_2 - x_1,\; y_2 - y_1,\; z_2 - z_1)
\]

```python
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
z1 = int(input("Enter z1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
z2 = int(input("Enter z2: "))

vector = (x2 - x1, y2 - y1, z2 - z1)
print("Vector from A to B:", vector)
```

---

## Case 5: Vector Addition in 2D

\[
(x_1, y_1) + (x_2, y_2) = (x_1 + x_2,\; y_1 + y_2)
\]

```python
x1, y1 = map(int, input("Enter vector 1 (x y): ").split())
x2, y2 = map(int, input("Enter vector 2 (x y): ").split())

result = (x1 + x2, y1 + y2)
print("Resultant vector:", result)
```

---

## Case 6: Vector Addition in 3D

\[
(x_1, y_1, z_1) + (x_2, y_2, z_2) = (x_1 + x_2,\; y_1 + y_2,\; z_1 + z_2)
\]

```python
x1, y1, z1 = map(int, input("Enter vector 1 (x y z): ").split())
x2, y2, z2 = map(int, input("Enter vector 2 (x y z): ").split())

result = (x1 + x2, y1 + y2, z1 + z2)
print("Resultant vector:", result)
```

---

## Learning Outcome
- Understood all standard vector representations
- Learned vector addition in both 2D and 3D
- Connected mathematical formulas directly with Python code
- Improved conceptual clarity through implementation

---

## Tools Used
- Python
- Basic vector algebra

---

## Conclusion
Studying vectors through Python programming helped reinforce theoretical concepts and made vector operations easier to understand, apply, and remember.
