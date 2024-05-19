import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
import math
from GUI.ventana_componentes import VentanaComponentes
from GUI.ventana_suma_magnitud import VentanaMagnitud

class VentanaSumaVectores(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Suma de Vectores")
        self.geometry("500x400")

        # Crear un frame para contener los botones y centrarlos
        frame = ttk.Frame(self)
        frame.pack(expand=True)

        button1 = ttk.Button(frame, text="Por Componentes", command=self.abrir_suma_componentes)
        button1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        button2 = ttk.Button(frame, text="Por Magnitud y Angulo", command=self.abrir_suma_magnitud)
        button2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Botón de regresar, colocado en la esquina inferior derecha
        button_regresar = tk.Button(frame, text="Regresar", command=self.regresar)
        button_regresar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
    def abrir_suma_componentes(self):
        self.withdraw()
        nueva_ventana = VentanaComponentes(self)
        nueva_ventana.grab_set()
    
    def abrir_suma_magnitud(self):
        self.withdraw()
        nueva_ventana = VentanaMagnitud(self)
        nueva_ventana.grab_set()

    def regresar(self):
        self.destroy()
        self.parent.deiconify()