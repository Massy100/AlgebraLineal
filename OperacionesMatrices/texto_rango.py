import tkinter as tk
from tkinter import ttk

def main(texto):
    root = tk.Tk()
    root.title("Rango Scrollbar")

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    content_frame = ttk.Frame(canvas)

    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    label_text = texto
    label = ttk.Label(content_frame, text=label_text, justify=tk.LEFT)
    label.pack()

    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()

