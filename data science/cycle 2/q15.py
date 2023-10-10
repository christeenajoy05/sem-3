import numpy as np

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Define matrix A and vector b (replace with your own values)
A = np.array([[2, 1,-2],
              [3,0,1],
              [1,1,-1]])

b = np.array([-3,5,2])


# Solve for X using np.linalg.solve()
X = np.linalg.solve(A, b)

# Print the solution X
print("Solution for X:")
print(X)
