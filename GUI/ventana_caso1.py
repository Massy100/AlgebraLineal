import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import math

class VentanaCaso1(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("VentanaCaso1")
        self.geometry("400x400")
        
        # Etiqueta y campo de texto para componente X
        self.label_x = tk.Label(self, text="Componente X")
        self.label_x.pack()
        self.entry_x = tk.Entry(self)
        self.entry_x.pack()
        
        # Etiqueta y campo de texto para componente Y
        self.label_y = tk.Label(self, text="Componente Y")
        self.label_y.pack()
        self.entry_y = tk.Entry(self)
        self.entry_y.pack()
        
        # Botón para graficar
        self.btn_graficar = tk.Button(self, text="Graficar", command=self.graficar)
        self.btn_graficar.pack(pady=10)
        
        # Etiquetas para mostrar los cálculos
        self.label_magnitud = tk.Label(self, text="")
        self.label_magnitud.pack()
        
        self.label_angulo = tk.Label(self, text="")
        self.label_angulo.pack()
        
        self.label_direccion = tk.Label(self, text="")
        self.label_direccion.pack()
        
        # Botón para regresar
        self.btn_regresar = tk.Button(self, text="Regresar", command=self.regresar)
        self.btn_regresar.pack(pady=10)
    
    def graficar(self):
        try:
            # Obtener los valores de los componentes X y Y
            x = float(self.entry_x.get())
            y = float(self.entry_y.get())
        
            # Calcular la magnitud
            magnitud = math.sqrt(x**2 + y**2)
            self.label_magnitud.config(text=f"Magnitud: √({x}² + {y}²) = {magnitud:.2f}")
        
            # Calcular el ángulo en grados
            angulo = math.degrees(math.atan2(y, x))
            self.label_angulo.config(text=f"Ángulo: arctan({y}/{x}) = {angulo:.2f}°")
        
            # Determinar la dirección
            if x > 0 and y > 0:
                direccion = "NE"
            elif x < 0 and y > 0:
                direccion = "NO"
            elif x < 0 and y < 0:
                direccion = "SO"
            elif x > 0 and y < 0:
                direccion = "SE"
            elif x == 0 and y > 0:
                direccion = "N"
            elif x == 0 and y < 0:
                direccion = "S"
            elif x > 0 and y == 0:
                direccion = "E"
            elif x < 0 and y == 0:
                direccion = "O"
            else:
                direccion = "Origen"
            self.label_direccion.config(text=f"Dirección: {direccion}")
        
            # Crear la gráfica del vector
            plt.figure()
            plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1)
            plt.xlim(-10, 10)
            plt.ylim(-10, 10)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Vector")
            plt.text(x, y, f"({x:.2f}, {y:.2f})\nMagnitud: {magnitud:.2f}\nÁngulo: {angulo:.2f}°\nDirección: {direccion}", fontsize=8)
            plt.grid()
            plt.show()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def regresar(self):
        self.destroy()
        self.master.deiconify()


