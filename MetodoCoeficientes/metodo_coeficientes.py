class DeterminanteMatriz:
    def __init__(self, fila1, fila2, fila3):
        self.fila1 = fila1
        self.fila2 = fila2
        self.fila3 = fila3

    def calcular_determinante(self):
        print(f'Columna 1: {self.fila1} '
              f'Columna 2: {self.fila2} '
              f'Columna 3: {self.fila3}')
        
        suma = (self.fila1[0] * self.fila2[1] * self.fila3[2] +
                self.fila2[0] * self.fila3[1] * self.fila1[2] +
                self.fila3[0] * self.fila1[1] * self.fila2[2])
        
        resta = (self.fila1[2] * self.fila2[1] * self.fila3[0] +
                 self.fila2[2] * self.fila3[1] * self.fila1[0] +
                 self.fila3[2] * self.fila1[1] * self.fila2[0])
        
        determinante = suma - resta

        print(f'({suma}) - ({resta})')
        print(f'{suma} - {resta}')
        print(determinante)

        return determinante
  
import numpy as np

class MatrixOperations:
    @staticmethod
    def get_minor(matrix, i, j):
        return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

    @staticmethod
    def calculate_determinant(matrix, depth=0):
        details = []
        if len(matrix) == 1:
            details.append(f"Determinante de {matrix} es {matrix[0][0]}")
            return matrix[0][0], details
        if len(matrix) == 2:
            result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            details.append(f"Determinante de {matrix} es {result}")
            return result, details
        determinant = 0
        for c in range(len(matrix)):
            minor = MatrixOperations.get_minor(matrix, 0, c)
            cofactor, cofactor_details = MatrixOperations.calculate_determinant(minor, depth + 1)
            sign = (-1) ** c
            determinant += sign * matrix[0][c] * cofactor
            details.extend(cofactor_details)
            details.append(f"m[0][{c}]={matrix[0][c]}, cofactor={cofactor}, sign={sign}, partial det={determinant}")
        details.append(f"Determinante de {matrix} es {determinant}")
        return determinant, details



