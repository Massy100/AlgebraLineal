import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from GUI.ventana_caso1 import VentanaCaso1
from GUI.ventana_caso3 import VentanaCaso3
from GUI.ventana_caso2 import VentanaCaso2
from GUI.ventana_caso4 import VentanaCaso4

class VentanaGraficaVectores(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Opciones Grafica de Vectores")
        self.geometry("500x400")

        # Crear un frame para contener los botones y centrarlos
        frame = ttk.Frame(self)
        frame.pack(expand=True)

        button0 = ttk.Button(frame, text="Ambos Componentes", command=self.abrir_caso_1)
        button0.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        button1 = ttk.Button(frame, text="Componente y Magnitud", command=self.abrir_caso_2)
        button1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        button2 = ttk.Button(frame, text="Magnitud y Angulo", command=self.abrir_caso_3)
        button2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        button3 = ttk.Button(frame, text="Componente y Angulo", command=self.abrir_caso_4)
        button3.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Botón de regresar, colocado en la esquina inferior derecha
        button_regresar = tk.Button(frame, text="Regresar", command=self.regresar)
        button_regresar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
    def abrir_caso_1(self):
        self.withdraw()
        nueva_ventana = VentanaCaso1(self)
        nueva_ventana.grab_set()
        
    def abrir_caso_2(self):
        self.withdraw()
        nueva_ventana = VentanaCaso2(self)
        nueva_ventana.grab_set()
    
    def abrir_caso_3(self):
        self.withdraw()
        nueva_ventana = VentanaCaso3(self)
        nueva_ventana.grab_set()
    
    def abrir_caso_4(self):
        self.withdraw()
        nueva_ventana = VentanaCaso4(self)
        nueva_ventana.grab_set()

    def regresar(self):
        self.destroy()
        self.parent.deiconify()