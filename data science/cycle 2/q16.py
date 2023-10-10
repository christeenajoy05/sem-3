import numpy as np

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Define the matrix A (replace with your own matrix)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Perform SVD on matrix A
U, S, VT = np.linalg.svd(A)

# Reconstruct the original matrix from the three matrices obtained in SVD
reconstructed_A = np.dot(U, np.dot(np.diag(S), VT))

# Print the original matrix A, SVD components, and the reconstructed matrix
print("Original Matrix A:")
print(A)

print("\nMatrix U:")
print(U)

print("\nSingular Values S:")
print(S)

print("\nMatrix VT (Transpose of V):")
print(VT)

print("\nSVD Reconstructed Matrix A:")
print(reconstructed_A)
