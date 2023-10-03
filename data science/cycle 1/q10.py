def add_matrices(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Return None if matrices have different dimensions

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def print_matrix(matrix):
    for row in matrix:
        print(row)


try:
    print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
    # Input matrices from the user
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix1 = []
    matrix2 = []

    print("Enter elements of the first matrix:")
    for i in range(rows):
        row = [int(x) for x in input().split()]
        matrix1.append(row)

    print("Enter elements of the second matrix:")
    for i in range(rows):
        row = [int(x) for x in input().split()]
        matrix2.append(row)

    # Call the function to add the matrices
    sum_matrix = add_matrices(matrix1, matrix2)

    if sum_matrix is not None:
        print("Sum of the two matrices:")
        print_matrix(sum_matrix)
    else:
        print("Matrices have different dimensions. Cannot perform addition.")
except ValueError:
    print("Invalid input. Please enter valid numerical values for matrix elements.")
