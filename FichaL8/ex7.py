def multiplica_mat(matriz1, matriz2):
    return [[sum([matriz1[i][k] * matriz2[k][j] for k in range(len(matriz1[0]))]) for j in range(len(matriz2[0]))] for i in range(len(matriz1))]


print(multiplica_mat([[1,2], [3,4]], [[3,5],[4,2]]))