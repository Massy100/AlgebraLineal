import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from GUI.ventana_operaciones_matrices import VentanaOperacionesMatrices
from GUI.ventana_matriz_inversa import VentanaMatrizInversa

class VentanaAlgebra(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Álgebra Lineal Básica")
        self.geometry("500x400")

        # Crear un frame para contener los botones y centrarlos
        frame = ttk.Frame(self)
        frame.pack(expand=True)

        button1 = ttk.Button(frame, text="Operaciones entre Matrices", command=self.abrir_ventana_operaciones_matrices)
        button1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        button2 = ttk.Button(frame, text="Matriz Inversa", command=self.abrir_ventana_matriz_inversa)
        button2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        button3 = ttk.Button(frame, text="Determinante de una Matriz", command=self.abrir_ventana_determinante_matriz)
        button3.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        button4 = ttk.Button(frame, text="Rango de una Matriz", command=self.abrir_ventana_rango_matriz)
        button4.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Botón de regresar, colocado en la esquina inferior derecha
        button_regresar = tk.Button(frame, text="Regresar", command=self.regresar)
        button_regresar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
    def abrir_ventana_operaciones_matrices(self):
        self.withdraw()
        nueva_ventana = VentanaOperacionesMatrices(self)
        nueva_ventana.grab_set()

    def abrir_ventana_matriz_inversa(self):
        self.withdraw()
        nueva_ventana = VentanaMatrizInversa(self)
        nueva_ventana.grab_set()
    
    def abrir_ventana_determinante_matriz(self):
        pass

    def abrir_ventana_rango_matriz(self):
        pass
    
    def regresar(self):
        self.destroy()
        self.parent.deiconify()