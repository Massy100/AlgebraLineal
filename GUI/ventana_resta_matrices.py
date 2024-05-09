import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import simpledialog, messagebox
from OperacionesMatrices.suma import SumaMatrices

class VentanaRestaMatrices(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Resta de Matrices")
        self.geometry("500x400")
        
        # Crear un frame principal para contener todo
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(expand=True, pady=20)

        # Crear frames para cada matriz y el signo de operación
        self.frame_matrix1 = ttk.Frame(self.main_frame)
        self.frame_matrix1.grid(row=0, column=0, padx=10, pady=20)

        self.frame_sum_sign = ttk.Frame(self.main_frame)
        self.frame_sum_sign.grid(row=0, column=1, padx=10, pady=20)
        self.sum_label = ttk.Label(self.frame_sum_sign, text="-", font=("Arial", 24))  # Cambiado a signo de resta
        self.sum_label.pack()

        self.frame_matrix2 = ttk.Frame(self.main_frame)
        self.frame_matrix2.grid(row=0, column=2, padx=10, pady=20)

        # Botón para iniciar la entrada de matrices
        self.start_button = ttk.Button(self, text="Iniciar Entradas", command=self.ask_dimensions)
        self.start_button.pack(pady=20)

        # Botón para calcular la resta
        self.calc_button = ttk.Button(self, text="Calcular Resta", command=self.process_matrix)  # Cambiado a calcular resta
        self.calc_button.pack(pady=10)

        # Botón de regresar
        self.button_regresar = ttk.Button(self, text="Regresar", command=self.regresar)
        self.button_regresar.pack(pady=20)

    def ask_dimensions(self):
        rows = simpledialog.askinteger("Input", "Número de filas:", parent=self, minvalue=1, maxvalue=10)
        columns = simpledialog.askinteger("Input", "Número de columnas:", parent=self, minvalue=1, maxvalue=10)
        if rows and columns:
            self.create_matrix_entries(rows, columns)
        else:
            messagebox.showerror("Error", "Debe ingresar dimensiones válidas.")

    def create_matrix_entries(self, rows, columns):
        # Limpiar y preparar frames para nuevas entradas
        for frame in [self.frame_matrix1, self.frame_matrix2]:
            for widget in frame.winfo_children():
                widget.destroy()

        self.matriz1_entries = []
        self.matriz2_entries = []
        for i in range(rows):
            row_entries1 = []
            row_entries2 = []
            for j in range(columns):
                entry1 = ttk.Entry(self.frame_matrix1, width=5)
                entry1.grid(row=i, column=j, padx=5, pady=5)
                row_entries1.append(entry1)

                entry2 = ttk.Entry(self.frame_matrix2, width=5)
                entry2.grid(row=i, column=j, padx=5, pady=5)
                row_entries2.append(entry2)
            self.matriz1_entries.append(row_entries1)
            self.matriz2_entries.append(row_entries2)

    def process_matrix(self):
        try:
            # Extraer los datos de las entradas de las matrices
            m1 = [[float(entry.get()) for entry in row] for row in self.matriz1_entries]
            m2 = [[float(entry.get()) for entry in row] for row in self.matriz2_entries]

            # Calcular la resta de las matrices y preparar los detalles del cálculo
            result = []
            calculation_details = []

            for i in range(len(m1)):
                result_row = []
                detail_row = []
                for j in range(len(m1[0])):
                    subtract_result = m1[i][j] - m2[i][j]
                    result_row.append(subtract_result)
                    detail_row.append(f"{m1[i][j]} - {m2[i][j]} = {subtract_result:.2f}")
                result.append(result_row)
                calculation_details.append(detail_row)

            # Mostrar la matriz resultado y los detalles del cálculo en una nueva ventana
            result_window = tk.Toplevel(self)
            result_window.title("Procedimiento Resta")
            for i, (row, details) in enumerate(zip(result, calculation_details)):
                for j, (val, detail) in enumerate(zip(row, details)):
                    label = ttk.Label(result_window, text=detail)
                    label.grid(row=i, column=j, padx=5, pady=5)

        except ValueError:
            messagebox.showerror("Error", "Por favor, asegúrese de que todos los campos contengan números válidos.")

    def regresar(self):
        self.destroy()
        self.parent.deiconify()
