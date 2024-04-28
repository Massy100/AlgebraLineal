import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from GUI.ventana_suma_matrices import VentanaSumaMatrices
from GUI.ventana_resta_matrices import VentanaRestaMatrices

class VentanaOperacionesMatrices(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Operaciones entre Matrices")
        self.geometry("500x400")

        # Crear un frame para contener los botones y centrarlos
        frame = ttk.Frame(self)
        frame.pack(expand=True)

        button1 = ttk.Button(frame, text="Suma de matrices", command=self.abrir_ventana_operaciones_matrices)
        button1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        button2 = ttk.Button(frame, text="Resta de matrices", command=self.abrir_ventana_resta_matrices)
        button2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        button3 = ttk.Button(frame, text="Multiplicación de matrices", command=self.abrir_ventana_multiplicacion_matrices)
        button3.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        button4 = ttk.Button(frame, text="Producto punto de matrices", command=self.abrir_ventana_producto_punto_matrices)
        button4.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Botón de regresar, colocado en la esquina inferior derecha
        button_regresar = tk.Button(frame, text="Regresar", command=self.regresar)
        button_regresar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
    def abrir_ventana_operaciones_matrices(self):
        self.withdraw()
        nueva_ventana = VentanaSumaMatrices(self)
        nueva_ventana.grab_set()

    def abrir_ventana_resta_matrices(self):
        self.withdraw()
        nueva_ventana = VentanaRestaMatrices(self)
        nueva_ventana.grab_set()
    
    def abrir_ventana_multiplicacion_matrices(self):
        pass

    def abrir_ventana_producto_punto_matrices(self):
        pass
    
    def regresar(self):
        self.destroy()
        self.parent.deiconify()