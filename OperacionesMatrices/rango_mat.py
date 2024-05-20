import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import Toplevel
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math
from OperacionesMatrices import texto_rango

class VentanaRangoMatriz(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.entries = []


        self.title("Matriz en Tkinter")

        self.entry = ttk.Label(self, text="Cantidad de Filas")
        self.entry.grid(row=0, column=0, padx=5, pady=5)

        self.entry_rows = ttk.Entry(self, width=5)
        self.entry_rows.grid(row=1, column=0, padx=5, pady=10)

        self.entry = ttk.Label(self, text="Cantidad de Columnas")
        self.entry.grid(row=2, column=0, padx=5, pady=5)

        self.entry_cols = ttk.Entry(self, width=5)
        self.entry_cols.grid(row=3, column=0, padx=5, pady=10)

        self.boton_operar = ttk.Button(self, text="Insertar Datos", command=self.crear_vectores)
        self.boton_operar.grid(row=4, column=0, padx=5, pady=5)

        self.boton_operar2 = ttk.Button(self, text="Obtener Resultado", command=self.obtener_valores)
        self.boton_operar2.grid(row=5, column=0, padx=5, pady=5)

        self.boton_regresar = ttk.Button(self, text="Regresar", command=self.regresar)
        self.boton_regresar.grid(row=6, column=0, padx=5, pady=5)

        self.muestra = tk.StringVar()
        self.muestra.set(f"")

        self.new_label = ttk.Label(self, textvariable=self.muestra)
        self.new_label.grid(row=7, column=0, padx=5, pady=5)

        self.mainloop()
    def crear_vectores(self):
        print(self.entries)
        for i in range(1, len(self.entries) + 1):
            entry = ttk.Label(self, text="")
            entry.grid(row=i, column=1, padx=5, pady=5)
            entry = ttk.Label(self, text="")
            entry.grid(row=0, column=i + 1, padx=5, pady=5)
        for i in self.entries:
            for y in range(len(self.entries[-1])):
                i[y].destroy()

        self.entries.clear()
        try:

            rows = int(self.entry_rows.get())
            if rows < -1:
                rows *= -1
                self.muestra.set("No te procupes,\n yo lo hago positivo")
            if rows <= 1:
                rows = 2
                self.muestra.set("Amigo, minimo 2,\n yo me encargo.")
            cols = int(self.entry_cols.get())
            if cols < -1:
                cols *= -1
                self.muestra.set("No te procupes,\n yo lo hago positivo")
            if cols <= 1:
                cols = 2
                self.muestra.set("Amigo, minimo 2,\n yo me encargo.")
            for i in range(2, cols + 2):
                entry = ttk.Label(self, text=i - 1)
                entry.grid(row=0, column=i, padx=5, pady=5)
            for i in range(1, rows + 1):
                entry = ttk.Label(self, text=i)
                entry.grid(row=i, column=1, padx=5, pady=5)
            for i in range(1, rows + 1):
                row_entries = []
                for j in range(2, cols + 2):
                    entry = ttk.Entry(self, width=5)
                    entry.grid(row=i, column=j, padx=5, pady=5)
                    row_entries.append(entry)
                self.entries.append(row_entries)
        except(Exception):
            messagebox.showerror("Error", "Valor no ingresado.")

    def obtener_valores(self):
        try:
            matriz = []
            for row_entries in self.entries:
                fila = []
                for entry in row_entries:
                    valor = float(entry.get())
                    fila.append(valor)
                matriz.append(fila)
            texto = self.encontrar_rango_procedimiento(matriz)
            #muestra.set(str(texto))
            texto_rango.main(texto)
        except(Exception):
            messagebox.showerror("Error", "Cada valor debe ser un numero.")


    def print_matrix(self, matrix):
        texto = ''
        for row in matrix:
            texto += (' '.join(f'{num:.2f}' for num in row))
            texto += '\n'
        return texto

    def encontrar_rango_procedimiento(self, matriz):

        texto = ''

        matriz_np = np.array(matriz, dtype=float)

        filas, columnas = matriz_np.shape
        texto += "Matriz inicial:\n"
        texto += self.print_matrix(matriz_np)

        fila_actual = 0
        for col in range(columnas):
            if fila_actual >= filas:
                break

            max_fila = fila_actual + np.argmax(np.abs(matriz_np[fila_actual:, col]))

            if matriz_np[max_fila, col] != 0:
                matriz_np[[fila_actual, max_fila]] = matriz_np[[max_fila, fila_actual]]
                texto += f"Intercambio fila {fila_actual} con fila {max_fila}:\n"
                texto += self.print_matrix(matriz_np)

                matriz_np[fila_actual] = matriz_np[fila_actual] / matriz_np[fila_actual, col]
                texto += f"Normalización de fila {fila_actual}:\n"
                texto += self.print_matrix(matriz_np)

                for i in range(fila_actual + 1, filas):
                    matriz_np[i] -= matriz_np[i, col] * matriz_np[fila_actual]
                    texto += f"Eliminación en fila {i} usando fila {fila_actual}:\n"
                    texto += self.print_matrix(matriz_np)

                fila_actual += 1

        rango = sum(np.any(row != 0) for row in matriz_np)
        texto += f"Matriz en forma escalonada:\n"
        texto += self.print_matrix(matriz_np)
        texto += f"\nRango: {rango}\n"

        return texto

    def regresar(self):
        self.destroy()
        self.parent.deiconify()



