import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import simpledialog, messagebox
from MatrizInversa.matriz_inversa import MatrizInversa

class VentanaMatrizInversa(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Matriz Inversa")
        self.geometry("500x400")
        self.matriz_entries = []

        # Crear un frame para contener los botones y centrarlos
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, pady=20)
        
        # Botón para solicitar dimensiones y crear entradas de matriz
        self.start_button = ttk.Button(self, text="Iniciar", command=self.ask_dimensions)
        self.start_button.pack(pady=20)

        # Botón para calcular la inversa
        self.calc_button = ttk.Button(self, text="Calcular Inversa", command=self.process_matrix)
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
        # Limpiar el frame anterior de cualquier widget que pudiera tener
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
            mi = MatrizInversa(matriz)
            inversa = mi.calcular_inversa()

            result_window = tk.Toplevel(self)
            result_window.title("Procedimiento Matriz Inversa")
            row_count = 0
            for detail in mi.detalles:
                label = ttk.Label(result_window, text=detail)
                label.grid(row=row_count, column=0, padx=5, pady=5, sticky="w")
                row_count += 1
            for i, row in enumerate(inversa):
                for j, val in enumerate(row):
                    label = ttk.Label(result_window, text=f"{val:.2f}")
                    label.grid(row=row_count, column=j, padx=5, pady=5)
                row_count += 1

        except ValueError as e:
            messagebox.showerror("Error", "La matriz no tiene inversa")

    def regresar(self):
        self.destroy()  # Cerrar esta ventana
        self.parent.deiconify()  # Mostrar la ventana principal