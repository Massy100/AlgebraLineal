class MatrixMultiplication:
    def __init__(self):
        pass

    def create_matrix(self, rows, cols):
        matrix = []
        print(f"Ingrese los valores para una matriz de {rows}x{cols}")
        for x in range(rows):
            row = []
            for y in range(cols):
                entry = float(input(f'Ingresa en la casilla {x + 1},{y + 1}: '))
                row.append(entry)
            matrix.append(row)
        return matrix

    def multiply_matrices(self, m1, m2):
        rows = len(m1)
        cols = len(m2[0])
        if len(m1[0]) != len(m2):
            raise ValueError("El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda.")

        result_matrix = []
        for i in range(rows):
            result_row = []
            for j in range(cols):
                cell_sum = 0
                for k in range(len(m2)):
                    cell_sum += m1[i][k] * m2[k][j]
                result_row.append(cell_sum)
            result_matrix.append(result_row)
        return result_matrix

    def print_multiplication_process(self, m1, m2):
        rows = len(m1)
        cols = len(m2[0])
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
        return expression_matrix

    def execute(self):
        x1 = int(input('Cuantas filas tiene la matriz 1: '))
        y1 = int(input('Cuantas columnas tiene la matriz 1: '))
        x2 = int(input('Cuantas filas tiene la matriz 2: '))
        y2 = int(input('Cuantas columnas tiene la matriz 2: '))

        if y1 != x2:
            print('No es posible multiplicar las matrices porque el número de columnas de la primera no coincide con el número de filas de la segunda.')
            return

        matrix1 = self.create_matrix(x1, y1)
        matrix2 = self.create_matrix(x2, y2)

        expressions = self.print_multiplication_process(matrix1, matrix2)
        print('\nExpresiones de la multiplicación:')
        for row in expressions:
            print(row)

        result = self.multiply_matrices(matrix1, matrix2)
        print('\nResultado de la multiplicación:')
        for row in result:
            print(row)


