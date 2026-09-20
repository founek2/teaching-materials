a = [[1, 2], [3, 4]]
b = [[1, 2], [3, 4]]


def suma(a, b):
    return a + b


def sum_matrix(matrix1, matrix2):
    # global a
    # a = 1

    result = []

    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix1[0])):
            result[i].append(0)
            # result[0][0] = 3
            #matrix1[i][j] = matrix1[i][j] + matrix2[i][j]
            result[i][j] = suma(matrix1[i][j], matrix2[i][j])

    return result


print(sum_matrix(a, b))
print(sum_matrix(a, b))
assert sum_matrix(a, b) == [[7, 9], [11, 13]]
assert sum_matrix(a, b) == [[7, 9], [11, 13]]
