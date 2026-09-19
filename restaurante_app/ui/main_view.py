import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio

class MainView(ttk.Frame):
    """Panel principal con gestión de Productos (CRUD) y consulta de Usuarios."""

    def __init__(self, parent: tk.Widget, restaurante_servicio: RestauranteServicio, on_logout: callable) -> None:
        super().__init__(parent)
        self.restaurante_servicio: RestauranteServicio = restaurante_servicio
        self.on_logout: callable = on_logout

        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        # Contenedor Superior (Header)
        header = ttk.Frame(self, padding=10)
        header.pack(fill="x", side="top")

        self.lbl_bienvenida = ttk.Label(header, text="Bienvenido/a", font=("Helvetica", 14, "bold"))
        self.lbl_bienvenida.pack(side="left")

        btn_logout = ttk.Button(header, text="Cerrar Sesión", command=self._cerrar_sesion)
        btn_logout.pack(side="right")

        # Control de Pestañas (Notebook)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 1: Productos (CRUD Formulario + Tabla)
        self.tab_productos = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_productos, text="Gestión de Productos")
        self._construir_pestana_productos()

        # Pestaña 2: Usuarios (Consulta)
        self.tab_usuarios = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_usuarios, text="Usuarios Registrados")
        self._construir_pestana_usuarios()

    def _construir_pestana_productos(self) -> None:
        # Panel Izquierdo: Formulario y Acciones
        frame_form = ttk.LabelFrame(self.tab_productos, text=" Datos del Producto ", padding=10)
        frame_form.pack(side="left", fill="y", padx=(0, 10))

        # Campos del Formulario usando Grid
        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, sticky="w", pady=4)
        self.ent_codigo = ttk.Entry(frame_form, width=20)
        self.ent_codigo.grid(row=0, column=1, pady=4, padx=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="w", pady=4)
        self.ent_nombre = ttk.Entry(frame_form, width=20)
        self.ent_nombre.grid(row=1, column=1, pady=4, padx=5)

        ttk.Label(frame_form, text="Categoría:").grid(row=2, column=0, sticky="w", pady=4)
        self.cmb_categoria = ttk.Combobox(
            frame_form,
            values=["Comida Rápida", "Bebidas", "Postres", "Entradas", "Platos Fuertes"],
            width=18,
            state="normal"
        )
        self.cmb_categoria.grid(row=2, column=1, pady=4, padx=5)

        ttk.Label(frame_form, text="Precio ($):").grid(row=3, column=0, sticky="w", pady=4)
        self.ent_precio = ttk.Entry(frame_form, width=20)
        self.ent_precio.grid(row=3, column=1, pady=4, padx=5)

        ttk.Label(frame_form, text="Stock:").grid(row=4, column=0, sticky="w", pady=4)
        self.ent_stock = ttk.Entry(frame_form, width=20)
        self.ent_stock.grid(row=4, column=1, pady=4, padx=5)

        # Botones de Acción (command=)
        frame_botones = ttk.Frame(frame_form, padding=(0, 10, 0, 0))
        frame_botones.grid(row=5, column=0, columnspan=2, sticky="ew")

        btn_registrar = ttk.Button(frame_botones, text="Registrar", command=self._cmd_registrar)
        btn_registrar.pack(fill="x", pady=2)

        btn_consultar = ttk.Button(frame_botones, text="Cargar / Buscar", command=self._cmd_consultar)
        btn_consultar.pack(fill="x", pady=2)

        btn_actualizar = ttk.Button(frame_botones, text="Actualizar", command=self._cmd_actualizar)
        btn_actualizar.pack(fill="x", pady=2)

        btn_eliminar = ttk.Button(frame_botones, text="Eliminar", command=self._cmd_eliminar)
        btn_eliminar.pack(fill="x", pady=2)

        btn_limpiar = ttk.Button(frame_botones, text="Limpiar Formulario", command=self._limpiar_formulario_productos)
        btn_limpiar.pack(fill="x", pady=(8, 2))

        # Panel Derecho: Tabla de Presentación
        frame_tabla = ttk.LabelFrame(self.tab_productos, text=" Catálogo Registrado ", padding=10)
        frame_tabla.pack(side="right", fill="both", expand=True)

        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        self.tree_productos = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

        self.tree_productos.heading("codigo", text="Código")
        self.tree_productos.heading("nombre", text="Nombre")
        self.tree_productos.heading("categoria", text="Categoría")
        self.tree_productos.heading("precio", text="Precio ($)")
        self.tree_productos.heading("stock", text="Stock")

        self.tree_productos.column("codigo", width=70, anchor="center")
        self.tree_productos.column("nombre", width=180, anchor="w")
        self.tree_productos.column("categoria", width=110, anchor="center")
        self.tree_productos.column("precio", width=70, anchor="e")
        self.tree_productos.column("stock", width=60, anchor="center")

        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree_productos.yview)
        self.tree_productos.configure(yscrollcommand=scrollbar.set)

        self.tree_productos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _construir_pestana_usuarios(self) -> None:
        frame_tabla = ttk.LabelFrame(self.tab_usuarios, text=" Usuarios del Sistema ", padding=10)
        frame_tabla.pack(fill="both", expand=True)

        columnas = ("identificacion", "nombre", "correo")
        self.tree_usuarios = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

        self.tree_usuarios.heading("identificacion", text="ID / Cédula")
        self.tree_usuarios.heading("nombre", text="Nombre Completo")
        self.tree_usuarios.heading("correo", text="Correo Electrónico")

        self.tree_usuarios.column("identificacion", width=120, anchor="center")
        self.tree_usuarios.column("nombre", width=220, anchor="w")
        self.tree_usuarios.column("correo", width=220, anchor="w")

        self.tree_usuarios.pack(fill="both", expand=True)

    # ACCIONES BOTONES DE PRODUCTOS (command=)

    def _cmd_registrar(self) -> None:
        try:
            cod = self.ent_codigo.get()
            nom = self.ent_nombre.get()
            cat = self.cmb_categoria.get()
            pre = float(self.ent_precio.get())
            stk = int(self.ent_stock.get())

            exito, mensaje = self.restaurante_servicio.registrar_producto(cod, nom, cat, pre, stk)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self._limpiar_formulario_productos()
                self._actualizar_tabla_productos()
            else:
                messagebox.showwarning("Atención", mensaje)

        except ValueError:
            messagebox.showerror("Error de Datos", "Precio y Stock deben ser números válidos (Precio float, Stock int).")

    def _cmd_consultar(self) -> None:
        cod = self.ent_codigo.get().strip()
        if not cod:
            messagebox.showwarning("Atención", "Ingrese un Código en el formulario para buscar el producto.")
            return

        prod = self.restaurante_servicio.buscar_producto_por_codigo(cod)
        if prod:
            self.ent_nombre.delete(0, tk.END)
            self.ent_nombre.insert(0, prod.nombre)

            self.cmb_categoria.set(prod.categoria)

            self.ent_precio.delete(0, tk.END)
            self.ent_precio.insert(0, str(prod.precio))

            self.ent_stock.delete(0, tk.END)
            self.ent_stock.insert(0, str(prod.stock))

            messagebox.showinfo("Producto Encontrado", f"Datos de '{prod.nombre}' cargados en el formulario.")
        else:
            messagebox.showwarning("No Encontrado", f"No se encontró producto con código '{cod}'.")

    def _cmd_actualizar(self) -> None:
        try:
            cod = self.ent_codigo.get()
            nom = self.ent_nombre.get()
            cat = self.cmb_categoria.get()
            pre = float(self.ent_precio.get())
            stk = int(self.ent_stock.get())

            exito, mensaje = self.restaurante_servicio.actualizar_producto(cod, nom, cat, pre, stk)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self._limpiar_formulario_productos()
                self._actualizar_tabla_productos()
            else:
                messagebox.showwarning("Atención", mensaje)

        except ValueError:
            messagebox.showerror("Error de Datos", "Asegúrese de ingresar un Precio y Stock numéricos válidos.")

    def _cmd_eliminar(self) -> None:
        cod = self.ent_codigo.get().strip()
        if not cod:
            messagebox.showwarning("Atención", "Ingrese el Código del producto que desea eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de eliminar el producto '{cod}'?")
        if confirmar:
            exito, mensaje = self.restaurante_servicio.eliminar_producto(cod)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self._limpiar_formulario_productos()
                self._actualizar_tabla_productos()
            else:
                messagebox.showwarning("Atención", mensaje)

    # MÉTODOS AUXILIARES Y ACTUALIZACIÓN

    def _limpiar_formulario_productos(self) -> None:
        self.ent_codigo.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.cmb_categoria.set("")
        self.ent_precio.delete(0, tk.END)
        self.ent_stock.delete(0, tk.END)
        self.ent_codigo.focus()

    def _actualizar_tabla_productos(self) -> None:
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)

        for p in self.restaurante_servicio.obtener_productos():
            self.tree_productos.insert("", "end", values=(p.codigo, p.nombre, p.categoria, f"{p.precio:.2f}", p.stock))

    def _actualizar_tabla_usuarios(self) -> None:
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)

        for u in self.restaurante_servicio.obtener_usuarios():
            self.tree_usuarios.insert("", "end", values=(u.identificacion, u.nombre, u.correo))

    def actualizar_datos_vista(self) -> None:
        """Actualiza el nombre de bienvenida y recarga las tablas solicitando datos al servicio."""
        usr = self.restaurante_servicio.usuario_autenticado
        if usr:
            self.lbl_bienvenida.config(text=f"Bienvenido/a, {usr.nombre}")

        self._actualizar_tabla_productos()
        self._actualizar_tabla_usuarios()

    def _cerrar_sesion(self) -> None:
        self.restaurante_servicio.cerrar_sesion()
        self.on_logout()