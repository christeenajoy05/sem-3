import numpy as np

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Define matrix A with dimensions 5x6
A = np.array([[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30]])

# Define matrix B with dimensions 3x3
B = np.array([[2, 1, 0],
              [0, 2, 0],
              [1, 0, 1]])

# Extract a submatrix of dimensions 3x3 from A (e.g., top-left corner)
submatrix = A[:3, :3]
print('Extracted submatrix:\n', submatrix)

# Multiply the extracted submatrix with B
result = np.dot(submatrix, B)
print('Result: \n', result)

# Replace the extracted submatrix in A with the result
A[:3, :3] = result

print("Matrix A after replacing the submatrix with the result:")
print(A)
