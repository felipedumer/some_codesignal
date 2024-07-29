def multiply_matrices(matrix1, matrix2):
    # Number of rows in the first matrix
    rows_matrix1 = len(matrix1)
    # Number of columns in the first matrix (and rows in the second matrix)
    cols_matrix1 = len(matrix1[0])
    # Number of columns in the second matrix
    cols_matrix2 = len(matrix2[0])
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]
    
    # Perform matrix multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Example matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Multiply the matrices
result = multiply_matrices(matrix1, matrix2)

# Print the result
for row in result:
    print(row)