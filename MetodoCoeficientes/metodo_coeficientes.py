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
    def calculate_determinant(matrix):
        # Convertimos la lista en un array de numpy para facilitar las operaciones
        a = np.array(matrix)
        return np.linalg.det(a)

