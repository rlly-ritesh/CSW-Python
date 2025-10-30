import numpy as np
# Create a matrix
matrix = np.array([[1, 2], [3, 4]])
print("Original Matrix:")
print(matrix)
# Determinant
det = np.linalg.det(matrix)
print("\nDeterminant:", det)
# Inverse
inv = np.linalg.inv(matrix)
print("\nInverse Matrix:")
print(inv)
# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
# Matrix transpose
transpose = matrix.T
print("\nTranspose:")
print(transpose)
# Verify: Matrix × Inverse = Identity
identity = np.dot(matrix, inv)
print("\nMatrix × Inverse (should be identity):")
print(identity)