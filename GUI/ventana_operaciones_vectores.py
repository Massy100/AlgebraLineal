import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from GUI.ventana_notacion_vectores import VentanaSumaVectores
from GUI.ventana_cruz_vectores import VentanaCruzVectores
from GUI.ventana_punto_vectores import VentanaPuntoVectores
from GUI.ventana_grafica_vectores import VentanaGraficaVectores

class VentanaOperacionesVectores(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Operaciones de Vectores")
        self.geometry("500x400")


        frame = ttk.Frame(self)
        frame.pack(expand=True)

        button0 = ttk.Button(frame, text="Grafica Vectores", command=self.abrir_grafica_vectores)
        button0.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        button1 = ttk.Button(frame, text="Suma y Resta Vectores", command=self.abrir_suma_vectores)
        button1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        button2 = ttk.Button(frame, text="Producto Punto Vectores", command=self.abrir_punto_vectores)
        button2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        button3 = ttk.Button(frame, text="Producto Cruz Vectores", command=self.abrir_cruz_vectores)
        button3.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Botón de regresar, colocado en la esquina inferior derecha
        button_regresar = tk.Button(frame, text="Regresar", command=self.regresar)
        button_regresar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
    def abrir_suma_vectores(self):
        self.withdraw()
        nueva_ventana = VentanaSumaVectores(self)
        nueva_ventana.grab_set()
        
    def abrir_grafica_vectores(self):
        self.withdraw()
        nueva_ventana = VentanaGraficaVectores(self)
        nueva_ventana.grab_set()
    
    def abrir_punto_vectores(self):
        self.withdraw()
        nueva_ventana = VentanaPuntoVectores(self)
        nueva_ventana.grab_set()
    
    def abrir_cruz_vectores(self):
        self.withdraw()
        nueva_ventana = VentanaCruzVectores(self)
        nueva_ventana.grab_set()

    def regresar(self):
        self.destroy()
        self.parent.deiconify()