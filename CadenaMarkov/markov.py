import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import numpy as np
import matplotlib.pyplot as plt

class CadenaMarkov:
    def __init__(self, matriz):
        self.matriz = matriz
        self.matriz_trasponer = self.transpose(matriz)

    def transpose(self, matriz):
        return [list(i) for i in zip(*matriz)]

    def multiplicar_matrices(self, condiciones_iniciales, veces):
        resultados = []
        condiciones_iniciales_array = [[float(x)] for x in condiciones_iniciales.split()]
        resultado = self.multiply_matrices(self.matriz_trasponer, condiciones_iniciales_array)
        resultados.append(resultado)
        for _ in range(veces - 1):
            resultado = self.multiply_matrices(self.matriz_trasponer, resultado)
            resultados.append(resultado)
        return resultados

    def multiply_matrices(self, a, b):
        return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
        
    def crear_matriz(self, filas, columnas):
        matriz = []
        print(f"Ingresando valores para la matriz de {filas}x{columnas}:")
        for i in range(filas):
            fila_actual = []
            for j in range(columnas):
                valor = float(input(f"Ingresa el valor para el elemento [{i + 1}, {j + 1}]: "))
                fila_actual.append(valor)
            matriz.append(fila_actual)
        return np.array(matriz)

    def realizar_multiplicaciones(self, condiciones_iniciales, veces):
        condiciones_iniciales_array = np.array([[float(numero)] for numero in condiciones_iniciales.split()])
        resultado = self.multiplicar_matrices(self.matriz_trasponer, condiciones_iniciales_array)

        resultados = [resultado.flatten()]
        for _ in range(veces - 1):
            resultado = self.multiplicar_matrices(self.matriz_trasponer, resultado)
            resultados.append(resultado.flatten())
        return resultados




