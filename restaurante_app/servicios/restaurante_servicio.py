from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    """Servicio de negocio que coordina las operaciones del restaurante."""

    def __init__(self, archivo_servicio: ArchivoServicio) -> None:
        self.archivo_servicio: ArchivoServicio = archivo_servicio
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.usuario_autenticado: Usuario | None = None
        self.inicializar_datos()

    def inicializar_datos(self) -> None:
        """Carga inicial de productos y usuarios."""
        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()

    def validar_acceso(self, identificacion: str, clave: str) -> tuple[bool, str]:
        """Valida credenciales de acceso."""
        id_clean = identificacion.strip()
        clave_clean = clave.strip()

        if not id_clean or not clave_clean:
            return False, "Por favor complete todos los campos."

        for usr in self.usuarios:
            if usr.identificacion.lower() == id_clean.lower() and usr.clave == clave_clean:
                self.usuario_autenticado = usr
                return True, f"Bienvenido/a, {usr.nombre}."

        return False, "Credenciales incorrectas. Verifique usuario y contraseña."

    def cerrar_sesion(self) -> None:
        self.usuario_autenticado = None

    def obtener_productos(self) -> list[Producto]:
        return self.productos

    def obtener_usuarios(self) -> list[Usuario]:
        return self.usuarios

    # CRUD DE PRODUCTOS

    def buscar_producto_por_codigo(self, codigo: str) -> Producto | None:
        cod_clean = codigo.strip().lower()
        for p in self.productos:
            if p.codigo.lower() == cod_clean:
                return p
        return None

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> tuple[bool, str]:
        if self.buscar_producto_por_codigo(codigo) is not None:
            return False, f"El código de producto '{codigo}' ya está registrado."

        try:
            nuevo = Producto(codigo, nombre, categoria, precio, stock)
            self.productos.append(nuevo)
            self.archivo_servicio.guardar_productos(self.productos)
            return True, f"Producto '{nuevo.nombre}' registrado con éxito."
        except ValueError as err:
            return False, str(err)

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> tuple[bool, str]:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False, f"No existe ningún producto registrado con código '{codigo}'."

        try:
            temp = Producto(codigo, nombre, categoria, precio, stock)
            producto.nombre = temp.nombre
            producto.categoria = temp.categoria
            producto.precio = temp.precio
            producto.stock = temp.stock
            self.archivo_servicio.guardar_productos(self.productos)
            return True, f"Producto '{codigo}' actualizado con éxito."
        except ValueError as err:
            return False, str(err)

    def eliminar_producto(self, codigo: str) -> tuple[bool, str]:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False, f"No existe ningún producto registrado con código '{codigo}'."

        self.productos.remove(producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return True, f"Producto '{codigo}' eliminado correctamente."