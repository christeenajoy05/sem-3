print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
import numpy as np

# Create a square matrix with random integer values
n = 4  # Specify the size of the square matrix
matrix = np.random.randint(1, 10, (n, n))  # Generates random integers between 1 and 9

# i) Inverse of the matrix
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("i) Inverse of the matrix:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("The matrix is singular. It does not have an inverse.")

# ii) Rank of the matrix
rank = np.linalg.matrix_rank(matrix)
print("\nii) Rank of the matrix:", rank)

# iii) Determinant of the matrix
determinant = np.linalg.det(matrix)
print("\niii) Determinant of the matrix:", determinant)

# iv) Transform the matrix into a 1D array
matrix_1d = matrix.flatten()
print("\niv) Matrix transformed into a 1D array:")
print(matrix_1d)

# v) Eigenvalues and Eigenvectors of the matrix
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("\nv) Eigenvalues of the matrix:")
print(eigenvalues)
print("\nEigenvectors of the matrix:")
print(eigenvectors)
