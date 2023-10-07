import numpy as np

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Create a 2D array (2x3) with complex data type
complex_array = np.array([
    [1 + 2j, 2 + 3j, 3 + 4j],
    [4 + 5j, 5 + 6j, 6 + 7j]
], dtype=complex)

# Print the 2D array
print("2D Array:")
print(complex_array)

# Get the number of rows and columns
rows, columns = complex_array.shape

# Display the number of rows and columns
print("Number of rows:", rows)
print("Number of columns:", columns)

# Display the dimension of the array
print("Array dimension:", complex_array.shape)

# Reshape the array to 3x2
reshaped_array = complex_array.reshape(3, 2)

# Print the reshaped array
print("Reshaped 3x2 Array:")
print(reshaped_array)
