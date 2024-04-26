import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel

class VentanaInvestigacion(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Investigación en Ciencias de Datos")
        self.geometry("500x400")

        # Crear un frame para contener los botones y centrarlos
        frame = ttk.Frame(self)
        frame.pack(expand=True)

        button1 = ttk.Button(frame, text="Operaciones con Vectores", command=self.abrir_ventana_operaciones_vectores)
        button1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Botón de regresar, colocado en la esquina inferior derecha
        button_regresar = tk.Button(frame, text="Regresar", command=self.regresar)
        button_regresar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
    def abrir_ventana_operaciones_vectores(self):
        pass

    def regresar(self):
        self.destroy()
        self.parent.deiconify()