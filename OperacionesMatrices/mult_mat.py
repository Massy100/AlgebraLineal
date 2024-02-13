def creat_matrix(x_can, y_can):
    matris = []
    for x in range(x_can):
        fila = []
        for y in range(y_can):
            columna = int(input(f'Ingresa en la casilla {x + 1},{y + 1}: '))
            fila.append(columna)
        matris.append(fila)

    for fil in matris:
        print(fil)
    return matris


def operar_matrix(x1, y2, m1, m2):
    matris = []
    for x2 in range(x1):
        fila = []
        for x in range(x1):
            columna = 0
            for y in range(y2):
                columna += m1[x2][y] * m2[y][x]
            fila.append(columna)
        matris.append(fila)
    print('\nMatris:')
    for fil in matris:
        print(fil)
    return matris


def imprimir_matrix(x1, y2, m1, m2):
    matris = []
    for x2 in range(x1):
        fila = []
        for x in range(x1):
            columna = str()
            for y in range(y2):
                columna += '(' + str(m1[x2][y]) + ' * ' + str(m2[y][x]) + ')'
                if y != y2 - 1:
                    columna += ' + '
            fila.append(columna)
        matris.append(fila)
    print('\nMatris:')
    for fil in matris:
        print(fil)
    return matris


def main():
    x1 = int(input('Cuantas filas tiene la matriz 1: '))
    y1 = int(input('Cuantas columnas tiene la matriz 1: '))
    x2 = int(input('Cuantas filas tiene la matriz 2: '))
    y2 = int(input('Cuantas columnas tiene la matriz 2: '))
    if y1 == x2:
        matris1 = creat_matrix(x1, y1)
        matris2 = creat_matrix(x2, y2)
        imprimir_matrix(x1, y2, matris1, matris2)
        operar_matrix(x1, y2, matris1, matris2)
    else:
        print('No es posible')


main()