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

class VentanaComponentes(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("VentanaComponentes")
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
        dimensiones = self.dimensiones.get()

        self.entradas = []
        self.operaciones = []

        # Crear etiquetas de componentes
        for j in range(dimensiones):
            tk.Label(self.marco_vectores, text=f"d{j+1}").grid(row=j+1, column=0, padx=5, pady=2)

        # Crear campos de texto para cada vector
        for i in range(num_vectores):
            tk.Label(self.marco_vectores, text=f"Vector {i+1}").grid(row=0, column=i*2+1, padx=5, pady=5, columnspan=2)

            componentes = []
            for j in range(dimensiones):
                entry = tk.Entry(self.marco_vectores)
                entry.grid(row=j+1, column=i*2+1, padx=5, pady=2)
                componentes.append(entry)
            self.entradas.append(componentes)
            
            combobox = ttk.Combobox(self.marco_vectores, values=["+", "-"])
            combobox.set("+")
            combobox.grid(row=dimensiones+1, column=i*2+1, padx=5, pady=5, columnspan=2)
            self.operaciones.append(combobox)

    def calcular(self):
        try:
            dimensiones = self.dimensiones.get()
            num_vectores = self.num_vectores.get()

            # Inicializar el vector resultado
            resultado = [0] * dimensiones

            # Inicializar la variable para el procedimiento
            procedimiento = ""

            # Calcular el resultado
            for j in range(dimensiones):
                procedimiento += f"d{j+1}: "
                for i in range(num_vectores):
                    signo = self.operaciones[i].get()
                    valor = float(self.entradas[i][j].get())
                    if signo == "+":
                        resultado[j] += valor
                        procedimiento += f"{valor} + "
                    elif signo == "-":
                        resultado[j] -= valor
                        procedimiento += f"(-{valor}) + "
                procedimiento = procedimiento.rstrip(" + -") + f" = {resultado[j]}\n"

            # Mostrar el procedimiento y resultado
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, f"Procedimiento:\n{procedimiento}\n")
            self.text_resultado.insert(tk.END, f"Resultado:\n{resultado}")

            # Guardar el resultado para graficar
            self.resultado = resultado

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def graficar(self):
        try:
            dimensiones = self.dimensiones.get()
            resultado = self.resultado

            if dimensiones == 2:
                # Crear la gráfica del vector resultado en 2D
                x, y = resultado
                plt.figure()
                plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='r', width=0.005)
                plt.xlim(-max(abs(x), abs(y)) - 1, max(abs(x), abs(y)) + 1)
                plt.ylim(-max(abs(x), abs(y)) - 1, max(abs(x), abs(y)) + 1)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("Vector Resultado")
                plt.grid()
                plt.text(x, y, f"({x:.2f}, {y:.2f})", fontsize=8, ha='right')
                plt.show()
            elif dimensiones == 3:
                # Crear la gráfica del vector resultado en 3D
                x, y, z = resultado
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.quiver(0, 0, 0, x, y, z)
                ax.set_xlim([min(0, x) - 1, max(0, x) + 1])
                ax.set_ylim([min(0, y) - 1, max(0, y) + 1])
                ax.set_zlim([min(0, z) - 1, max(0, z) + 1])
                ax.set_xlabel('X')
                ax.set_ylabel('Y')
                ax.set_zlabel('Z')
                ax.set_title("Vector Resultado")
                ax.text(x, y, z, f"({x:.2f}, {y:.2f}, {z:.2f})", fontsize=8)
                plt.show()
            else:
                raise NotImplementedError("La gráfica solo está implementada para vectores de hasta 3 dimensiones.")

        except AttributeError:
            messagebox.showerror("Error", "Calcule el resultado antes de graficar.")
        except NotImplementedError as e:
            messagebox.showerror("Error", str(e))
            
    def regresar(self):
        self.destroy()
        self.parent.deiconify()
        
    def limpiar_texto(self):
        self.text_resultado.delete(1.0, tk.END)