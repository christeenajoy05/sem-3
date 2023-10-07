import numpy as np

# Create a 3D array of float data type
#  we create a 2x3x4 array (2 planes, each with 3 rows and 4 columns)

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
array_3d = np.array([
    [
        [1.0, 2.0, 3.0, 4.0],
        [5.0, 6.0, 7.0, 8.0],
        [9.0, 10.0, 11.0, 12.0]
    ],
    [
        [13.0, 14.0, 15.0, 16.0],
        [17.0, 18.0, 19.0, 20.0],
        [21.0, 22.0, 23.0, 24.0]
    ]
], dtype=float)

# Print the 3D array
print("3D Array:")
print(array_3d)
