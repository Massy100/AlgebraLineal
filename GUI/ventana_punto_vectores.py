import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
import math
from OperacionesConVectores import vector_por_grados

class VentanaPuntoVectores(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Creacion de Vectores")
        self.geometry("500x400")

        # Crear un frame para contener los botones y centrarlos
        frame = ttk.Frame(self)
        frame.pack(expand=True)

        button1 = ttk.Button(frame, text="Calcular", command=self.calcular)
        button1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Botón de regresar, colocado en la esquina inferior derecha
        button_regresar = tk.Button(frame, text="Regresar", command=self.regresar)
        button_regresar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
    def calcular(self):
        vector_por_grados.main()

    def regresar(self):
        self.destroy()
        self.parent.deiconify()