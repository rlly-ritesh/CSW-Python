import numpy as np
# Dot product of two vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot_product = np.dot(a, b)
print("Vector a:", a)
print("Vector b:", b)
print("Dot product (a · b):", dot_product)
print("Calculation: (1*4) + (2*5) + (3*6) =", dot_product)
# Matrix multiplication using dot product
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = np.dot(matrix1, matrix2)
print("\nMatrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Matrix multiplication result:")
print(result)