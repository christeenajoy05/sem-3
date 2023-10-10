import numpy as np

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Create a matrix X (e.g., 3x3)
X = np.array([[2, 3, 4],
              [5, 6, 7],
              [8, 9, 10]])

# i) Display the cube of each element of the matrix using different methods

# Method 1: Using the power operator (**) to calculate the cube
cubed_elements_1 = X ** 3

# Method 2: Using the power function (np.power) to calculate the cube
cubed_elements_2 = np.power(X, 3)

# Method 3: Using the multiply function (np.multiply) to calculate the cube
cubed_elements_3 = np.multiply(X, X) * X

# Method 4: Using the * operator to calculate the cube
cubed_elements_4 = X * X * X

print("i) Cube of each element of the matrix (Method 1):\n", cubed_elements_1)
print("\nCube of each element of the matrix (Method 2):\n", cubed_elements_2)
print("\nCube of each element of the matrix (Method 3):\n", cubed_elements_3)
print("\nCube of each element of the matrix (Method 4):\n", cubed_elements_4)

# ii) Display the identity matrix of the given square matrix
identity_matrix = np.identity(X.shape[0])
print("\nii) Identity matrix of the given square matrix:\n", identity_matrix)

# iii) Display each element of the matrix to different powers (e.g., squares and cubes)
squared_elements = np.power(X, 2)
cubed_elements = np.power(X, 3)

print("\niii) Squared elements of the matrix:\n", squared_elements)
print("\nCubed elements of the matrix:\n", cubed_elements)

Y = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Perform the operation X^2 + 2Y
result = X**2 + 2*Y

print("Result of the operation X^2 + 2Y:\n", result)