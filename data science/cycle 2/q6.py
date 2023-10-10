import numpy as np
# Create a 2D array (4x4)
print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
two_dimensional_array = np.arange(16).reshape(4,4)
print(two_dimensional_array)

# Display all elements excluding the first row
elements_excluding_first_row = two_dimensional_array[1:, :]

print("a. All elements excluding the first row:")
print(elements_excluding_first_row)
# Display all elements excluding the last column
elements_excluding_last_column = two_dimensional_array[:, :-1]

print("b. All elements excluding the last column:")
print(elements_excluding_last_column)

# Display the elements of the 1st and 2nd column in the 2nd and 3rd row
elements_1st_2nd_column_2nd_3rd_row = two_dimensional_array[1:3, 0:2]

print("c. Elements of the 1st and 2nd column in the 2nd and 3rd row:")
print(elements_1st_2nd_column_2nd_3rd_row)

# Display the elements of the 2nd and 3rd column
elements_2nd_3rd_column = two_dimensional_array[:, 1:3]

print("d. Elements of the 2nd and 3rd column:")
print(elements_2nd_3rd_column)

# Display the 2nd and 3rd element of the 1st row
elements_2nd_3rd_1st_row = two_dimensional_array[0, 1:3]

print("e. 2nd and 3rd element of the 1st row:", elements_2nd_3rd_1st_row)

# Display elements from indices 4 to 10 in descending order

x=two_dimensional_array.flatten()
ele=x[4:11]
ele_sorted_descending = np.sort(ele)[::-1]

# Print the sorted elements in descending order
print("f.Display the elements from indices 4 to 10 in descending order",ele_sorted_descending)



