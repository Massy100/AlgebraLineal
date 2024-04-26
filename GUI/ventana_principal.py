import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from GUI.ventana_algebra import VentanaAlgebra
from GUI.ventana_criptografia import VentanaCriptografia
from GUI.ventana_investigacion import VentanaInvestigacion
from GUI.ventana_simulacion import VentanaSimulacion


class VentanaPrincipal(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ventana Principal")
        self.geometry("500x400")

        # Crear un frame para contener los botones y centrarlos
        frame = ttk.Frame(self)
        frame.pack(expand=True)

        # Botón de Álgebra Lineal Básica
        button1 = ttk.Button(frame, text="Álgebra Lineal Básica", command=self.abrir_ventana_algebra)
        button1.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        # Botón de Criptografía
        button2 = ttk.Button(frame, text="Criptografía", command=self.abrir_ventana_criptografia)
        button2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        # Botón de Investigación en Ciencias de Datos
        button3 = ttk.Button(frame, text="Investigación en Ciencias de Datos", command=self.abrir_ventana_investigacion)
        button3.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        # Botón de Simulación y Modelado
        button4 = ttk.Button(frame, text="Simulación y Modelado", command=self.abrir_ventana_simulacion)
        button4.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
    def abrir_ventana_algebra(self):
        self.withdraw()
        nueva_ventana = VentanaAlgebra(self)
        nueva_ventana.grab_set()

    def abrir_ventana_criptografia(self):
        self.withdraw()
        nueva_ventana = VentanaCriptografia(self)
        nueva_ventana.grab_set()
    
    def abrir_ventana_investigacion(self):
        self.withdraw()
        nueva_ventana = VentanaInvestigacion(self)
        nueva_ventana.grab_set()

    def abrir_ventana_simulacion(self):
        self.withdraw()
        nueva_ventana = VentanaSimulacion(self)
        nueva_ventana.grab_set()

def main():
    root = tk.Tk()  
    root.withdraw()  
    ventana_principal = VentanaPrincipal(root)
    ventana_principal.mainloop()

