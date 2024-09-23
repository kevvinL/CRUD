import tkinter as menuvista
from tkinter import ttk
from modelo.modelobk import modelo

class GestionProductos:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Productos")
        self.master.geometry("1200x800")
        self.master.configure(bg='#f5f5f5')
        self.crearinterface()
        self.cargarDatos()

    def cargarDatos(self):
        modelo_bd = modelo()
        productos = modelo_bd.obtener_productos()  # Método que devuelve los productos guardados
        
        # Limpiar la tabla antes de volver a cargar los datos
        self.productos_table.delete(*self.productos_table.get_children())
        
        for producto in productos:
            nombreP, cantidad, precio, fecha = producto.values()  # Extrae los valores del diccionario
            self.productos_table.insert("", "end", values=(nombreP, cantidad, precio, fecha))

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

        self.registrar = menuvista.Button(botonframe, text="Registrar productos", width=20, height=3, command=self.abrirVentanaRegistro)
        self.registrar.place(x=500, y=30)

        self.guardar_button = menuvista.Button(botonframe, text="Eliminar", width=20, height=3, command=self.eliminarProducto)
        self.guardar_button.place(x=300, y=30)

        self.eliminar_button = menuvista.Button(botonframe, text="Editar", width=20, height=3 , command=self.editarProducto)
        self.eliminar_button.place(x=700, y=30)

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

        menuvista.Label(form_frame, text="Fecha:", bg='#ecf0f1').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.fecha_entry = menuvista.Entry(form_frame, width=30)
        self.fecha_entry.grid(row=3, column=1, padx=10, pady=5)
        

        self.boton = menuvista.Button(form_frame, text="Guardar", command=self.guardarProducto)
        self.boton.place(x=230, y=150)

    def crearTabla(self, parent):
        table_frame = self.frame(parent, 950, 500, '#ecf0f1')
        table_frame.pack(side="top", fill="both", expand=True)

        self.productos_table = ttk.Treeview(table_frame, columns=("Nombre", "Cantidad", "Precio", "Fecha"), show="headings")
        self.productos_table.heading("Nombre", text="Nombre")
        self.productos_table.heading("Cantidad", text="Cantidad")
        self.productos_table.heading("Precio", text="Precio")
        self.productos_table.heading("Fecha", text="Fecha")

        self.productos_table.column("Nombre", width=250)
        self.productos_table.column("Cantidad", width=150)
        self.productos_table.column("Precio", width=150)
        self.productos_table.column("Fecha", width=200)

        self.productos_table.pack(fill="both", expand=True)

    def guardarProducto(self):
        nombreP = self.nombre_entry.get()
        cantidad = self.cantidad_entry.get()
        precio = self.precio_entry.get()
        fecha = self.fecha_entry.get()

        if nombreP and cantidad and precio and fecha:
            modelo_bd = modelo()  
            guardado = modelo_bd.inventario(nombreP, cantidad, precio, fecha)

            if guardado:
                print("Producto guardado correctamente en la base de datos.")
                self.limpiarFormulario()
                self.cargarDatos()
            else:
                print("Error al guardar el producto en la base de datos.")
        else:
            print("Por favor, completa todos los campos.")

    def limpiarFormulario(self):
        self.nombre_entry.delete(0, "end")
        self.cantidad_entry.delete(0, "end")
        self.precio_entry.delete(0, "end")
        self.fecha_entry.delete(0, "end")

    def eliminarProducto(self):
        selected_item = self.productos_table.selection()
        if selected_item:
            item = self.productos_table.item(selected_item)
            producto_nombre = item['values'][0]
            
            modelo_bd = modelo()
            eliminacion_exitosa = modelo_bd.eliminar_producto(producto_nombre)

            if eliminacion_exitosa:
                print("Producto eliminado correctamente de la base de datos.")
                self.productos_table.delete(selected_item)
            else:
                print("Error al eliminar el producto de la base de datos.")
        else:
            print("Selecciona un producto para eliminar.")

    def editarProducto(self):
        selected_item = self.productos_table.selection()
        
        if selected_item:
            # Obtener los datos del producto seleccionado
            item = self.productos_table.item(selected_item)
            producto_nombre, cantidad, precio, fecha = item['values']
            
            # Abrir la ventana de edición
            self.ventanaedicion = menuvista.Toplevel(self.master)
            self.ventanaedicion.title("Editar producto")
            self.ventanaedicion.geometry("600x300")
            self.ventanaedicion.config(bg="#ecf0f1")
            
            # Crear el formulario con los datos del producto
            self.crearFormularioEdicion(self.ventanaedicion, producto_nombre, cantidad, precio, fecha)
        else:
            print("Selecciona un producto para editar.")

    def crearFormularioEdicion(self, parent, nombreP, cantidad, precio, fecha):
        form_frame = self.frame(parent, 950, 150, '#ecf0f1')
        form_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        menuvista.Label(form_frame, text="Nombre:", bg='#ecf0f1').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.nombre_entry = menuvista.Entry(form_frame, width=30)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)
        self.nombre_entry.insert(0, nombreP)  # Poner el valor actual en el campo de entrada

        menuvista.Label(form_frame, text="Cantidad:", bg='#ecf0f1').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.cantidad_entry = menuvista.Entry(form_frame, width=30)
        self.cantidad_entry.grid(row=1, column=1, padx=10, pady=5)
        self.cantidad_entry.insert(0, cantidad)

        menuvista.Label(form_frame, text="Precio:", bg='#ecf0f1').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.precio_entry = menuvista.Entry(form_frame, width=30)
        self.precio_entry.grid(row=2, column=1, padx=10, pady=5)
        self.precio_entry.insert(0, precio)

        menuvista.Label(form_frame, text="Fecha:", bg='#ecf0f1').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.fecha_entry = menuvista.Entry(form_frame, width=30)
        self.fecha_entry.grid(row=3, column=1, padx=10, pady=5)
        self.fecha_entry.insert(0, fecha)

        self.boton = menuvista.Button(form_frame, text="Guardar cambios", command=lambda: self.actualizarProducto(nombreP))
        self.boton.place(x=230, y=150)


    def actualizarProducto(self, nombre_original):
        nombreP = self.nombre_entry.get()
        cantidad = self.cantidad_entry.get()
        precio = self.precio_entry.get()
        fecha = self.fecha_entry.get()

        if nombreP and cantidad and precio and fecha:
            modelo_bd = modelo()  
            actualizado = modelo_bd.actualizar_producto(nombre_original, nombreP, cantidad, precio, fecha)

            if actualizado:
                print("Producto actualizado correctamente en la base de datos.")
                self.ventanaedicion.destroy()
                self.cargarDatos()  # Actualiza la tabla con los nuevos datos
            else:
                print("Error al actualizar el producto en la base de datos.")
        else:
            print("Por favor, completa todos los campos.")


    def crearinterface(self):
        self.encabezado()
        self.crearbotones(self.master)
        self.crearTabla(self.master)