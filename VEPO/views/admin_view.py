import tkinter as tk
from tkinter import ttk


class Administracion:
    def __init__(self, root, nombre_completo):
        super().__init__(root)
        self.root = root
        self.root.title("Administración")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Título de la ventana
        lbl_titulo = tk.Label(
            self.root,
            text="Administración",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333333",
        )
        lbl_titulo.pack(pady=20)

        # Mensaje de bienvenida
        lbl_mensaje = tk.Label(
            self.root,
            text=f"Bienvenido a la sección de administración.{nombre_completo}",
            font=("Arial", 14),
            bg="#f0f0f0",
            fg="#666666",
        )
        lbl_mensaje.pack(pady=10)

    def tabla_empleados(self, parent):
        right_frame = tk.Frame(parent)
        right_frame.pack(side="right", fill="both",
                         expand=True, padx=5, pady=5)

        lbl_tabla = tk.Label(
            right_frame, text="Registros de empleados", font=("Helvetica", 10, "bold"))
        lbl_tabla.pack(anchor="w", pady=2)

        # Scrollbar
        tree_scroll = ttk.Scrollbar(right_frame)
        tree_scroll.pack(side="right", fill="y")

        # Tabla (Treeview)
        self.table = ttk.Treeview(
            right_frame,
            columns=("ID empleado", "Nombre", "Price", "Stock"),
            show="headings",
            yscrollcommand=tree_scroll.set
        )
        self.table.pack(fill="both", expand=True)

        tree_scroll.config(command=self.table.yview)

        # Encabezados
        self.table.heading("ID Product", text="ID")
        self.table.heading("Name", text="Nombre")
        self.table.heading("Price", text="Precio")
        self.table.heading("Stock", text="Stock")

        # Ancho de columnas
        self.table.column("ID Product", width=40, anchor="center")
        self.table.column("Name", width=140)
        self.table.column("Price", width=70, anchor="e")
        self.table.column("Stock", width=60, anchor="center")
