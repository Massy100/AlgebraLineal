matriz = [[19, 15, 12],
          [3, 11, 15],
          [15, 2, 19]]

identidad = [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]]


def div_matriz(matriz_ex, cant):
    new_matriz = []
    for i in matriz_ex:
        new_matriz.append(i / cant)
    return new_matriz


def mult_matriz(matriz_ex, cant):
    new_matriz = []
    for i in matriz_ex:
        new_matriz.append(i * cant)
    return new_matriz


def restar_matriz(matriz1, matriz2, sign):
    new_matrix = []
    for i in range(len(matriz1)):
        print(matriz1[i], matriz2[i], matriz1[i] + matriz2[i])
        new_matrix.append(float(format(matriz1[i] * sign + matriz2[i], '.4f')))
    return new_matrix


identidad[2] = restar_matriz(mult_matriz(identidad[0], matriz[2][0] / matriz[0][0]), identidad[2], -1)
matriz[2] = restar_matriz(mult_matriz(matriz[0], matriz[2][0] / matriz[0][0]), matriz[2], -1)
print(matriz)
print(identidad, '\n')

identidad[1] = restar_matriz(mult_matriz(identidad[0], matriz[1][0] / matriz[0][0]), identidad[1], -1)
matriz[1] = restar_matriz(mult_matriz(matriz[0], matriz[1][0] / matriz[0][0]), matriz[1], -1)
print(matriz)
print(identidad, '\n')

identidad[2] = restar_matriz(mult_matriz(identidad[1], matriz[2][1] / matriz[1][1]), identidad[2], -1)
matriz[2] = restar_matriz(mult_matriz(matriz[1], matriz[2][1] / matriz[1][1]), matriz[2], -1)

print(matriz)
print(identidad, '\n')

identidad[0] = restar_matriz(mult_matriz(identidad[2], matriz[0][2] / matriz[2][2]), identidad[0], -1)
matriz[0] = restar_matriz(mult_matriz(matriz[2], matriz[0][2] / matriz[2][2]), matriz[0], -1)

print(matriz)
print(identidad, '\n')

identidad[1] = restar_matriz(mult_matriz(identidad[2], matriz[1][2] / matriz[2][2]), identidad[1], -1)
matriz[1] = restar_matriz(mult_matriz(matriz[2], matriz[1][2] / matriz[2][2]), matriz[1], -1)

print(matriz)
print(identidad, '\n')

identidad[0] = restar_matriz(mult_matriz(identidad[1], matriz[0][1] / matriz[1][1]), identidad[0], -1)
matriz[0] = restar_matriz(mult_matriz(matriz[1], matriz[0][1] / matriz[1][1]), matriz[0], -1)

print(matriz)
print(identidad, '\n')

identidad[2] = div_matriz(identidad[2], matriz[2][2])
matriz[2] = div_matriz(matriz[2], matriz[2][2])

print(matriz)
print(identidad, '\n')

identidad[1] = div_matriz(identidad[1], matriz[1][1])
matriz[1] = div_matriz(matriz[1], matriz[1][1])

print(matriz)
print(identidad, '\n')

identidad[0] = div_matriz(identidad[0], matriz[0][0])
matriz[0] = div_matriz(matriz[0], matriz[0][0])

print(matriz)
print(identidad, '\n')
