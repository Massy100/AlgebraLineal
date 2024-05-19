import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
import math
from mpl_toolkits.mplot3d import Axes3D

import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

class VentanaMagnitud(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("VentanaMagnitud")
        self.geometry("800x600")
        self.parent = parent

        # Variables para almacenar el número de vectores
        self.num_vectores = tk.IntVar()

        # Etiqueta y campo para el número de vectores
        self.label_num_vectores = tk.Label(self, text="Número de vectores:")
        self.label_num_vectores.pack(pady=5)
        self.entry_num_vectores = tk.Entry(self, textvariable=self.num_vectores)
        self.entry_num_vectores.pack(pady=5)

        # Botón para confirmar y crear los campos de texto
        self.btn_confirmar = tk.Button(self, text="Confirmar", command=self.crear_campos_texto)
        self.btn_confirmar.pack(pady=10)

        # Marco para contener los campos de texto de los vectores
        self.marco_vectores = tk.Frame(self)
        self.marco_vectores.pack(pady=10)

        # Botones para calcular, graficar y limpiar
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.pack(pady=10)
        self.btn_graficar = tk.Button(self, text="Graficar", command=self.graficar)
        self.btn_graficar.pack(pady=10)
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

        self.entradas_magnitud = []
        self.entradas_angulo = []
        self.operaciones = []

        # Crear campos de texto para cada vector
        for i in range(num_vectores):
            tk.Label(self.marco_vectores, text=f"Vector {i+1}").grid(row=i, column=0, padx=5, pady=5)
            tk.Label(self.marco_vectores, text="Magnitud:").grid(row=i, column=1, padx=5, pady=5)
            entrada_magnitud = tk.Entry(self.marco_vectores)
            entrada_magnitud.grid(row=i, column=2, padx=5, pady=5)
            self.entradas_magnitud.append(entrada_magnitud)

            tk.Label(self.marco_vectores, text="Ángulo:").grid(row=i, column=3, padx=5, pady=5)
            entrada_angulo = tk.Entry(self.marco_vectores)
            entrada_angulo.grid(row=i, column=4, padx=5, pady=5)
            self.entradas_angulo.append(entrada_angulo)
            
            combobox = ttk.Combobox(self.marco_vectores, values=["+", "-"])
            combobox.set("+")
            combobox.grid(row=i, column=5, padx=5, pady=5)
            self.operaciones.append(combobox)

    def calcular(self):
        try:
            num_vectores = self.num_vectores.get()
            resultado_x = 0
            resultado_y = 0
            procedimiento = ""

            for i in range(num_vectores):
                magnitud = float(self.entradas_magnitud[i].get())
                angulo = float(self.entradas_angulo[i].get())
                signo = self.operaciones[i].get()

                x = magnitud * math.cos(math.radians(angulo))
                y = magnitud * math.sin(math.radians(angulo))

                if signo == "+":
                    resultado_x += x
                    resultado_y += y
                    procedimiento += f"({magnitud} * cos({angulo}) + {magnitud} * sin({angulo})) + "
                elif signo == "-":
                    resultado_x -= x
                    resultado_y -= y
                    procedimiento += f"({magnitud} * cos({angulo}) - {magnitud} * sin({angulo})) - "

            resultado_x = round(resultado_x, 2)
            resultado_y = round(resultado_y, 2)
            procedimiento = procedimiento.rstrip(" + -") + f" = ({resultado_x}, {resultado_y})\n"

            magnitud_resultante = math.sqrt(resultado_x**2 + resultado_y**2)
            angulo_resultante = math.degrees(math.atan2(resultado_y, resultado_x))

            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, f"Procedimiento:\n{procedimiento}\n")
            self.text_resultado.insert(tk.END, f"Resultado:\n({resultado_x}, {resultado_y})\n")
            self.text_resultado.insert(tk.END, f"Magnitud resultante: {magnitud_resultante:.2f}\n")
            self.text_resultado.insert(tk.END, f"Ángulo resultante: {angulo_resultante:.2f}°")

            self.resultado_x = resultado_x
            self.resultado_y = resultado_y

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def graficar(self):
        try:
            x = self.resultado_x
            y = self.resultado_y
            magnitud = math.sqrt(x**2 + y**2)
            angulo = math.degrees(math.atan2(y, x))

            # Crear la gráfica del vector resultado en 2D
            plt.figure()
            plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='r', width=0.005)
            plt.xlim(-magnitud - 1, magnitud + 1)
            plt.ylim(-magnitud - 1, magnitud + 1)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Vector Resultado")
            plt.grid()
            plt.text(x, y, f"({x:.2f}, {y:.2f})\nMagnitud: {magnitud:.2f}\nÁngulo: {angulo:.2f}°", fontsize=8, ha='right')
            plt.show()

        except AttributeError:
            messagebox.showerror("Error", "Calcule el resultado antes de graficar.")
        except NotImplementedError as e:
            messagebox.showerror("Error", str(e))

    def limpiar_texto(self):
        self.text_resultado.delete(1.0, tk.END)

    def regresar(self):
        self.destroy()
        self.parent.deiconify()