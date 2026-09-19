# Sistema de Gestión de Restaurante - Semana 14 (Componentes y Contenedores UI)

**Estudiante:** Edisson Valentin Vera Gamboa  
**Asignatura:** Programación Orientada a Objetos   
**Semana:** 14 - Formulario CRUD y Contenedores Tkinter

---

## 1. Propósito de la Aplicación
Esta versión evoluciona la interfaz gráfica de `restaurante_app` integrando un panel de administración para la gestión completa de Productos (Crear, Consultar/Cargar, Actualizar y Eliminar). Aplica componentes y contenedores Tkinter/ttk sin alterar la arquitectura modular ni las responsabilidades de servicio.

---

## 2. Estructura del Proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json          # Persistencia JSON de productos
│   └── usuarios.json           # Persistencia JSON de usuarios
├── modelos/
│   ├── producto.py             # Entidad Producto con validaciones
│   └── usuario.py              # Entidad Usuario
├── servicios/
│   ├── archivo_servicio.py     # Lectura y escritura en disco
│   └── restaurante_servicio.py # Lógica de negocio y reglas de validación
├── ui/
│   ├── login_view.py           # Pantalla de autenticación
│   └── main_view.py            # Panel con formulario CRUD y tablas Treeview
├── main.py                     # Punto de entrada y ciclo de vida tk.Tk
└── README.md                   # Documentación técnica