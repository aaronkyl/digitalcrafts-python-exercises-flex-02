matrix1 = [[2, -2], [5, 3]]
matrix2 = [[-1, 4], [7, -6]]
result = []

matrix1_rows = len(matrix1)
matrix1_cols = len(matrix1[1])
matrix2_rows = len(matrix2)
matrix2_cols = len(matrix2[1])

for i in range(0, matrix1_rows):
    result.append([])
    for j in range(0, matrix2_cols):
        result[i].append(0)
        for k in range(0, matrix1_cols):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
            k += 1
        j += 1
    i += 1

print(result)