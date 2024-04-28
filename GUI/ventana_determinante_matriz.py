import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import simpledialog, messagebox
from MatrizInversa.matriz_inversa import MatrizInversa
from MetodoCoeficientes.metodo_coeficientes import DeterminanteMatriz
from MetodoCoeficientes.metodo_coeficientes import MatrixOperations

class VentanaMatrizDeterminante(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Determinante Matriz")
        self.geometry("500x400")
        self.matriz_entries = []

        # Crear un frame para contener los botones y centrarlos
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, pady=20)
        
        # Botón para solicitar dimensiones y crear entradas de matriz
        self.start_button = ttk.Button(self, text="Iniciar", command=self.ask_dimensions)
        self.start_button.pack(pady=20)

        # Botón para calcular la determinante
        self.calc_button = ttk.Button(self, text="Calcular Determinante", command=self.process_matrix)
        self.calc_button.pack(pady=10)

        # Botón de regresar
        self.button_regresar = ttk.Button(self, text="Regresar", command=self.regresar)
        self.button_regresar.pack(pady=20)

    def ask_dimensions(self):
        rows = simpledialog.askinteger("Input", "Numero de filas:", parent=self, minvalue=1, maxvalue=10)
        columns = simpledialog.askinteger("Input", "Numero de columnas:", parent=self, minvalue=1, maxvalue=10)
        if rows and columns and rows == columns:  # La matriz debe ser cuadrada
            self.create_matrix_entries(rows, columns)
        else:
            messagebox.showerror("Error", "Debe ingresar una matriz cuadrada.")

    def create_matrix_entries(self, rows, columns):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.matriz_entries = []
        for i in range(rows):
            row_entries = []
            for j in range(columns):
                entry = ttk.Entry(self.frame, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.matriz_entries.append(row_entries)

    def process_matrix(self):
        try:
            matriz = [[float(entry.get()) for entry in row_entries] for row_entries in self.matriz_entries]
            determinante = MatrixOperations.calculate_determinant(matriz)
            messagebox.showinfo("Resultado", f"La determinante de la matriz es: {determinante:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, asegúrese de que todos los campos contengan números válidos.")

    def regresar(self):
        self.destroy()
        self.parent.deiconify()