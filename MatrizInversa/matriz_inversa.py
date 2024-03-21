class MatrizInversa:
    
    def __init__(self, matriz):
        self.matriz = matriz

    matriz = [[19, 15, 12],
            [3, 11, 15],
            [15, 2, 19]]

    identidad = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]

    def imprecion(matriz1, matriz2, cant, lugar):
        if lugar == 0:
            print(f'{matriz1[0]} \t\t\t| {matriz2[0]} * {cant}\n'
                f'{matriz1[1]} \t\t\t| {matriz2[1]}\n'
                f'{matriz1[2]} \t\t\t| {matriz2[2]}\n')
        elif lugar == 1:
            print(f'{matriz1[0]} \t\t\t| {matriz2[0]}\n'
                f'{matriz1[1]} \t\t\t| {matriz2[1]} * {cant}\n'
                f'{matriz1[2]} \t\t\t| {matriz2[2]}\n')
        elif lugar == 2:
            print(f'{matriz1[0]} \t\t\t| {matriz2[0]}\n'
                f'{matriz1[1]} \t\t\t| {matriz2[1]}\n'
                f'{matriz1[2]} \t\t\t| {matriz2[2]} * {cant}\n')
        elif lugar == 4:
            print(f'{matriz1[0]} \t\t\t| {matriz2[0]}\n'
                f'{matriz1[1]} \t\t\t| {matriz2[1]}\n'
                f'{matriz1[2]} \t\t\t| {matriz2[2]} / {cant}\n')
        elif lugar == 5:
            print(f'{matriz1[0]} \t\t\t| {matriz2[0]}\n'
                f'{matriz1[1]} \t\t\t| {matriz2[1]} / {cant}\n'
                f'{matriz1[2]} \t\t\t| {matriz2[2]}\n')
        elif lugar == 6:
            print(f'{matriz1[0]} \t\t\t| {matriz2[0]} / {cant}\n'
                f'{matriz1[1]} \t\t\t| {matriz2[1]}\n'
                f'{matriz1[2]} \t\t\t| {matriz2[2]}\n')
        else:
            print(f'{matriz1[0]} \t\t\t| {matriz2[0]}\n'
                f'{matriz1[1]} \t\t\t| {matriz2[1]}\n'
                f'{matriz1[2]} \t\t\t| {matriz2[2]}\n')

    def div_matriz(matriz_ex, cant):
        new_matriz = []
        for i in matriz_ex:
            new_matriz.append(float(format(i / cant, '.4f')))
        return new_matriz


    def mult_matriz(matriz_ex, cant):
        new_matriz = []
        for i in matriz_ex:
            new_matriz.append(i * cant)
        return new_matriz


    def restar_matriz(matriz1, matriz2, sign):
        new_matrix = []
        for i in range(len(matriz1)):
            new_matrix.append(float(format(matriz1[i] * sign + matriz2[i], '.4f')))
        return new_matrix


    imprecion(matriz, identidad, -matriz[2][0] / matriz[0][0], 0)

    identidad[2] = restar_matriz(mult_matriz(identidad[0], matriz[2][0] / matriz[0][0]), identidad[2], -1)
    matriz[2] = restar_matriz(mult_matriz(matriz[0], matriz[2][0] / matriz[0][0]), matriz[2], -1)

    imprecion(matriz, identidad, -matriz[1][0] / matriz[0][0], 3)
    imprecion(matriz, identidad, -matriz[1][0] / matriz[0][0], 0)

    identidad[1] = restar_matriz(mult_matriz(identidad[0], matriz[1][0] / matriz[0][0]), identidad[1], -1)
    matriz[1] = restar_matriz(mult_matriz(matriz[0], matriz[1][0] / matriz[0][0]), matriz[1], -1)

    imprecion(matriz, identidad, -matriz[2][1] / matriz[1][1], 3)
    imprecion(matriz, identidad, -matriz[2][1] / matriz[1][1], 1)

    identidad[2] = restar_matriz(mult_matriz(identidad[1], matriz[2][1] / matriz[1][1]), identidad[2], -1)
    matriz[2] = restar_matriz(mult_matriz(matriz[1], matriz[2][1] / matriz[1][1]), matriz[2], -1)

    imprecion(matriz, identidad, -matriz[0][2] / matriz[2][2], 3)
    imprecion(matriz, identidad, -matriz[0][2] / matriz[2][2], 2)

    identidad[0] = restar_matriz(mult_matriz(identidad[2], matriz[0][2] / matriz[2][2]), identidad[0], -1)
    matriz[0] = restar_matriz(mult_matriz(matriz[2], matriz[0][2] / matriz[2][2]), matriz[0], -1)

    imprecion(matriz, identidad, -matriz[1][2] / matriz[2][2], 3)
    imprecion(matriz, identidad, -matriz[1][2] / matriz[2][2], 2)

    identidad[1] = restar_matriz(mult_matriz(identidad[2], matriz[1][2] / matriz[2][2]), identidad[1], -1)
    matriz[1] = restar_matriz(mult_matriz(matriz[2], matriz[1][2] / matriz[2][2]), matriz[1], -1)

    imprecion(matriz, identidad, -matriz[0][1] / matriz[1][1], 3)
    imprecion(matriz, identidad, -matriz[0][1] / matriz[1][1], 1)

    identidad[0] = restar_matriz(mult_matriz(identidad[1], matriz[0][1] / matriz[1][1]), identidad[0], -1)
    matriz[0] = restar_matriz(mult_matriz(matriz[1], matriz[0][1] / matriz[1][1]), matriz[0], -1)

    imprecion(matriz, identidad, -matriz[0][1] / matriz[1][1], 3)
    imprecion(matriz, identidad, matriz[2][2], 4)

    identidad[2] = div_matriz(identidad[2], matriz[2][2])
    matriz[2] = div_matriz(matriz[2], matriz[2][2])

    imprecion(matriz, identidad, matriz[2][2], 3)
    imprecion(matriz, identidad, matriz[1][1], 5)

    identidad[1] = div_matriz(identidad[1], matriz[1][1])
    matriz[1] = div_matriz(matriz[1], matriz[1][1])

    imprecion(matriz, identidad, matriz[0][0], 3)
    imprecion(matriz, identidad, matriz[0][0], 6)

    identidad[0] = div_matriz(identidad[0], matriz[0][0])
    matriz[0] = div_matriz(matriz[0], matriz[0][0])

    imprecion(matriz, identidad, matriz[0][0], 3)

    print('Matriz inversa: ', identidad)

