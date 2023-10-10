def transposeMatrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    return [[matrix[i][j] for i in range(num_rows)] for j in range(num_cols)]
