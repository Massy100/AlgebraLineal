import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import simpledialog, messagebox
from OperacionesMatrices.mult_mat import MatrixMultiplication

class VentanaMultiplicacionMatrices(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Multiplicación de Matrices")
        self.geometry("600x400")

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(expand=True, pady=20)

        self.frame_matrix1 = ttk.Frame(self.main_frame)
        self.frame_matrix1.grid(row=0, column=0, padx=10, pady=20)

        self.frame_multiplication_sign = ttk.Frame(self.main_frame)
        self.frame_multiplication_sign.grid(row=0, column=1, padx=10, pady=20)
        self.multiplication_label = ttk.Label(self.frame_multiplication_sign, text="*", font=("Arial", 24))
        self.multiplication_label.pack()

        self.frame_matrix2 = ttk.Frame(self.main_frame)
        self.frame_matrix2.grid(row=0, column=2, padx=10, pady=20)

        self.start_button = ttk.Button(self, text="Iniciar Entradas", command=self.ask_dimensions)
        self.start_button.pack(pady=20)

        self.calc_button = ttk.Button(self, text="Calcular Multiplicación", command=self.process_matrix)
        self.calc_button.pack(pady=10)

        self.button_regresar = ttk.Button(self, text="Regresar", command=self.regresar)
        self.button_regresar.pack(pady=20)

        self.matriz1_entries = []
        self.matriz2_entries = []
        self.rows1 = 0
        self.cols1 = 0
        self.rows2 = 0
        self.cols2 = 0

    def ask_dimensions(self):
        self.rows1 = simpledialog.askinteger("Input", "Número de filas para Matriz 1:", parent=self, minvalue=1, maxvalue=10)
        self.cols1 = simpledialog.askinteger("Input", "Número de columnas para Matriz 1:", parent=self, minvalue=1, maxvalue=10)
        self.rows2 = simpledialog.askinteger("Input", "Número de filas para Matriz 2:", parent=self, minvalue=1, maxvalue=10)
        self.cols2 = simpledialog.askinteger("Input", "Número de columnas para Matriz 2:", parent=self, minvalue=1, maxvalue=10)
        if self.cols1 != self.rows2:
            messagebox.showerror("Error", "El número de columnas de la Matriz 1 debe coincidir con el número de filas de la Matriz 2 para la multiplicación.")
        else:
            self.create_matrix_entries()

    def create_matrix_entries(self):
        for frame in [self.frame_matrix1, self.frame_matrix2]:
            for widget in frame.winfo_children():
                widget.destroy()

        for i in range(self.rows1):
            row_entries1 = []
            for j in range(self.cols1):
                entry1 = ttk.Entry(self.frame_matrix1, width=5)
                entry1.grid(row=i, column=j, padx=5, pady=5)
                row_entries1.append(entry1)
            self.matriz1_entries.append(row_entries1)

        for i in range(self.rows2):
            row_entries2 = []
            for j in range(self.cols2):
                entry2 = ttk.Entry(self.frame_matrix2, width=5)
                entry2.grid(row=i, column=j, padx=5, pady=5)
                row_entries2.append(entry2)
            self.matriz2_entries.append(row_entries2)

    def process_matrix(self):
        try:
            m1 = [[float(entry.get()) for entry in row] for row in self.matriz1_entries]
            m2 = [[float(entry.get()) for entry in row] for row in self.matriz2_entries]
            result = []
            for i in range(self.rows1):
                result_row = []
                for j in range(self.cols2):
                    cell_sum = 0
                    for k in range(self.cols1):  
                        cell_sum += m1[i][k] * m2[k][j]
                    result_row.append(cell_sum)
                result.append(result_row)

            result_window = tk.Toplevel(self)
            result_window.title("Resultado de la Multiplicación")
            for i, row in enumerate(result):
                for j, val in enumerate(row):
                    label = ttk.Label(result_window, text=f"{val:.2f}")
                    label.grid(row=i, column=j, padx=5, pady=5)

        except ValueError:
            messagebox.showerror("Error", "Por favor, asegúrese de que todos los campos contengan números válidos.")

    def regresar(self):
        self.destroy()
        self.parent.deiconify()