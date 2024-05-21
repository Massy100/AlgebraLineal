import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib.pyplot as plt


class VentanaCaso4(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ventana Caso")
        self.geometry("400x500")
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
            # Obtener el componente, angulo y direccion del componente
            componenete_D = self.combo_componente.get()
            componente = float(self.entry_componente.get())
            angulo = float(self.entry_angulo.get())



            # Calcular la magnitud
            if componenete_D == 'X':
                magnitud = round(componente / math.cos(math.radians(angulo)), 2)
                direct = 'cos'
            else:
                magnitud = round(componente / math.sin(math.radians(angulo)), 2)
                direct = 'sin'

            if magnitud < 0:
                magnitud *= -1




            # Calcular el componente complementario
            componente_complementario = round(math.sqrt(magnitud ** 2 - componente ** 2), 2)

            # Calcular la dirección
            if angulo < 0 or angulo >= 360:
                raise ValueError("El ángulo debe estar entre 0 y 360 grados.")

            if 0 <= angulo < 90:
                direccion = "Ya que el angulo comprendido esta en el primer cuadrante se sabe que es EN"
            elif 90 <= angulo < 180:
                direccion = "Ya que el angulo comprendido esta en el segundo cuadrante se sabe que es NO"
            elif 180 <= angulo < 270:
                direccion = "Ya que el angulo comprendido esta en el tercer cuadrante se sabe que es SO"
            else:
                direccion = "Ya que el angulo comprendido esta en el cuarto cuadrante se sabe que es SE"

            # Mostrar los resultados
            self.label_resultados.config(text=f"Paso 1: Encontrar la magnitud\nPara esto usaremos componenete / {direct}(angulo)\n {componente} / {direct}{angulo}\nResultado: {magnitud:.2f}\nPaso 2: Encontrar el componente complementario:\n pare esto siempre usaremos sqrt(magnitud^2 - componente^2)\nsqrt({magnitud}^2 - {componente}^2)\nsqrt({round(magnitud ** 2, 2)} - {round(componente ** 2,2)}) \nResultado: {componente_complementario:.2f}\nDirección:\n {direccion}")

            # Habilitar el botón de graficar
            self.btn_graficar.config(state=tk.NORMAL)

            # Almacenar la magnitud y la dirección para poder usarlas en el método graficar
            self.magnitud = magnitud
            self.co_co = componente_complementario
            self.componenete_D = componenete_D

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def graficar(self):
        try:
            # Obtener el componente
            componente = float(self.entry_componente.get())
            grados = float(self.entry_angulo.get())
            if self.componenete_D == 'X':
                x = componente
                y = self.co_co
            else:
                x = self.co_co
                y = componente

            # Ajustar el signo de los componentes dependiendo del ángulo y la dirección
            if 0 <= grados <= 90:
                direccion = 'EN'
            elif 90 < grados <= 180:
                x = -x
                direccion = 'NO'
            elif 180 < grados <= 270:
                y = -y
                x = -x
                direccion = 'OS'
            else:
                y = -y
                direccion = 'SE'

            # Graficar el vector
            plt.figure()
            plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='r', width=0.005)
            plt.text(x, y, f"({x:.2f}, {y:.2f})\nMagnitud: {self.magnitud:.2f}\nDireccion: {direccion}", fontsize=8)
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