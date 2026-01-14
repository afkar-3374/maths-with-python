import sympy as sp

# define the variable
x = sp.symbols('x')

# define the function
h = (-4*x - 3)*(x - 3)

# solve h(x) = 0 using symbolic method
zeros = sp.solve(h, x)

print("Given function: h(x) = (-4x - 3)(x - 3)")
print("Zeros of the function are:")
for z in zeros:
    print(z)
