def creat_matrix(tama):
    matris = []
    for x in range(tama):
        fila = []
        for y in range(tama):
            columna = int(input(f'Ingresa en la casilla {x + 1},{y + 1}: '))
            fila.append(columna)
        matris.append(fila)

    for fil in matris:
        print(fil)
    return matris


def imprimir_operacion(operation, m1, m2, tama):
    matris = []
    for x in range(tama):
        fila = []
        for y in range(tama):
            columna = str(m1[x][y]) + operation + str(m2[x][y])
            fila.append(columna)
        matris.append(fila)
    for fil in matris:
        print(fil)
    return matris


def operar_matris(m1, m2, tama, sig):
    matris = []
    for x in range(tama):
        fila = []
        for y in range(tama):
            columna = m1[x][y] + sig * m2[x][y]
            fila.append(columna)
        matris.append(fila)
    for fil in matris:
        print(fil)
    return matris

def main():
    tama = int(input('Ingresa el tamaño de de las matrices: '))
    print('Primera matriz')
    matris1 = creat_matrix(tama)
    print('Segunda matriz')
    matris2 = creat_matrix(tama)
    select = input('Elige si deseas una suma o una resta (+) (-): ')
    print('Operacion: ')
    if select == '+':
        imprimir_operacion('+', matris1, matris2, tama)
        print('Resultado: ')
        operar_matris(matris1, matris2, tama, 1)
    elif select == '-':
        imprimir_operacion('-', matris1, matris2, tama)
        print('Resultado: ')
        operar_matris(matris1, matris2, tama, -1)


main()