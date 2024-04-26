class MatrizInversa:
    def __init__(self, matriz):
        self.matriz = [list(map(float, fila)) for fila in matriz]
        self.identidad = [[float(i == j) for j in range(len(matriz))] for i in range(len(matriz))]

    def calcular_inversa(self):
        n = len(self.matriz)
        for i in range(n):
            # Hacer el elemento diagonal 1 y los otros elementos en la misma columna 0
            factor = self.matriz[i][i]
            for j in range(n):
                self.matriz[i][j] /= factor
                self.identidad[i][j] /= factor
            for k in range(n):
                if k != i:
                    factor = self.matriz[k][i]
                    for j in range(n):
                        self.matriz[k][j] -= factor * self.matriz[i][j]
                        self.identidad[k][j] -= factor * self.identidad[i][j]
        return self.identidad

# Ejemplo de uso
# mi = MatrizInversa([[1, 2], [3, 4]])
# inversa = mi.calcular_inversa()
# print("Matriz Inversa:", inversa)


