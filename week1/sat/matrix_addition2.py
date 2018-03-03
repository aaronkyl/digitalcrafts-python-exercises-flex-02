matrix1 = [[1, 3, 1], [2, 4]]
matrix2 = [[5, 2, 5], [1, 0]]
result = []

for i in range(0, len(matrix1)):
    result.append([])
    for j in range(0, len(matrix1[i])):
        result[i].append(matrix1[i][j] + matrix2[i][j])

print(result)