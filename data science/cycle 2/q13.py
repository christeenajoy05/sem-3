import numpy as np

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Define matrices A, B, and C
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = np.array([[9, 10],
              [11, 12]])

# Perform matrix multiplication of A, B, and C
result = np.dot(np.dot(A, B), C)

# Print the result
print("Result of matrix multiplication:")
print(result)
