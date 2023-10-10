import numpy as np

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Define a matrix (replace with your own matrix)
"""matrix = np.array([[1, 2, 3],
                   [2, 4, 5],
                   [3, 5, 6]])"""

"""matrix = np.array([[0, 2, -3],
                  [-2, 0, 4],
                  [3, -4, 0]])"""


matrix= np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])


# Transpose the matrix to obtain its transpose
transpose_matrix = np.transpose(matrix)

# Check for symmetry
if np.array_equal(matrix, transpose_matrix):
    print("The matrix is symmetric.")
elif np.array_equal(matrix, -transpose_matrix):
    print("The matrix is skew symmetric.")
else:
    print("The matrix is neither symmetric nor skew symmetric.")
