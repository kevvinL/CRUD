import tkinter as vistaProducto
from tkinter import ttk

class Inventario:
    def __init__(self, ventana):  # Corrige el nombre del método __init__
        self.ventana = ventana
        self.productos = [
            {"nombre": "Jamón", "cantidad": 10, "precio_venta": 15.5},
            {"nombre": "Queso", "cantidad": 20, "precio_venta": 12.0},
            {"nombre": "Salami", "cantidad": 30, "precio_venta": 8.0}
        ]
    
    def crearFormularioP(self):
        self.formulario = vistaProducto.Tk()
        self.formulario.title("Inventario de Productos")
        self.formulario.geometry("600x400")
        self.formulario.config(bg="white")
        return self.formulario
    
    def contenedor(self, datoContenedor):
        self.ventanaInventario = vistaProducto.Frame(datoContenedor)
        self.ventanaInventario.config(bg="white", width=600, height=350)  # Ajusta el tamaño del frame
        self.ventanaInventario.pack(fill="both", expand=True)
        return self.ventanaInventario
    
    def inventario(self, datoContenedor):
        titulo = vistaProducto.Label(datoContenedor, text="Gestión de Productos", font=("Arial", 24), bg="white")
        titulo.pack(pady=20)
        
        botonesFrame = vistaProducto.Frame(datoContenedor, bg="white")
        botonesFrame.pack(pady=10)
        
        botonCrear = vistaProducto.Button(botonesFrame, text="Crear Producto", width=15, height=2, command=self.crearProducto)
        botonCrear.grid(row=0, column=0, padx=10)
        
        botonEliminar = vistaProducto.Button(botonesFrame, text="Eliminar Producto", width=15, height=2, command=self.eliminarProducto)
        botonEliminar.grid(row=0, column=1, padx=10)
        
        botonEditar = vistaProducto.Button(botonesFrame, text="Editar Producto", width=15, height=2, command=self.editarProducto)
        botonEditar.grid(row=0, column=2, padx=10)
        
        columnas = ('nombre', 'cantidad', 'precio_venta')
        tabla = ttk.Treeview(datoContenedor, columns=columnas, show='headings')
        
        tabla.heading('nombre', text='Nombre')
        tabla.heading('cantidad', text='Cantidad')
        tabla.heading('precio_venta', text='Precio Venta')
        
        tabla.column('nombre', width=150)
        tabla.column('cantidad', width=100)
        tabla.column('precio_venta', width=100)
        
        for producto in self.productos:
            tabla.insert('', vistaProducto.END, values=(producto['nombre'], producto['cantidad'], producto['precio_venta']))
        tabla.pack(fill='both', expand=True)
    
    def crearProducto(self):
        ventanaCrear = vistaProducto.Toplevel(self.formulario)
        ventanaCrear.title("Crear Nuevo Producto")
        ventanaCrear.geometry("550x400")
        
        cabeceraCP = vistaProducto.Frame(ventanaCrear, bg="#A6775B")
        cabeceraCP.pack(fill='x', pady=10)
        
        tituloV = vistaProducto.Label(cabeceraCP, text="AGREGAR NUEVO PRODUCTO", font=("Arial", 24), bg="#A6775B", fg="white")
        tituloV.pack(pady=10)
        
        camposFrame = vistaProducto.Frame(ventanaCrear)
        camposFrame.pack(padx=20, pady=20)

        nombreLabel = vistaProducto.Label(camposFrame, text="Nombre del producto:")
        nombreLabel.grid(row=0, column=0, pady=5, sticky='e')

        self.nombreEntry = vistaProducto.Entry(camposFrame)
        self.nombreEntry.grid(row=0, column=1, pady=5)

        cantidadLabel = vistaProducto.Label(camposFrame, text="Cantidad Producto:")
        cantidadLabel.grid(row=1, column=0, pady=5, sticky='e')

        self.cantidadEntry = vistaProducto.Entry(camposFrame)
        self.cantidadEntry.grid(row=1, column=1, pady=5)
        
        precioVLabel = vistaProducto.Label(camposFrame, text="Precio Venta:")
        precioVLabel.grid(row=2, column=0, pady=5, sticky='e')

        self.precioVEntry = vistaProducto.Entry(camposFrame)
        self.precioVEntry.grid(row=2, column=1, pady=5)
        
        guardarBoton = vistaProducto.Button(camposFrame, text="Guardar", width=10, height=2, command=self.guardarProducto)
        guardarBoton.grid(row=3, column=1, pady=10)
    
    def guardarProducto(self):
        nombre = self.nombreEntry.get()
        cantidad = self.cantidadEntry.get()
        precio = self.precioVEntry.get()

        if nombre and cantidad and precio:
            # Agregar el nuevo producto a la lista de productos
            self.productos.append({
                "nombre": nombre,
                "cantidad": int(cantidad),
                "precio_venta": float(precio)
            })
            print(f"Producto guardado: {nombre}, {cantidad}, {precio}")
            self.formulario.destroy()
            self.crearFormularioP()
            self.contenedor(self.formulario)
            self.inventario(self.ventanaInventario)
        else:
            print("Por favor, completa todos los campos.")

    def eliminarProducto(self):
        print("Eliminar Producto - Implementar funcionalidad")
    
    def editarProducto(self):
        print("Editar Producto - Implementar funcionalidad")

