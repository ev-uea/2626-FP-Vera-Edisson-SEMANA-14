import sys
import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class App(tk.Tk):
    """Ventana contenedora única de Tkinter que gestiona el flujo de vistas."""

    def __init__(self) -> None:
        super().__init__()

        self.title("Sistema de Gestión de Restaurante - Gourmet Express")
        self.geometry("820x540")
        self.minsize(780, 480)

        # Configurar Servicios
        ruta_productos = os.path.join(BASE_DIR, "datos", "productos.json")
        ruta_usuarios = os.path.join(BASE_DIR, "datos", "usuarios.json")

        self.archivo_servicio = ArchivoServicio(ruta_productos, ruta_usuarios)
        self.restaurante_servicio = RestauranteServicio(self.archivo_servicio)

        # Contenedor dinámico de vistas
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Vistas
        self.login_view = LoginView(
            parent=self.container,
            restaurante_servicio=self.restaurante_servicio,
            on_login_success=self.mostrar_main_view
        )

        self.main_view = MainView(
            parent=self.container,
            restaurante_servicio=self.restaurante_servicio,
            on_logout=self.mostrar_login_view
        )

        self.mostrar_login_view()

    def mostrar_login_view(self) -> None:
        self.main_view.pack_forget()
        self.login_view.pack(fill="both", expand=True)

    def mostrar_main_view(self) -> None:
        self.login_view.pack_forget()
        self.main_view.actualizar_datos_vista()
        self.main_view.pack(fill="both", expand=True)

def main() -> None:
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()