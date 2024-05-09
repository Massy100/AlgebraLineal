class MatrizInversa:
    def __init__(self, matriz):
        self.matriz = [list(map(float, fila)) for fila in matriz]
        self.identidad = [[float(i == j) for j in range(len(matriz))] for i in range(len(matriz))]
        self.detalles = []  # Almacenará los detalles de cada paso

    def calcular_inversa(self):
        n = len(self.matriz)
        for i in range(n):
            if self.matriz[i][i] == 0:
                # Buscar un buen pivote en la columna i debajo de la fila i
                for k in range(i+1, n):
                    if self.matriz[k][i] != 0:
                        # Intercambiar las filas i y k
                        self.matriz[i], self.matriz[k] = self.matriz[k], self.matriz[i]
                        self.identidad[i], self.identidad[k] = self.identidad[k], self.identidad[i]
                        self.registrar_operacion(k, i, "Intercambio de filas para pivote")
                        break
                else:
                    raise ValueError("La matriz no es invertible debido a una columna de ceros.")

            # Normalizar la fila i para que el elemento diagonal sea 1
            factor = self.matriz[i][i]
            self.registrar_operacion(i, factor, "Normalizando")
            for j in range(n):
                self.matriz[i][j] /= factor
                self.identidad[i][j] /= factor
            
            # Hacer cero los otros elementos en la columna i
            for k in range(n):
                if k != i:
                    factor = self.matriz[k][i]
                    self.registrar_operacion(k, factor, f"Eliminando {factor} de la fila {k}")
                    for j in range(n):
                        self.matriz[k][j] -= factor * self.matriz[i][j]
                        self.identidad[k][j] -= factor * self.identidad[i][j]
        return self.identidad

    def registrar_operacion(self, fila, factor, descripcion):
        operacion = f"Fila {fila}: {descripcion} por {factor:.2f}"
        self.detalles.append(operacion)



