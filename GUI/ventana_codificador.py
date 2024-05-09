import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from Codificador.codificador import cifrar_mensaje, descifrar_mensaje, matriz_inversa_cifrado

class VentanaCifradoMatrices(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Cifrado de Matrices")
        self.geometry("600x400")

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(expand=True, pady=20)
        
        self.label_codificado = tk.Label(self.main_frame, text="")
        self.label_codificado.pack(padx=10, pady=10)
        
        self.label_cifrado = tk.Label(self.main_frame, text="")
        self.label_cifrado.pack(padx=10, pady=10)
        
        self.label_decodificado = tk.Label(self.main_frame, text="")
        self.label_decodificado.pack(padx=10, pady=10)
        
        self.label_descifrado = tk.Label(self.main_frame, text="")
        self.label_descifrado.pack(padx=10, pady=10)

        self.text_area = tk.Text(self.main_frame, height=10)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.encrypt_button = ttk.Button(self.main_frame, text="Cifrar", command=self.encrypt_message)
        self.encrypt_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.decrypt_button = ttk.Button(self.main_frame, text="Descifrar", command=self.decrypt_message)
        self.decrypt_button.pack(side=tk.RIGHT, padx=10, pady=10)
        
        self.button_limpiar = tk.Button(self.main_frame, text="Limpiar", command=self.clear)
        self.button_limpiar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        self.button_regresar = tk.Button(self.main_frame, text="Regresar", command=self.regresar)
        self.button_regresar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    def encrypt_message(self):
        message = self.text_area.get("1.0", tk.END).strip()
        if message:
            encrypted_message = cifrar_mensaje(message) 
            resultado = matriz_inversa_cifrado(message)
            self.label_cifrado.config(text=resultado)
            self.label_codificado.config(text=f"MENSAJE CODIFICADO: {encrypted_message}")
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, encrypted_message)
        else:
            messagebox.showerror("Error", "Ingrese un mensaje para cifrar.")

    def decrypt_message(self):
        message = self.text_area.get("1.0", tk.END).strip()
        if message:
            decrypted_message = descifrar_mensaje(message)
            self.label_decodificado.config(text=f"MENSAJE DECODIFICADO: {decrypted_message}")
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, decrypted_message)
        else:
            messagebox.showerror("Error", "Ingrese un mensaje para descifrar.")

    def regresar(self):
        self.destroy()
        self.parent.deiconify()
        
    def clear(self):
        self.label_codificado.config(text="")
        self.label_cifrado.config(text="")
        self.label_decodificado.config(text="")
        self.label_descifrado.config(text="")
        
