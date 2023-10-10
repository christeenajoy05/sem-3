import numpy as np

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Create a 1D NumPy array
arr_1d = np.array([1, 2, 3])

# Convert the 1D array to a diagonal matrix
diagonal_matrix = np.diag(arr_1d)

# Print the diagonal matrix
print(diagonal_matrix)


# Create a square 2D NumPy array
square_matrix = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

# Extract the diagonal elements as a 1D array
diagonal_1d = np.diag(square_matrix)

# Print the 1D array of diagonal elements
print(diagonal_1d)

# Create a rectangular 2D NumPy array
rectangular_matrix = np.array([[1, 2, 3],
                               [4, 5, 6]])

# Extract the diagonal elements as a 1D array
diagonal_1d = np.diag(rectangular_matrix)

# Print the 1D array of diagonal elements
print(diagonal_1d)
