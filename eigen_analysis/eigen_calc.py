import numpy as np

print("Eigenvalues and Eigenvectors Calculator")

# Matrix input
A = np.array([
    [float(input("Enter a11: ")), float(input("Enter a12: "))],
    [float(input("Enter a21: ")), float(input("Enter a22: "))]
])

# Compute
values, vectors = np.linalg.eig(A)

print("\nMatrix A:\n", A)
print("\nEigenvalues:\n", values)
print("\nEigenvectors:\n", vectors)
