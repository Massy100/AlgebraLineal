import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
import math
from OperacionesConVectores import vector_por_grados

class VentanaPuntoVectores(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ventana Producto Punto")
        self.geometry("800x600")
        self.parent = parent

        # Variables para almacenar el número de vectores y las dimensiones
        self.num_vectores = tk.IntVar()
        self.dimensiones = tk.IntVar()

        # Etiqueta y campo para el número de vectores
        self.label_num_vectores = tk.Label(self, text="Número de vectores:")
        self.label_num_vectores.pack(pady=5)
        self.entry_num_vectores = tk.Entry(self, textvariable=self.num_vectores)
        self.entry_num_vectores.pack(pady=5)

        # Etiqueta y campo para las dimensiones de los vectores
        self.label_dimensiones = tk.Label(self, text="Dimensiones de los vectores:")
        self.label_dimensiones.pack(pady=5)
        self.entry_dimensiones = tk.Entry(self, textvariable=self.dimensiones)
        self.entry_dimensiones.pack(pady=5)

        # Botón para confirmar y crear los campos de texto
        self.btn_confirmar = tk.Button(self, text="Confirmar", command=self.crear_campos_texto)
        self.btn_confirmar.pack(pady=10)

        # Marco para contener los campos de texto de los vectores
        self.marco_vectores = tk.Frame(self)
        self.marco_vectores.pack(pady=10)

        # Botones para calcular y limpiar
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.pack(pady=10)
        self.btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar_texto)
        self.btn_limpiar.pack(pady=10)

        # Botón para regresar
        self.btn_regresar = tk.Button(self, text="Regresar", command=self.regresar)
        self.btn_regresar.pack(pady=10)

        # Texto para mostrar el procedimiento y resultado
        self.text_resultado = tk.Text(self, height=10, width=80)
        self.text_resultado.pack(pady=10)

    def crear_campos_texto(self):
        # Limpiar el marco de vectores antes de crear nuevos campos
        for widget in self.marco_vectores.winfo_children():
            widget.destroy()

        num_vectores = self.num_vectores.get()
        dimensiones = self.dimensiones.get()

        self.entradas = []

        # Crear etiquetas de componentes
        for j in range(dimensiones):
            tk.Label(self.marco_vectores, text=f"d{j+1}").grid(row=j+1, column=0, padx=5, pady=2)

        # Crear campos de texto para cada vector
        for i in range(num_vectores):
            tk.Label(self.marco_vectores, text=f"Vector {i+1}").grid(row=0, column=i+1, padx=5, pady=5)

            componentes = []
            for j in range(dimensiones):
                entry = tk.Entry(self.marco_vectores)
                entry.grid(row=j+1, column=i+1, padx=5, pady=2)
                componentes.append(entry)
            self.entradas.append(componentes)

    def calcular(self):
        try:
            dimensiones = self.dimensiones.get()
            num_vectores = self.num_vectores.get()

            if num_vectores < 2:
                raise ValueError("Debe haber al menos dos vectores para calcular el producto punto.")

            # Inicializar el resultado del producto punto
            resultado = 0

            # Inicializar la variable para el procedimiento
            procedimiento = "Procedimiento:\n"

            # Calcular el producto punto
            for j in range(dimensiones):
                producto_parcial = 1
                procedimiento += f"d{j+1}: "
                for i in range(num_vectores):
                    valor = float(self.entradas[i][j].get())
                    producto_parcial *= valor
                    procedimiento += f"{valor} * "

                procedimiento = procedimiento.rstrip(" * ") + f"= {producto_parcial}\n"
                resultado += producto_parcial

            procedimiento += f"\nResultado final: {resultado}"

            # Mostrar el procedimiento y resultado
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, procedimiento)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def limpiar_texto(self):
        self.text_resultado.delete(1.0, tk.END)

    def regresar(self):
        self.destroy()
        self.parent.deiconify()
    