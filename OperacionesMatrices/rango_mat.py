import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math

import texto_rango

def crear_grafico():
    def crear_vectores():
        print(entries)
        for i in range(1, len(entries) + 1):
            entry = ttk.Label(root, text="")
            entry.grid(row=i, column=1, padx=5, pady=5)
            entry = ttk.Label(root, text="")
            entry.grid(row=0, column=i + 1, padx=5, pady=5)
        for i in entries:
            for y in range(len(entries[-1])):
                i[y].destroy()

        entries.clear()
        try:

            rows = int(entry_rows.get())
            if rows < -1:
                rows *= -1
                muestra.set("No te procupes,\n yo lo hago positivo")
            if rows <= 1:
                rows = 2
                muestra.set("Amigo, minimo 2,\n yo me encargo.")
            cols = int(entry_cols.get())
            if cols < -1:
                cols *= -1
                muestra.set("No te procupes,\n yo lo hago positivo")
            if cols <= 1:
                cols = 2
                muestra.set("Amigo, minimo 2,\n yo me encargo.")
            for i in range(2, cols + 2):
                entry = ttk.Label(root, text=i - 1)
                entry.grid(row=0, column=i, padx=5, pady=5)
            for i in range(1, rows + 1):
                entry = ttk.Label(root, text=i)
                entry.grid(row=i, column=1, padx=5, pady=5)
            for i in range(1, rows + 1):
                row_entries = []
                for j in range(2, cols + 2):
                    entry = ttk.Entry(root, width=5)
                    entry.grid(row=i, column=j, padx=5, pady=5)
                    row_entries.append(entry)
                entries.append(row_entries)
        except(Exception):
            messagebox.showerror("Error", "Valor no ingresado.")

    def obtener_valores():
        try:
            matriz = []
            for row_entries in entries:
                fila = []
                for entry in row_entries:
                    valor = float(entry.get())
                    fila.append(valor)
                matriz.append(fila)
            texto = encontrar_rango_procedimiento(matriz)
            #muestra.set(str(texto))
            texto_rango.main(texto)
        except(Exception):
            messagebox.showerror("Error", "Cada valor debe ser un numero.")


    def print_matrix(matrix):
        texto = ''
        for row in matrix:
            texto += (' '.join(f'{num:.2f}' for num in row))
            texto += '\n'
        return texto

    def encontrar_rango_procedimiento(matriz):

        texto = ''

        matriz_np = np.array(matriz, dtype=float)

        filas, columnas = matriz_np.shape
        texto += "Matriz inicial:\n"
        texto += print_matrix(matriz_np)

        fila_actual = 0
        for col in range(columnas):
            if fila_actual >= filas:
                break

            max_fila = fila_actual + np.argmax(np.abs(matriz_np[fila_actual:, col]))

            if matriz_np[max_fila, col] != 0:
                matriz_np[[fila_actual, max_fila]] = matriz_np[[max_fila, fila_actual]]
                texto += f"Intercambio fila {fila_actual} con fila {max_fila}:\n"
                texto += print_matrix(matriz_np)

                matriz_np[fila_actual] = matriz_np[fila_actual] / matriz_np[fila_actual, col]
                texto += f"Normalización de fila {fila_actual}:\n"
                texto += print_matrix(matriz_np)

                for i in range(fila_actual + 1, filas):
                    matriz_np[i] -= matriz_np[i, col] * matriz_np[fila_actual]
                    texto += f"Eliminación en fila {i} usando fila {fila_actual}:\n"
                    texto += print_matrix(matriz_np)

                fila_actual += 1

        rango = sum(np.any(row != 0) for row in matriz_np)
        texto += f"Matriz en forma escalonada:\n"
        texto += print_matrix(matriz_np)
        texto += f"\nRango: {rango}\n"

        return texto


    entries = []

    root = tk.Tk()
    root.title("Matriz en Tkinter")

    entry = ttk.Label(root, text="Cantidad de Filas")
    entry.grid(row=0, column=0, padx=5, pady=5)

    entry_rows = ttk.Entry(root, width=5)
    entry_rows.grid(row=1, column=0, padx=5, pady=10)

    entry = ttk.Label(root, text="Cantidad de Columnas")
    entry.grid(row=2, column=0, padx=5, pady=5)

    entry_cols = ttk.Entry(root, width=5)
    entry_cols.grid(row=3, column=0, padx=5, pady=10)

    boton_operar = ttk.Button(root, text="Insertar Datos", command=crear_vectores)
    boton_operar.grid(row=4, column=0, padx=5, pady=5)

    boton_operar2 = ttk.Button(root, text="Obtener Resultado", command=obtener_valores)
    boton_operar2.grid(row=5, column=0, padx=5, pady=5)

    muestra = tk.StringVar()
    muestra.set(f"")

    new_label = ttk.Label(root, textvariable=muestra)
    new_label.grid(row=6, column=0, padx=5, pady=5)







    root.mainloop()
crear_grafico()