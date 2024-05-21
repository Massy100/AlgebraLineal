import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import math

class VentanaCaso2(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("VentanaCaso2")
        self.geometry("400x500")
        self.parent = parent
        
        # Etiqueta y campo de texto para magnitud
        self.label_magnitud = tk.Label(self, text="Magnitud")
        self.label_magnitud.pack(pady=5)
        self.entry_magnitud = tk.Entry(self)
        self.entry_magnitud.pack(pady=5)
        
        # Etiqueta y campo de texto para componente
        self.label_componente = tk.Label(self, text="Componente")
        self.label_componente.pack(pady=5)
        self.entry_componente = tk.Entry(self)
        self.entry_componente.pack(pady=5)
        
        # Combobox para seleccionar si el componente es X o Y
        self.componente_var = tk.StringVar()
        self.combo_componente = ttk.Combobox(self, textvariable=self.componente_var)
        self.combo_componente['values'] = ('X', 'Y')
        self.combo_componente.pack(pady=5)
        
        # Botón para calcular y graficar
        self.btn_calcular = tk.Button(self, text="Graficar", command=self.calcular)
        self.btn_calcular.pack(pady=10)
        
        # Etiquetas para mostrar los cálculos
        self.label_complementario = tk.Label(self, text="")
        self.label_complementario.pack(pady=5)
        
        self.label_angulo = tk.Label(self, text="")
        self.label_angulo.pack(pady=5)
        
        self.label_direccion = tk.Label(self, text="")
        self.label_direccion.pack(pady=5)
        
        # Botón para regresar
        self.btn_regresar = tk.Button(self, text="Regresar", command=self.regresar)
        self.btn_regresar.pack(pady=10)
    
    def calcular(self):
        try:
            # Obtener los valores de la magnitud y el componente
            magnitud = float(self.entry_magnitud.get())
            componente = float(self.entry_componente.get())
            componente_tipo = self.combo_componente.get()
        
            if componente_tipo not in ['X', 'Y']:
                raise ValueError("Seleccione si el componente es X o Y.")
        
            if componente_tipo == 'X':
                x = componente
                y = math.sqrt(magnitud**2 - x**2)
                self.label_complementario.config(text=f"Paso 1: Encontrar el componente en Y:\nPara esto se debe usar la identidad pitagorica sqrt(magnitud^2 - cateto^2) \nsqrt({magnitud}^2 - {x}^2)\nsqrt({magnitud ** 2} - {x ** 2})\nsqrt({magnitud ** 2 - x ** 2})\n Resultado: {y:.2f}")
                angulo = math.degrees(math.atan2(y, x))
            else:
                y = componente
                x = math.sqrt(magnitud**2 - y**2)
                self.label_complementario.config(text=f"Paso 1: Encontrar el componente en X:\nPara esto se debe usar la identidad pitagorica sqrt(magnitud^2 - cateto^2) \nsqrt({magnitud}^2 - {y}^2)\nsqrt({magnitud ** 2} - {y ** 2})\nsqrt({magnitud ** 2 - y ** 2})\nResultado: {x:.2f}")
                angulo = math.degrees(math.atan2(y, x))
            
            self.label_angulo.config(text=f"Paso 2: Encontrar el ángulo:\nPara esto debemos encontrar la tangente inversa de (y, x)\n atan2({y:.2f}, {x:.2f}) \nResultado: {angulo:.2f} grados")
        
            # Determinar la dirección
            if 0 <= angulo < 90:
                direccion = "Es NE dado que X y Y son positivos"
            elif 90 <= angulo < 180:
                direccion = "Es NO dado que X es negativo y Y es positivo"
            elif 180 <= angulo < 270:
                direccion = "Es SO dado que X y Y son negativos"
            elif 270 <= angulo < 360:
                direccion = "Es SE dado que X es positivo y Y es negativo"
            else:
                direccion = "Un angulo negativo no es manejable por este programa"
            self.label_direccion.config(text=f"Paso 3: Encontrar la dirección:\n {direccion}")
        
            # Crear la gráfica del vector
            plt.figure()
            plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='r', width=0.005)
            plt.xlim(-magnitud - 1, magnitud + 1)
            plt.ylim(-magnitud - 1, magnitud + 1)
            plt.text(x, y, f"({x:.2f}, {y:.2f})\nMagnitud: {magnitud:.2f}\nÁngulo: {angulo:.2f} grados\nDirección: {direccion}", fontsize=8)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Vector")
            plt.grid()
            plt.show()
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def regresar(self):
        self.destroy()
        self.parent.deiconify()