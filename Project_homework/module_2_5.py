def get_matrix(n, m, value):
    matrix = []
    if n < 1 or m < 1:
        return matrix
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print('Матрица:', result1)
print('Матрица:', result2)
print('Матрица:', result3)
