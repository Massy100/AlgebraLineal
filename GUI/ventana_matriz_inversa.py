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

        # Botón de regresar, colocado en la esquina inferior derecha
        self.button_regresar = tk.Button(self.frame, text="Regresar", command=self.regresar)
        self.button_regresar.pack(side=tk.BOTTOM, anchor='se', padx=10, pady=5)

    def ask_dimensions(self):
        rows = simpledialog.askinteger("Input", "Number of rows:", parent=self, minvalue=1, maxvalue=10)
        columns = simpledialog.askinteger("Input", "Number of columns:", parent=self, minvalue=1, maxvalue=10)
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
            matriz = []
            for row_entries in self.matriz_entries:
                row = [float(entry.get()) for entry in row_entries]
                matriz.append(row)
        
            # Crear una instancia de MatrizInversa y calcular la inversa
            mi = MatrizInversa(matriz)
            inversa = mi.calcular_inversa()

            # Mostrar la matriz inversa en una nueva ventana o de otra forma
            result_window = tk.Toplevel(self)
            result_window.title("Matriz Inversa")
            for i, row in enumerate(inversa):
                for j, val in enumerate(row):
                    label = ttk.Label(result_window, text=f"{val:.2f}")
                    label.grid(row=i, column=j, padx=5, pady=5)
                
            print("Matrix values:")
            for row in inversa:
                print(row)
        except ValueError as e:
            messagebox.showerror("Error", "Por favor, asegúrese de que todos los campos contengan números válidos.")

    def regresar(self):
        self.destroy()  # Cerrar esta ventana
        self.parent.deiconify()  # Mostrar la ventana principal