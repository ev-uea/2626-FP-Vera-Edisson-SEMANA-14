import json
import os
from modelos.producto import Producto
from modelos.usuario import Usuario

class ArchivoServicio:
    """Servicio encargado de la lectura y escritura JSON."""

    def __init__(self, ruta_productos: str, ruta_usuarios: str) -> None:
        self.ruta_productos: str = ruta_productos
        self.ruta_usuarios: str = ruta_usuarios

    def guardar_productos(self, lista_productos: list[Producto]) -> bool:
        try:
            datos = [prod.a_diccionario() for prod in lista_productos]
            with open(self.ruta_productos, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"[Error Permiso]: No hay permisos para escribir en '{self.ruta_productos}'.")
            return False

    def cargar_productos(self) -> list[Producto]:
        productos: list[Producto] = []
        try:
            with open(self.ruta_productos, "r", encoding="utf-8") as archivo:
                contenido = json.load(archivo)
                for reg in contenido:
                    if isinstance(reg, dict):
                        productos.append(Producto.desde_diccionario(reg))
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            pass
        return productos

    def cargar_usuarios(self) -> list[Usuario]:
        usuarios: list[Usuario] = []
        try:
            with open(self.ruta_usuarios, "r", encoding="utf-8") as archivo:
                contenido = json.load(archivo)
                for reg in contenido:
                    if isinstance(reg, dict):
                        usuarios.append(Usuario.desde_diccionario(reg))
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            pass
        return usuarios