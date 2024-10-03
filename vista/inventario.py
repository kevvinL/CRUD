import tkinter as menuvista
from tkinter import ttk
from tkinter import messagebox

class GestionProductos:
    def __init__(self, master, controlador):
        self.master = master
        self.master.title("Gestión de Productos")
        self.master.geometry("1200x800")
        self.master.configure(bg='#f5f5f5')
        self.controlador = controlador  
        self.crearinterface()
        self.cargarDatos()

    def cargarDatos(self):
        productos = self.controlador.consultaInventario("todos")
        
        # Limpiar la tabla antes de volver a cargar los datos
        self.productos_table.delete(*self.productos_table.get_children())
        
        for producto in productos:
            nombreP, cantidad, precio, categoria = producto.values()  # Extrae los valores del diccionario
            self.productos_table.insert("", "end", values=(nombreP, cantidad, precio, categoria))

    def frame(self, parent, width, height, bg):
        frame = menuvista.Frame(parent, width=width, height=height, bg=bg)
        frame.pack_propagate(False)
        return frame

    def encabezado(self):
        encabezadoframe = self.frame(self.master, 1200, 100, '#2c3e50')
        encabezadoframe.pack(side="top", fill="x")
        encabezadolabel = menuvista.Label(encabezadoframe, text="Gestión de Productos", font=("Helvetica", 24, "bold"), bg='#2c3e50', fg='white')
        encabezadolabel.pack(pady=20)
        return encabezadoframe

    def crearbotones(self, parent):
        botonframe = self.frame(parent, 950, 150, '#ecf0f1')
        botonframe.pack(side="top", fill="x", pady=10)

        self.registrar = menuvista.Button(botonframe, text="Crear Producto", width=20, height=3, command=self.controlador.iniciarCrearProducto)
        self.registrar.place(x=500, y=30)

        self.eliminar_button = menuvista.Button(botonframe, text="Eliminar Producto", width=20, height=3, command=self.controlador.iniciarEliminar)
        self.eliminar_button.place(x=300, y=30)

        self.editar_button = menuvista.Button(botonframe, text="Editar Producto", width=20, height=3, command=self.controlador.iniciarActualizacion)
        self.editar_button.place(x=700, y=30)

    def abrirVentanaRegistro(self):
        self.ventanaregistro = menuvista.Toplevel(self.master)
        self.ventanaregistro.title("Registro productos")
        self.ventanaregistro.geometry("600x300")
        self.ventanaregistro.config(bg="#ecf0f1")
        self.crearFormulario(self.ventanaregistro)

    def crearFormulario(self, parent):
        form_frame = self.frame(parent, 950, 150, '#ecf0f1')
        form_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        menuvista.Label(form_frame, text="Nombre:", bg='#ecf0f1').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.nombre_entry = menuvista.Entry(form_frame, width=30)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        menuvista.Label(form_frame, text="Cantidad:", bg='#ecf0f1').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.cantidad_entry = menuvista.Entry(form_frame, width=30)
        self.cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

        menuvista.Label(form_frame, text="Precio:", bg='#ecf0f1').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.precio_entry = menuvista.Entry(form_frame, width=30)
        self.precio_entry.grid(row=2, column=1, padx=10, pady=5)

        menuvista.Label(form_frame, text="Categoría:", bg='#ecf0f1').grid(row=3, column=0, padx=10, pady=5, sticky="e")

        # Combobox para seleccionar categoría
        self.categoria_var = ttk.Combobox(form_frame, values=["Seleccionar", "Tartas", "Galletas", "Cupcakes", "Postres Fríos"], state="readonly")
        self.categoria_var.current(0)  # Establece "Seleccionar" como valor inicial
        self.categoria_var.grid(row=3, column=1, padx=10, pady=5)

        self.boton = menuvista.Button(form_frame, text="Guardar", command=self.controlador.iniciarGuardarPro)
        self.boton.place(x=230, y=250)

    def crearTabla(self, parent):
        table_frame = self.frame(parent, 950, 500, '#ecf0f1')
        table_frame.pack(side="top", fill="both", expand=True)

        self.productos_table = ttk.Treeview(table_frame, columns=("Nombre", "Cantidad", "Precio", "Categoría"), show="headings")
        self.productos_table.heading("Nombre", text="Nombre")
        self.productos_table.heading("Cantidad", text="Cantidad")
        self.productos_table.heading("Precio", text="Precio")
        self.productos_table.heading("Categoría", text="Categoría")  # Cambiado a Categoría

        self.productos_table.column("Nombre", width=250)
        self.productos_table.column("Cantidad", width=150)
        self.productos_table.column("Precio", width=150)
        self.productos_table.column("Categoría", width=200)

        self.productos_table.pack(fill="both", expand=True)

    def guardarProducto(self):
        productoNuevo =  {
            "nombreP": self.nombre_entry.get(),
            "cantidad": self.cantidad_entry.get(),
            "precio": self.precio_entry.get(),
            "categoria": self.categoria_var.get()
        }
        
        if productoNuevo["nombreP"] and productoNuevo["cantidad"] and productoNuevo["precio"] and productoNuevo["categoria"] != "Seleccionar":
            guardado = self.controlador.GuardarProducto(productoNuevo)  # Llamada a la función del controlador
            if guardado:
                messagebox.showinfo("Confirmación", "Creado Correctamente")
                print("Producto guardado correctamente en la base de datos.")
                self.limpiarFormulario()
                self.ventanaregistro.destroy()
                self.cargarDatos()
            else:
                messagebox.showinfo("ERROR", "No se pudo guardar el producto.")
                print("Error al guardar el producto en la base de datos.")
        else:
            messagebox.showinfo("ERROR", "Por favor, complete todos los campos.")
            print("Por favor, completa todos los campos.")

    def limpiarFormulario(self):
        self.nombre_entry.delete(0, "end")
        self.cantidad_entry.delete(0, "end")
        self.precio_entry.delete(0, "end")

    def eliminarProducto(self):
        selected_item = self.productos_table.selection()
        if selected_item:
            item = self.productos_table.item(selected_item)
            producto_nombre = item['values'][0]
            confirmacion = self.controlador.eliminarProducto(producto_nombre)
            if confirmacion:
                messagebox.showinfo("Confirmación", "Producto eliminado correctamente")
                print("Producto eliminado correctamente de la base de datos.")
                self.productos_table.delete(selected_item)
            else:
                messagebox.showinfo("ERROR", "No se pudo eliminar el producto.")
                print("Error al eliminar el producto de la base de datos.")
        else:
            messagebox.showinfo("ERROR", "Seleccione un producto")
            print("Selecciona un producto para eliminar.")

    def editarProducto(self):
        selected_item = self.productos_table.selection()
        if selected_item:
            item = self.productos_table.item(selected_item)
            producto_nombre, cantidad, precio, categoria = item['values']
            
            self.ventanaedicion = menuvista.Toplevel(self.master)
            self.ventanaedicion.title("Editar producto")
            self.ventanaedicion.geometry("600x300")
            self.ventanaedicion.config(bg="#ecf0f1")
            
            self.crearFormularioEdicion(self.ventanaedicion, producto_nombre, cantidad, precio, categoria)
        else:
            messagebox.showinfo("ERROR", "Seleccione un producto para editar")
            print("Selecciona un producto para editar.")

    def crearFormularioEdicion(self, parent, nombreP, cantidad, precio, categoria):
        form_frame = self.frame(parent, 950, 150, '#ecf0f1')
        form_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        menuvista.Label(form_frame, text="Nombre:", bg='#ecf0f1').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.nombre_entry = menuvista.Entry(form_frame, width=30)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)
        self.nombre_entry.insert(0, nombreP)

        menuvista.Label(form_frame, text="Cantidad:", bg='#ecf0f1').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.cantidad_entry = menuvista.Entry(form_frame, width=30)
        self.cantidad_entry.grid(row=1, column=1, padx=10, pady=5)
        self.cantidad_entry.insert(0, cantidad)

        menuvista.Label(form_frame, text="Precio:", bg='#ecf0f1').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.precio_entry = menuvista.Entry(form_frame, width=30)
        self.precio_entry.grid(row=2, column=1, padx=10, pady=5)
        self.precio_entry.insert(0, precio)

        menuvista.Label(form_frame, text="Categoría:", bg='#ecf0f1').grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.categoria_var = ttk.Combobox(form_frame, values=["Seleccionar", "Tartas", "Galletas", "Cupcakes", "Postres Fríos"], state="readonly")
        self.categoria_var.grid(row=3, column=1, padx=10, pady=5)
        
        if categoria in self.categoria_var["values"]:
            self.categoria_var.set(categoria)

        self.boton = menuvista.Button(form_frame, text="Guardar", command=lambda: self.actualizarProducto(nombreP))
        self.boton.place(x=230, y=250)

    def actualizarProducto(self, nombre_original):
        productoActualizar = {
            "nombre_nuevo": nombre_original,
            "nombreP" : self.nombre_entry.get(),
            "cantidad" : self.cantidad_entry.get(),
            "precio" : self.precio_entry.get(),
            "categoria": self.categoria_var.get()
        }

        if productoActualizar["nombre_nuevo"] and productoActualizar["cantidad"] and productoActualizar["precio"] and productoActualizar["categoria"]:
            actualizado = self.controlador.actualizarProducto(productoActualizar)
            if actualizado:
                messagebox.showinfo("Confirmación", "Producto actualizado correctamente")
                print("Producto actualizado correctamente en la base de datos.")
                self.ventanaedicion.destroy()
                self.cargarDatos()
            else:
                messagebox.showinfo("ERROR", "No se pudo actualizar el producto.")
                print("Error al actualizar el producto en la base de datos.")
        else:
            messagebox.showinfo("ERROR", "Por favor, complete todos los campos.")
            print("Por favor, completa todos los campos.")

    def crearinterface(self):
        self.encabezado()
        self.crearbotones(self.master)
        self.crearTabla(self.master)
