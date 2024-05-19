import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import simpledialog, messagebox
from CadenaMarkov.markov import CadenaMarkov
import matplotlib.pyplot as plt
import networkx as nx

class VentanaCadenaMarkov(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Cadenas de Markov")
        self.geometry("500x400")
        
        self.matriz_entries = []
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, pady=20)
        
        self.start_button = ttk.Button(self, text="Iniciar", command=self.ask_dimensions)
        self.start_button.pack(pady=20)

        self.calc_button = ttk.Button(self, text="Calcular Multiplicaciones", command=self.process_matrix)
        self.calc_button.pack(pady=10)
        self.calc_button.config(state=tk.DISABLED)
        
        self.graph_button = ttk.Button(self, text="Graficar Grafo", command=self.graph_matrix)
        self.graph_button.pack(pady=10)
        #self.graph_button.config(state=tk.DISABLED) 

        self.button_regresar = ttk.Button(self, text="Regresar", command=self.regresar)
        self.button_regresar.pack(pady=20)

        self.output_text = tk.Text(self, height=15, width=50)
        self.output_text.pack(pady=20)
        
    def ask_dimensions(self):
        self.calc_button.config(state=tk.DISABLED)  # Disable button until new matrix is ready
        rows = simpledialog.askinteger("Input", "Número de filas:", parent=self, minvalue=1, maxvalue=10)
        columns = simpledialog.askinteger("Input", "Número de columnas:", parent=self, minvalue=1, maxvalue=10)
        if rows and columns and rows == columns:
            self.create_matrix_entries(rows, columns)
            self.calc_button.config(state=tk.NORMAL)  # Enable after matrix is created
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
            matriz = [[float(entry.get()) for entry in row] for row in self.matriz_entries]
            if not self.validate_matrix(matriz):
                messagebox.showerror("Error", "Las filas de la matriz deben sumar 1.")
                return
            condiciones = simpledialog.askstring("Condiciones Iniciales", "Ingrese condiciones iniciales (separadas por espacios):", parent=self)
            veces = simpledialog.askinteger("Iteraciones", "Número de veces para multiplicar:", parent=self, minvalue=1)
            cadena = CadenaMarkov(matriz)
            resultados = cadena.multiplicar_matrices(condiciones, veces)
            self.display_results(resultados)
        except ValueError:
            messagebox.showerror("Error", "Por favor, asegúrese de que todos los campos contengan números válidos.")

    def validate_matrix(self, matriz):
        return all(abs(sum(row) - 1) < 0.0001 for row in matriz)  # Use a tolerance for floating point arithmetic

    def display_results(self, resultados):
        self.output_text.delete('1.0', tk.END)
        for i, res in enumerate(resultados, 1):
            self.output_text.insert(tk.END, f"Iteración {i}: {res}\n")

    def regresar(self):
        self.destroy()
        self.parent.deiconify()
        
    def graph_matrix(self):
        try:
            matriz = [[float(entry.get()) for entry in row] for row in self.matriz_entries]
            G = self.crear_grafo_desde_matriz(matriz)
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15, arrows=True)
            edge_labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
            plt.show()
        except ValueError:
            messagebox.showerror("Error", "Asegúrese de que todos los campos de la matriz contengan números válidos.")

    def crear_grafo_desde_matriz(self, matriz):
        G = nx.DiGraph()
        for i, fila in enumerate(matriz):
            for j, valor in enumerate(fila):
                if valor != 0:
                    G.add_edge(i, j, weight=valor)
        return G