def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


rezult1 = get_matrix(2, 2, 10)
rezult2 = get_matrix(3, 5, 42)
rezult3 = get_matrix(4, 2, 13)
print(rezult1)
print(rezult2)
print(rezult3)
