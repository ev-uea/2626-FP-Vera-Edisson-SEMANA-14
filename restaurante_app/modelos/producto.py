class Producto:
    """Entidad que representa un producto del restaurante con validaciones."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        if precio <= 0:
            raise ValueError("El precio debe ser un valor mayor a cero.")
        if stock < 0:
            raise ValueError("El stock no puede ser un valor negativo.")
        if not codigo.strip() or not nombre.strip() or not categoria.strip():
            raise ValueError("Código, nombre y categoría son campos obligatorios.")

        self.codigo: str = codigo.strip()
        self.nombre: str = nombre.strip()
        self.categoria: str = categoria.strip()
        self.precio: float = float(precio)
        self.stock: int = int(stock)

    def a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> "Producto":
        return Producto(
            codigo=str(datos["codigo"]),
            nombre=str(datos["nombre"]),
            categoria=str(datos["categoria"]),
            precio=float(datos["precio"]),
            stock=int(datos.get("stock", 0))
        )