# Vector addition in 3D
x1, y1, z1 = map(int, input("Enter vector 1 (x y z): ").split())
x2, y2, z2 = map(int, input("Enter vector 2 (x y z): ").split())

result = (x1 + x2, y1 + y2, z1 + z2)
print("Resultant vector:", result)
