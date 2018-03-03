# TODO

matrix1 = [[2, -2], [5, 3]]
matrix2 = [[-1, 4], [7, -6]]
result = []

array_dimension = len(matrix1)

for i in range(0, array_dimension):
    result.append([])
    for j in range(0, array_dimension):
        for k in range(0, array_dimension):
            result[i].append(matrix1[i][j] * matrix2[i][i] + matrix1[i][j] * matrix2[j][i])
        
print(result)