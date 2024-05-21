import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import math

class VentanaCaso3(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("VentanaCaso3")
        self.geometry("400x400")
        self.parent  = parent
        
        # Etiqueta y campo de texto para magnitud
        self.label_magnitud = tk.Label(self, text="Magnitud")
        self.label_magnitud.pack()
        self.entry_magnitud = tk.Entry(self)
        self.entry_magnitud.pack()
        
        # Etiqueta y campo de texto para ángulo
        self.label_angulo = tk.Label(self, text="Ángulo (grados)")
        self.label_angulo.pack()
        self.entry_angulo = tk.Entry(self)
        self.entry_angulo.pack()
        
        # Botón para calcular componentes
        self.btn_calcular = tk.Button(self, text="Graficar", command=self.calcular)
        self.btn_calcular.pack(pady=10)
        
        # Etiquetas para mostrar los cálculos
        self.label_componente_x = tk.Label(self, text="")
        self.label_componente_x.pack()
        
        self.label_componente_y = tk.Label(self, text="")
        self.label_componente_y.pack()
        
        self.label_direccion = tk.Label(self, text="")
        self.label_direccion.pack()
        
        # Botón para regresar
        self.btn_regresar = tk.Button(self, text="Regresar", command=self.regresar)
        self.btn_regresar.pack(pady=10)
    
    def calcular(self):
        try:
            # Obtener los valores de la magnitud y el ángulo
            magnitud = float(self.entry_magnitud.get())
            angulo = float(self.entry_angulo.get())
        
            if angulo < 0 or angulo > 360:
                raise ValueError("El ángulo debe estar entre 0 y 360 grados.")
        
            # Calcular los componentes X y Y
            x = magnitud * math.cos(math.radians(angulo))
            y = magnitud * math.sin(math.radians(angulo))
            self.label_componente_x.config(text=f"Componente X: {magnitud} * cos({angulo}) = {x:.2f}")
            self.label_componente_y.config(text=f"Componente Y: {magnitud} * sin({angulo}) = {y:.2f}")
        
            # Determinar la dirección
            if 0 <= angulo < 90:
                direccion = "Ya que el angulo comprendido esta en el primer cuadrante se sabe que es EN"
            elif 90 <= angulo < 180:
                direccion = "Ya que el angulo comprendido esta en el segundo cuadrante se sabe que es NO"
            elif 180 <= angulo < 270:
                direccion = "Ya que el angulo comprendido esta en el tercer cuadrante se sabe que es SO"
            elif 270 <= angulo < 360:
                direccion = "Ya que el angulo comprendido esta en el cuarto cuadrante se sabe que es SE"
            else:
                direccion = "Un angulo negativo no es manejable por este programa"
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
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def regresar(self):
        self.destroy()
        self.parent.deiconify()