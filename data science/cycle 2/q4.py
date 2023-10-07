import numpy as np

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Create a one-dimensional array with 10 elements using arange
one_dimensional_array = np.arange(10)

# a. Display the first 4 elements
first_4_elements = one_dimensional_array[:4]

# b. Display the last 6 elements
last_6_elements = one_dimensional_array[-6:]

# c. Display elements from index 2 to 7
elements_2_to_7 = one_dimensional_array[2:8]

# Display the results
print("Original Array:", one_dimensional_array)
print("a. First 4 elements:", first_4_elements)
print("b. Last 6 elements:", last_6_elements)
print("c. Elements from index 2 to 7:", elements_2_to_7)
