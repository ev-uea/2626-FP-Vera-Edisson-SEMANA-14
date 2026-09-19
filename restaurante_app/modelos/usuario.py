class Usuario:
    """Entidad que representa a un usuario registrado en el sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str, clave: str = "1234") -> None:
        if not identificacion.strip() or not nombre.strip() or not correo.strip():
            raise ValueError("Identificación, nombre y correo son obligatorios.")

        self.identificacion: str = identificacion.strip()
        self.nombre: str = nombre.strip()
        self.correo: str = correo.strip()
        self.clave: str = clave.strip()

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "clave": self.clave
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> "Usuario":
        return Usuario(
            identificacion=str(datos["identificacion"]),
            nombre=str(datos["nombre"]),
            correo=str(datos["correo"]),
            clave=str(datos.get("clave", "1234"))
        )