import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from models.login_model import User
from views.home_view import DashboardVentana

bg_color = "#E5E5E5"
bl_color= "#BDBDBD"
c_color= "#3D5A80"
c_color_hover= "#14213D"
card_color = "#EDF2F4"      
sombra_color = "#BDBDBD"    

fuente= "Candara"

class LoginVentana:

    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self.root.geometry("890x670")
        self.root.configure(bg=bg_color)
        self.root.resizable(False, False)

        self._crear_interfaz()

    def _crear_interfaz(self):

        sombra = tk.Frame(self.root, bg=sombra_color)
        sombra.place(relx=0.5, rely=0.5, x=6, y=6, anchor="center", width=380, height=430)

        marco = tk.Frame(self.root, bg=card_color)
        marco.place(relx=0.5, rely=0.5, anchor="center", width=380, height=430)
       
        lbl_titulo = tk.Label(
            marco, text="Iniciar Sesión", bg=card_color, font=(fuente, 16, "bold")
        )
        lbl_titulo.pack(pady=25)

        lbl_usuario = tk.Label(
            marco, text="Usuario:",bg=card_color, font=(fuente, 12))
        lbl_usuario.pack(anchor="w", padx=50, pady=(5, 2))

        self.entry_usuario = tk.Entry(marco, font=(fuente, 11), relief="flat", highlightthickness=1,highlightbackground=bl_color ,highlightcolor=c_color)
        self.entry_usuario.pack(fill="x", padx=50,ipady=6)

        lbl_pass = tk.Label(marco, text="Contraseña:",bg=card_color,
                            font=(fuente, 12))
        lbl_pass.pack(anchor="w", padx=50, pady=(15,2))

        self.entry_pass = tk.Entry(marco, font=(fuente, 11), relief="flat",
            highlightthickness=1, highlightbackground= bl_color ,highlightcolor=c_color, show="*")
        self.entry_pass.pack(fill="x", padx=50, ipady=6)

        btn_ingresar = tk.Button(
            marco,
            text="Entrar",
            font=(fuente, 12, "bold"),
            bg=c_color,
            fg="white",
            cursor="hand2",
            relief="flat",
            highlightthickness=1,
            highlightbackground=bl_color,
            activebackground=c_color_hover,
            highlightcolor=c_color,
            command=self._validar_login,
        )
        btn_ingresar.pack(fill="x", padx=50, pady=30, ipady=6)

    def _validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get().strip()

        if not usuario_texto or not pass_texto:
            messagebox.showwarning(
                "Campos Vacíos", "Por favor ingresa usuario y contraseña."
            )
            return

        usuario_obj = User(usuario_texto, pass_texto)
        datos_usuario = usuario_obj.auth()

        if datos_usuario:
            id_emp = datos_usuario.get('id_employee')
            nombre_usuario = datos_usuario.get('username', 'Usuario')

            # Registrar en el historial únicamente si las credenciales son válidas
            usuario_obj.logeo_historial(id_emp, nombre_usuario)

            messagebox.showinfo(
                "Bienvenido", f"¡Hola {nombre_usuario}! Acceso concedido."
            )
            self._abrir_dashboard(nombre_usuario)
        else:
            messagebox.showerror(
                "Error de Acceso", "Usuario o contraseña incorrectos."
            )

    def _abrir_dashboard(self, nombre_completo):
        self.root.destroy()
        root_dashboard = tk.Tk()
        DashboardVentana(root_dashboard, nombre_completo)
        root_dashboard.mainloop()
