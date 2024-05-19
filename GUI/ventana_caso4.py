import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib.pyplot as plt


class VentanaCaso4(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ventana Caso")
        self.geometry("400x400")
        self.parent = parent

        # Etiqueta y campo de texto para el componente
        self.label_componente = tk.Label(self, text="Componente")
        self.label_componente.pack(pady=5)
        self.entry_componente = tk.Entry(self)
        self.entry_componente.pack(pady=5)

        # Combobox para seleccionar si el componente es X o Y
        self.componente_var = tk.StringVar()
        self.combo_componente = ttk.Combobox(self, textvariable=self.componente_var)
        self.combo_componente['values'] = ('X', 'Y')
        self.combo_componente.pack(pady=5)

        # Etiqueta y campo de texto para el ángulo
        self.label_angulo = tk.Label(self, text="Ángulo (en grados)")
        self.label_angulo.pack(pady=5)
        self.entry_angulo = tk.Entry(self)
        self.entry_angulo.pack(pady=5)

        # Botón para calcular
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.pack(pady=10)

        # Etiqueta para mostrar los resultados
        self.label_resultados = tk.Label(self, text="")
        self.label_resultados.pack(pady=5)

        # Botón para graficar
        self.btn_graficar = tk.Button(self, text="Graficar", command=self.graficar, state=tk.DISABLED)
        self.btn_graficar.pack(pady=10)

        # Botón para regresar
        self.btn_regresar = tk.Button(self, text="Regresar", command=self.regresar)
        self.btn_regresar.pack(pady=10)

    def calcular(self):
        try:
            # Obtener el componente y el ángulo
            componente = float(self.entry_componente.get())
            angulo = float(self.entry_angulo.get())

            # Calcular la magnitud
            magnitud = math.sqrt(componente ** 2 + componente ** 2)

            # Calcular el componente complementario
            componente_complementario = magnitud * math.sin(math.radians(angulo))

            # Calcular la dirección
            if angulo < 0 or angulo >= 360:
                raise ValueError("El ángulo debe estar entre 0 y 360 grados.")

            if 0 <= angulo < 90:
                direccion = "NE"
            elif 90 <= angulo < 180:
                direccion = "NO"
            elif 180 <= angulo < 270:
                direccion = "SO"
            else:
                direccion = "SE"

            # Mostrar los resultados
            self.label_resultados.config(text=f"Magnitud: {magnitud:.2f}\nComponente complementario: {componente_complementario:.2f}\nDirección: {direccion}")

            # Habilitar el botón de graficar
            self.btn_graficar.config(state=tk.NORMAL)

            # Almacenar la magnitud y la dirección para poder usarlas en el método graficar
            self.magnitud = magnitud
            self.direccion = direccion

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def graficar(self):
        try:
            # Obtener el componente
            componente = float(self.entry_componente.get())

            # Calcular los componentes x e y
            x = componente
            y = componente

            # Ajustar el signo de los componentes dependiendo del ángulo y la dirección
            if self.direccion == "NE":
                pass  # Los componentes ya están en el primer cuadrante
            elif self.direccion == "NO":
                x = -x  # Ajustar para el segundo cuadrante
            elif self.direccion == "SO":
                x = -x  # Ajustar para el tercer cuadrante
                y = -y  # Ajustar para el tercer cuadrante
            else:
                y = -y  # Ajustar para el cuarto cuadrante

            # Graficar el vector
            plt.figure()
            plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='r', width=0.005)
            plt.text(x, y, f"({x:.2f}, {y:.2f})\nMagnitud: {self.magnitud:.2f}\nDirección: {self.direccion}", fontsize=8)
            plt.xlim(-self.magnitud - 1, self.magnitud + 1)
            plt.ylim(-self.magnitud - 1, self.magnitud + 1)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Vector")
            plt.grid()
            plt.show()

        except ValueError as e:
            messagebox.showerror("Error", "Debe calcular los valores antes de graficar")

            
    def regresar(self):
        self.destroy()
        self.parent.deiconify()