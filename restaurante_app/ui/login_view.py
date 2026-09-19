import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio

class LoginView(ttk.Frame):
    """Vista gráfica de inicio de sesión."""

    def __init__(self, parent: tk.Widget, restaurante_servicio: RestauranteServicio, on_login_success: callable) -> None:
        super().__init__(parent)
        self.restaurante_servicio: RestauranteServicio = restaurante_servicio
        self.on_login_success: callable = on_login_success

        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        card = ttk.LabelFrame(self, text=" Acceso al Sistema ", padding=25)
        card.pack(expand=True, padx=20, pady=20)

        lbl_titulo = ttk.Label(card, text="Gourmet Express", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=(0, 15))

        ttk.Label(card, text="Usuario / ID:").pack(anchor="w")
        self.ent_usuario = ttk.Entry(card, width=30)
        self.ent_usuario.pack(pady=(2, 10))
        self.ent_usuario.focus()

        ttk.Label(card, text="Contraseña:").pack(anchor="w")
        self.ent_clave = ttk.Entry(card, width=30, show="*")
        self.ent_clave.pack(pady=(2, 15))

        btn_ingresar = ttk.Button(card, text="Iniciar Sesión", command=self._procesar_login)
        btn_ingresar.pack(fill="x", pady=5)

        self.ent_clave.bind("<Return>", lambda event: self._procesar_login())

    def _procesar_login(self) -> None:
        usr = self.ent_usuario.get()
        clave = self.ent_clave.get()

        exito, mensaje = self.restaurante_servicio.validar_acceso(usr, clave)

        if exito:
            messagebox.showinfo("Acceso Correcto", mensaje)
            self.limpiar_campos()
            self.on_login_success()
        else:
            messagebox.showwarning("Error de Acceso", mensaje)

    def limpiar_campos(self) -> None:
        self.ent_usuario.delete(0, tk.END)
        self.ent_clave.delete(0, tk.END)
        self.ent_usuario.focus()