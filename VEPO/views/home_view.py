from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from models.login_model import User
from models.ingreso_model import IngresoModel


class DashboardVentana:

    def __init__(
        self, root, nombre_usuario, on_registrar_callback=IngresoModel.guardar
    ):
        self.root = root
        self.root.title("Panel Principal - VEPO")
        self.root.geometry("1280x720")
        self.root.resizable(True, True)
        self.root.config(bg="#2b2b2b")

        self.nombre_usuario = nombre_usuario
        self.on_registrar_callback = on_registrar_callback

        # 1. Obtener id_employee y Rol directamente desde la Base de Datos (MVC)
        self.id_employee = IngresoModel.obtener_id_employee_por_username(
            self.nombre_usuario
        )
        id_rol = User.obtener_rol_por_username(self.nombre_usuario)
        # Suponiendo que el id_rol == 1 representa Administrador
        self.es_admin = id_rol == 1

        # Estado del menú lateral
        self.sidebar_visible = False

        # ================= BARRA SUPERIOR (HEADER) =================
        top_bar = tk.Frame(self.root, bg="#1e1e1e", height=50)
        top_bar.pack(side="top", fill="x")
        top_bar.pack_propagate(False)

        self.btn_hamburguesa = tk.Button(
            top_bar,
            text="☰",
            font=("Helvetica", 16, "bold"),
            bg="#1e1e1e",
            fg="white",
            bd=0,
            activebackground="#333333",
            activeforeground="white",
            cursor="hand2",
            command=self.toggle_sidebar,
        )
        self.btn_hamburguesa.pack(side="left", padx=(10, 5))

        lbl_vepo = tk.Label(
            top_bar,
            text="vepo",
            font=("Comic Sans MS", 14, "bold"),
            fg="white",
            bg="#1e1e1e",
        )
        lbl_vepo.pack(side="left", padx=10)

        btn_ingresos = tk.Button(
            top_bar,
            text="Ingresos",
            font=("Helvetica", 10, "bold"),
            bg="#4CAF50",
            fg="black",
            cursor="hand2",
            bd=0,
            padx=12,
            pady=3,
            command=lambda: self.mostrar_vista("ingresos"),
        )
        btn_ingresos.pack(side="left", padx=5)

        btn_egresos = tk.Button(
            top_bar,
            text="Egresos",
            font=("Helvetica", 10, "bold"),
            bg="#FF9800",
            fg="black",
            cursor="hand2",
            bd=0,
            padx=12,
            pady=3,
            command=lambda: self.mostrar_vista("egresos"),
        )
        btn_egresos.pack(side="left", padx=5)

        lbl_mensaje = tk.Label(
            top_bar,
            text=f"Usuario: {nombre_usuario}",
            font=("Helvetica", 10),
            fg="#cccccc",
            bg="#1e1e1e",
        )
        lbl_mensaje.pack(side="right", padx=15)

        # ================= CONTENEDOR PRINCIPAL =================
        self.body_container = tk.Frame(self.root, bg="#2b2b2b")
        self.body_container.pack(fill="both", expand=True)

        # ================= MENÚ LATERAL DESPLEGABLE (SIDEBAR) =================
        self.sidebar = tk.Frame(self.body_container, bg="#1e1e1e", width=220)

        lbl_menu_title = tk.Label(
            self.sidebar,
            text="OPCIONES",
            font=("Helvetica", 11, "bold"),
            fg="#888888",
            bg="#1e1e1e",
        )
        lbl_menu_title.pack(anchor="w", padx=15, pady=(20, 10))

        # Administrar Usuarios (Habilitado según el Rol consultado en la BD)
        btn_admin_user = tk.Button(
            self.sidebar,
            text="👥  Administrar Usuarios",
            font=("Helvetica", 10),
            bg="#1e1e1e",
            fg="white" if self.es_admin else "#666666",
            bd=0,
            anchor="w",
            padx=15,
            pady=10,
            cursor="hand2" if self.es_admin else "arrow",
            activebackground="#333333" if self.es_admin else "#1e1e1e",
            activeforeground="white" if self.es_admin else "#666666",
            command=self.abrir_administrar_usuarios,
        )
        btn_admin_user.pack(fill="x")

        # Cambiar Contraseña (Modal)
        btn_change_pass = tk.Button(
            self.sidebar,
            text="🔑  Cambiar Contraseña",
            font=("Helvetica", 10),
            bg="#1e1e1e",
            fg="white",
            bd=0,
            anchor="w",
            padx=15,
            pady=10,
            cursor="hand2",
            activebackground="#333333",
            activeforeground="white",
            command=self.abrir_cambiar_contrasena_modal,
        )
        btn_change_pass.pack(fill="x")

        separator = tk.Frame(self.sidebar, bg="#333333", height=1)
        separator.pack(fill="x", padx=10, pady=10)

        btn_cerrar_side = tk.Button(
            self.sidebar,
            text="🚪  Cerrar Sesión",
            font=("Helvetica", 10, "bold"),
            bg="#1e1e1e",
            fg="#f44336",
            bd=0,
            anchor="w",
            padx=15,
            pady=10,
            cursor="hand2",
            activebackground="#333333",
            activeforeground="#f44336",
            command=self.cerrar_sesion,
        )
        btn_cerrar_side.pack(fill="x")

        # ================= ÁREA DE CONTENIDO =================
        self.content_area = tk.Frame(self.body_container, bg="#2b2b2b")
        self.content_area.pack(side="right", fill="both", expand=True)

        # Cierre automático al hacer clic en el área principal
        self.content_area.bind(
            "<Button-1>", self.cerrar_sidebar_si_click_fuera)

        # Cargar vista predeterminada
        self.mostrar_vista("ingresos")

    # ---------------- MÉTODOS DE MENÚ Y NAVEGACIÓN ----------------
    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar.pack_forget()
            self.sidebar_visible = False
        else:
            self.sidebar.pack(side="left", fill="y", before=self.content_area)
            self.sidebar.pack_propagate(False)
            self.sidebar_visible = True

    def cerrar_sidebar_si_click_fuera(self, event):
        if self.sidebar_visible:
            self.toggle_sidebar()

    def abrir_administrar_usuarios(self):
        if not self.es_admin:
            messagebox.showwarning(
                "Acceso Denegado",
                "No tienes permisos de Administrador para acceder a este módulo.",
            )
            return
        if self.sidebar_visible:
            self.toggle_sidebar()
        messagebox.showinfo(
            "Módulo Usuarios", "Abriendo módulo de administración de usuarios..."
        )

    def abrir_cambiar_contrasena_modal(self):
        if self.sidebar_visible:
            self.toggle_sidebar()

        modal = tk.Toplevel(self.root)
        modal.title("Cambiar Contraseña")
        modal.geometry("380x280")
        modal.resizable(False, False)
        modal.config(bg="#2b2b2b")
        modal.grab_set()

        modal.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 190
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 140
        modal.geometry(f"+{x}+{y}")

        tk.Label(
            modal,
            text="Cambiar Contraseña",
            font=("Helvetica", 12, "bold"),
            fg="white",
            bg="#2b2b2b",
        ).pack(pady=15)

        frame_inputs = tk.Frame(modal, bg="#2b2b2b")
        frame_inputs.pack(padx=20, pady=5, fill="x")

        tk.Label(
            frame_inputs,
            text="Contraseña actual:",
            fg="white",
            bg="#2b2b2b",
            font=("Helvetica", 9),
        ).pack(anchor="w")
        txt_actual = tk.Entry(
            frame_inputs, show="*", bg="#3b3b3b", fg="white", font=("Helvetica", 10)
        )
        txt_actual.pack(fill="x", pady=(0, 10), ipady=3)

        tk.Label(
            frame_inputs,
            text="Nueva contraseña:",
            fg="white",
            bg="#2b2b2b",
            font=("Helvetica", 9),
        ).pack(anchor="w")
        txt_nueva = tk.Entry(
            frame_inputs, show="*", bg="#3b3b3b", fg="white", font=("Helvetica", 10)
        )
        txt_nueva.pack(fill="x", pady=(0, 15), ipady=3)

        def guardar_cambio():
            pass_act = txt_actual.get().strip()
            pass_nue = txt_nueva.get().strip()
            if not pass_act or not pass_nue:
                messagebox.showwarning(
                    "Campos vacíos", "Por favor completa ambos campos.", parent=modal
                )
                return
            messagebox.showinfo(
                "Éxito", "Contraseña actualizada correctamente.", parent=modal
            )
            modal.destroy()

        btn_guardar = tk.Button(
            modal,
            text="Guardar Cambio",
            bg="#245f8a",
            fg="white",
            font=("Helvetica", 10, "bold"),
            bd=0,
            pady=5,
            cursor="hand2",
            command=guardar_cambio,
        )
        btn_guardar.pack(fill="x", padx=20, pady=10)

    def cerrar_sesion(self):
        if messagebox.askyesno(
            "Cerrar Sesión", "¿Estás seguro de que deseas cerrar la sesión?"
        ):
            self.root.destroy()
            from views.login_view import LoginVentana

            root_login = tk.Tk()
            LoginVentana(root_login)
            root_login.mainloop()

    def mostrar_vista(self, tipo):
        for widget in self.content_area.winfo_children():
            widget.destroy()

        if tipo == "ingresos":
            self.construir_vista_ingresos()
        elif tipo == "egresos":
            self.construir_vista_egresos()

    # ---------------- VISTAS DE CONTENIDO ----------------
    def construir_vista_ingresos(self):
        self.content_area.bind(
            "<Button-1>", self.cerrar_sidebar_si_click_fuera)

        lbl_titulo = tk.Label(
            self.content_area,
            text="Registrar Ingreso",
            font=("Helvetica", 14, "bold"),
            fg="white",
            bg="#2b2b2b",
        )
        lbl_titulo.pack(anchor="w", padx=20, pady=(15, 10))

        form_frame = tk.Frame(self.content_area, bg="#2b2b2b")
        form_frame.pack(anchor="w", padx=20, pady=5)

        # 1. FECHA
        frame_fecha = tk.Frame(form_frame, bg="#2b2b2b")
        frame_fecha.pack(side="left", padx=(0, 20), anchor="n")

        tk.Label(
            frame_fecha,
            text="Fecha (dd/mm/aaaa)",
            font=("Helvetica", 10, "bold"),
            fg="white",
            bg="#2b2b2b",
        ).pack(anchor="w", pady=(0, 5))

        self.entrada_fecha = tk.Entry(
            frame_fecha,
            font=("Helvetica", 11),
            width=15,
            bg="#3b3b3b",
            fg="white",
            insertbackground="white",
            borderwidth=1,
            relief="solid",
        )
        self.entrada_fecha.pack(ipady=4)
        self.entrada_fecha.insert(0, datetime.now().strftime("%d/%m/%Y"))

        # 2. TIPO DE VENTA
        frame_tipo = tk.Frame(form_frame, bg="#2b2b2b")
        frame_tipo.pack(side="left", padx=(0, 20), anchor="n")

        tk.Label(
            frame_tipo,
            text="Tipo de venta",
            font=("Helvetica", 10, "bold"),
            fg="white",
            bg="#2b2b2b",
        ).pack(anchor="w", pady=(0, 5))

        self.tipo_venta_var = tk.StringVar(value="Ventana")
        opciones_venta = ["Ventana", "Ruta", "Garrafones"]
        for opc in opciones_venta:
            rb = tk.Radiobutton(
                frame_tipo,
                text=opc,
                variable=self.tipo_venta_var,
                value=opc,
                font=("Helvetica", 10),
                fg="white",
                bg="#2b2b2b",
                selectcolor="#3b3b3b",
                activebackground="#2b2b2b",
                activeforeground="white",
            )
            rb.pack(anchor="w", pady=2)

        # 3. CANTIDAD
        frame_cantidad = tk.Frame(form_frame, bg="#2b2b2b")
        frame_cantidad.pack(side="left", padx=(0, 20), anchor="n")

        tk.Label(
            frame_cantidad,
            text="Cantidad",
            font=("Helvetica", 10, "bold"),
            fg="white",
            bg="#2b2b2b",
        ).pack(anchor="w", pady=(0, 5))

        self.entrada_cantidad = tk.Entry(
            frame_cantidad,
            font=("Helvetica", 11),
            width=15,
            bg="#3b3b3b",
            fg="white",
            insertbackground="white",
            borderwidth=1,
            relief="solid",
        )
        self.entrada_cantidad.pack(ipady=4)

        # 4. BOTÓN REGISTRAR
        frame_boton = tk.Frame(form_frame, bg="#2b2b2b")
        frame_boton.pack(side="left", anchor="s", pady=(22, 0))

        btn_registrar = tk.Button(
            frame_boton,
            text="Registrar",
            font=("Helvetica", 11, "bold"),
            bg="#245f8a",
            fg="white",
            cursor="hand2",
            padx=15,
            pady=4,
            command=self.accion_registrar_ingreso,
        )
        btn_registrar.pack()

        # TABLA DE HISTORIAL DE VENTAS (Cargado directo desde la Base de Datos)
        lbl_historial = tk.Label(
            self.content_area,
            text="Historial de Ventas Guardadas (Base de Datos)",
            font=("Helvetica", 12, "bold"),
            fg="white",
            bg="#2b2b2b",
        )
        lbl_historial.pack(anchor="w", padx=20, pady=(25, 10))

        tabla_frame = tk.Frame(self.content_area, bg="#2b2b2b")
        tabla_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#3b3b3b",
            foreground="white",
            fieldbackground="#3b3b3b",
            rowheight=25,
        )
        style.configure(
            "Treeview.Heading",
            background="#1e1e1e",
            foreground="white",
            font=("Helvetica", 10, "bold"),
        )
        style.map("Treeview", background=[("selected", "#245f8a")])

        columnas = ("fecha", "tipo", "cantidad")
        self.tree_ingresos = ttk.Treeview(
            tabla_frame, columns=columnas, show="headings", height=8
        )

        self.tree_ingresos.heading("fecha", text="Fecha")
        self.tree_ingresos.heading("tipo", text="Tipo de Venta")
        self.tree_ingresos.heading("cantidad", text="Cantidad")

        self.tree_ingresos.column("fecha", anchor="center", width=150)
        self.tree_ingresos.column("tipo", anchor="center", width=200)
        self.tree_ingresos.column("cantidad", anchor="center", width=150)

        scrollbar = ttk.Scrollbar(
            tabla_frame, orient="vertical", command=self.tree_ingresos.yview
        )
        self.tree_ingresos.configure(yscroll=scrollbar.set)

        self.tree_ingresos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Cargar datos desde la base de datos al renderizar la vista
        self.actualizar_tabla_historial()

    def actualizar_tabla_historial(self):
        """Consulta las ventas registradas en la BD y llena la tabla (Treeview)."""
        if hasattr(self, "tree_ingresos"):
            for i in self.tree_ingresos.get_children():
                self.tree_ingresos.delete(i)

            # Consulta directa al Modelo (MVC)
            ventas_bd = IngresoModel.obtener_ventas()
            for reg in ventas_bd:
                self.tree_ingresos.insert(
                    "", "end", values=(reg["fecha"], reg["tipo"], reg["cantidad"])
                )

    def accion_registrar_ingreso(self):
        fecha = self.entrada_fecha.get().strip()
        tipo = self.tipo_venta_var.get()
        cantidad = self.entrada_cantidad.get().strip()

        if not cantidad or not cantidad.isdigit():
            messagebox.showerror(
                "Error de Validación",
                "Por favor ingresa un valor entero válido en la cantidad.",
            )
            return

        if self.id_employee is None:
            messagebox.showerror(
                "Error de Usuario",
                "No se pudo recuperar el ID del empleado para guardar la venta.",
            )
            return

        if self.on_registrar_callback:
            exito = self.on_registrar_callback(
                self.id_employee, fecha, tipo, int(cantidad)
            )
            if exito:
                # Refresca la tabla consultando nuevamente los datos insertados en la BD
                self.actualizar_tabla_historial()
                self.entrada_cantidad.delete(0, tk.END)
                messagebox.showinfo(
                    "Éxito", f"Ingreso de {tipo} registrado correctamente."
                )
            else:
                messagebox.showerror(
                    "Error BD",
                    "Ocurrió un error al intentar guardar en la base de datos.",
                )

    def construir_vista_egresos(self):
        self.content_area.bind(
            "<Button-1>", self.cerrar_sidebar_si_click_fuera)

        lbl_titulo = tk.Label(
            self.content_area,
            text="Gestión de Egresos",
            font=("Helvetica", 16, "bold"),
            fg="white",
            bg="#2b2b2b",
        )
        lbl_titulo.pack(pady=20)

        lbl_info = tk.Label(
            self.content_area,
            text="Aquí van los registros y formularios de egresos.",
            font=("Helvetica", 11),
            fg="#cccccc",
            bg="#2b2b2b",
        )
        lbl_info.pack(pady=5)
