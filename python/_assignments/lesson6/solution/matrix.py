def generate_matrix(value, shape):
    matrix = []
    for i in range(shape[0]):
        matrix.append([])
        for j in range(shape[1]):
            matrix[i].append(value)

    return matrix


shape = (3, 10)
value = 5

generate_matrix(value, shape)

generate_matrix(5, (3, 10))

# named paramenter
generate_matrix(5, shape=(3, 10))
generate_matrix(value=5, shape=(3, 10))
