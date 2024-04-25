def create_matrix(rows, cols):
    matrix = []
    for x in range(rows):
        row = []
        for y in range(cols):
            entry = float(input(f'Ingresa en la casilla {x + 1},{y + 1}: '))
            row.append(entry)
        matrix.append(row)

    for row in matrix:
        print(row)
    return matrix


def multiply_matrices(rows, cols, m1, m2):
    result_matrix = []
    for i in range(rows):
        result_row = []
        for j in range(cols):
            cell_sum = 0
            for k in range(len(m2)):
                cell_sum += m1[i][k] * m2[k][j]
            result_row.append(cell_sum)
        result_matrix.append(result_row)

    print('\nResultado de la multiplicación:')
    for row in result_matrix:
        print(row)
    return result_matrix


def print_multiplication_process(rows, cols, m1, m2):
    expression_matrix = []
    for i in range(rows):
        expression_row = []
        for j in range(cols):
            expression = ''
            for k in range(len(m2)):
                expression += f'({m1[i][k]} * {m2[k][j]})'
                if k != len(m2) - 1:
                    expression += ' + '
            expression_row.append(expression)
        expression_matrix.append(expression_row)

    print('\nExpresiones de la multiplicación:')
    for row in expression_matrix:
        print(row)
    return expression_matrix


def main():
    x1 = int(input('Cuantas filas tiene la matriz 1: '))
    y1 = int(input('Cuantas columnas tiene la matriz 1: '))
    x2 = int(input('Cuantas filas tiene la matriz 2: '))
    y2 = int(input('Cuantas columnas tiene la matriz 2: '))
    if y1 == x2:
        matrix1 = create_matrix(x1, y1)
        matrix2 = create_matrix(x2, y2)
        print_multiplication_process(x1, y2, matrix1, matrix2)
        multiply_matrices(x1, y2, matrix1, matrix2)
    else:
        print('No es posible multiplicar las matrices porque el número de columnas de la primera no coincide con el número de filas de la segunda.')

main()
