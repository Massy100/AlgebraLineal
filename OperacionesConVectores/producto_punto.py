import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
import math


def crear_grafico():
    def crear_vectores():
        for i in range(1, len(entries) + 1):
            entry = ttk.Label(root, text="")
            entry.grid(row=i, column=1, padx=5, pady=5)
        for i in entries:
            i[0].destroy()
            i[1].destroy()
            i[2].destroy()
        entries.clear()
        try:
            entry = ttk.Label(root, text="X")
            entry.grid(row=0, column=2, padx=5, pady=5)

            entry = ttk.Label(root, text="Y")
            entry.grid(row=0, column=3, padx=5, pady=5)

            entry = ttk.Label(root, text="Z")
            entry.grid(row=0, column=4, padx=5, pady=5)

            rows = int(entry_rows.get())
            if rows < -1:
                rows *= -1
                muestra.set("No te procupes,\n yo lo hago positivo")
            if rows <= 1:
                rows = 2
                muestra.set("Amigo, minimo 2,\n yo me encargo.")
            cols = 3
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
            print(matriz)
        except(Exception):
            messagebox.showerror("Error", "Cada valor debe ser un numero.")
        texto, x, y, z = crear_texto()
        muestra.set(str(texto))


    def crear_texto():
        x = 0
        y = 0
        z = 0
        texto = 'Procedimiento:\n1. Multiplicar todas las X:\n'
        for i in entries:
            x += float(i[0].get())
            texto = texto + str(i[0].get()) + ' * '
        texto = texto[:-3]

        texto = texto + f'= {x}\n2. Multiplicar todas las Y:\n'

        for i in entries:
            y += float(i[1].get())
            texto = texto + str(i[1].get()) + ' * '
        texto = texto[:-3]

        texto = texto + f'= {y}\n3. Multiplicar todas las Z:\n'

        for i in entries:
            z += float(i[2].get())
            texto = texto + str(i[2].get()) + ' * '
        texto = texto[:-3]

        texto = texto + f'= {z}\n4. Finalmente nos queda \nX: {x} Y: {y} Z: {z}\n y se suman:\n quedando: {x} + {y} + {z}\nTotal: {x + y + z}'
        return texto, x, y, z


    entries = []

    root = tk.Tk()
    root.title("Matriz en Tkinter")

    entry = ttk.Label(root, text="Cantidad de vectores a aplicar")
    entry.grid(row=0, column=0, padx=5, pady=5)

    entry_rows = ttk.Entry(root, width=5)
    entry_rows.grid(row=1, column=0, padx=5, pady=10)

    boton_operar = ttk.Button(root, text="Cantidad de vectores a aplicar", command=crear_vectores)
    boton_operar.grid(row=2, column=0, padx=5, pady=5)

    boton_operar2 = ttk.Button(root, text="Obtener Valores", command=obtener_valores)
    boton_operar2.grid(row=3, column=0, padx=5, pady=5)

    muestra = tk.StringVar()
    muestra.set(f"")

    new_label = ttk.Label(root, textvariable=muestra)
    new_label.grid(row=4, column=0, padx=5, pady=5)




    root.mainloop()
crear_grafico()