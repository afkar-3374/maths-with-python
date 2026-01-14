import sympy as sp

# define variable
x = sp.symbols('x')

# define the factors
factor1 = -4*x - 3
factor2 = x - 3

print("Given function: h(x) = (-4x - 3)(x - 3)\n")

# Step 1
print("Step 1:")
print("Solve -4x - 3 = 0")
solution1 = sp.solve(factor1, x)
print("x =", solution1[0], "\n")

# Step 2
print("Step 2:")
print("Solve x - 3 = 0")
solution2 = sp.solve(factor2, x)
print("x =", solution2[0], "\n")

print("Final Answer:")
print("The zeros are:", solution1[0], "and", solution2[0])
