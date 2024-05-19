import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
import math
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class VentanaCruzVectores(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ventana Producto Cruz")
        self.geometry("800x600")
        self.parent = parent

        # Etiquetas para la entrada de vectores
        self.label_vector1 = tk.Label(self, text="Vector 1 (x, y, z):")
        self.label_vector1.grid(row=0, column=0, padx=5, pady=5)
        self.label_vector2 = tk.Label(self, text="Vector 2 (x, y, z):")
        self.label_vector2.grid(row=1, column=0, padx=5, pady=5)

        # Campos de entrada para los vectores
        self.entry_vector1 = tk.Entry(self)
        self.entry_vector1.grid(row=0, column=1, padx=5, pady=5)
        self.entry_vector2 = tk.Entry(self)
        self.entry_vector2.grid(row=1, column=1, padx=5, pady=5)

        # Botones para calcular, graficar y limpiar
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.grid(row=2, column=0, padx=5, pady=5)
        self.btn_graficar = tk.Button(self, text="Graficar", command=self.graficar)
        self.btn_graficar.grid(row=2, column=1, padx=5, pady=5)
        self.btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.grid(row=2, column=2, padx=5, pady=5)

        # Texto para mostrar el procedimiento y resultado
        self.text_resultado = tk.Text(self, height=10, width=80)
        self.text_resultado.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
        
        # Botón para regresar
        self.btn_regresar = tk.Button(self, text="Regresar", command=self.regresar)
        self.btn_regresar.grid(row=2, column=3, padx=5, pady=5)

    def calcular(self):
        try:
            # Obtener los vectores ingresados como cadenas
            vector1_str = self.entry_vector1.get()
            vector2_str = self.entry_vector2.get()

            # Convertir las cadenas de vectores en listas de componentes
            vector1 = [float(x) for x in vector1_str.split(",")]
            vector2 = [float(x) for x in vector2_str.split(",")]

            # Verificar que los vectores tengan tres dimensiones
            if len(vector1) != 3 or len(vector2) != 3:
                raise ValueError("Los vectores deben tener exactamente tres dimensiones.")

            # Calcular el producto cruz
            resultado = np.cross(vector1, vector2)

            # Mostrar el procedimiento y resultado
            procedimiento = f"Procedimiento para el Producto Cruz de {vector1} y {vector2}:\n"
            procedimiento += f"({vector1[1]} * {vector2[2]}) - ({vector1[2]} * {vector2[1]}) = {vector1[1] * vector2[2]} - {vector1[2] * vector2[1]} = {vector1[1] * vector2[2] - vector1[2] * vector2[1]}\n"
            procedimiento += f"({vector1[2]} * {vector2[0]}) - ({vector1[0]} * {vector2[2]}) = {vector1[2] * vector2[0]} - {vector1[0] * vector2[2]} = {vector1[2] * vector2[0] - vector1[0] * vector2[2]}\n"
            procedimiento += f"({vector1[0]} * {vector2[1]}) - ({vector1[1]} * {vector2[0]}) = {vector1[0] * vector2[1]} - {vector1[1] * vector2[0]} = {vector1[0] * vector2[1] - vector1[1] * vector2[0]}\n"
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, procedimiento)
            self.text_resultado.insert(tk.END, f"\nResultado del Producto Cruz: {resultado}\n")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def graficar(self):
        try:
            # Obtener los vectores ingresados como cadenas
            vector1_str = self.entry_vector1.get()
            vector2_str = self.entry_vector2.get()

            # Convertir las cadenas de vectores en listas de componentes
            vector1 = [float(x) for x in vector1_str.split(",")]
            vector2 = [float(x) for x in vector2_str.split(",")]

            # Verificar que los vectores tengan tres dimensiones
            if len(vector1) != 3 or len(vector2) != 3:
                raise ValueError("Los vectores deben tener exactamente tres dimensiones.")

            # Calcular el producto cruz
            resultado = np.cross(vector1, vector2)

            # Graficar el resultado en 3D
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.quiver(0, 0, 0, resultado[0], resultado[1], resultado[2], color='r')
            ax.set_xlim([-1, 1])
            ax.set_ylim([-1, 1])
            ax.set_zlim([-1, 1])
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_title("Producto Cruz de Vectores")
            plt.show()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def limpiar(self):
        self.entry_vector1.delete(0, tk.END)
        self.entry_vector2.delete(0, tk.END)
        self.text_resultado.delete(1.0, tk.END)

    def regresar(self):
        self.destroy()
        self.parent.deiconify()