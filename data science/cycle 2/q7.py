import numpy as np

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Create two 2D arrays
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# a. Add the 2 matrices and print it
addition_result = array1 + array2
print("a. Addition Result:")
print(addition_result)

# b. Subtract 2 matrices
subtraction_result = array1 - array2
print("b. Subtraction Result:")
print(subtraction_result)

# c. Multiply the individual elements of matrix
multiplication_result = array1 * array2
print("c. Multiplication Result:")
print(multiplication_result)

# d. Divide the elements of the matrices
division_result = array1 / array2
print("d. Division Result:")
print(division_result)

# e. Perform matrix multiplication
matrix_multiplication_result = np.dot(array1, array2)
print("e. Matrix Multiplication Result:")
print(matrix_multiplication_result)

# f. Display transpose of the matrix
transpose_result = np.transpose(array1)
print("f. Transpose Result:")
print(transpose_result)

# g. Sum of diagonal elements of a matrix
diagonal_sum = np.trace(array1)
print("g. Sum of Diagonal Elements:")
print(diagonal_sum)
