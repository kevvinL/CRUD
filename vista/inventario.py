import tkinter as menuvista
from tkinter import ttk

class GestionProductos:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Productos")
        self.master.geometry("1200x800")
        self.master.configure(bg='#f5f5f5')
        self.crearinterface()

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

        self.registrar = menuvista.Button(botonframe, text="Registrar productos" ,width=20, height=3, command=self.registros)
        self.registrar.place(x=500 , y= 30)

        self.guardar_button = menuvista.Button(botonframe, text="Eliminar", width=20, height=3 ,command=self.guardarProducto)
        self.guardar_button.place(x=300, y=30)

        self.eliminar_button = menuvista.Button(botonframe, text="Editar",width=20, height=3 ,command=self.eliminarProducto)
        self.eliminar_button.place(x=700, y=30)

    def registros(self):
        ventanaregistro = menuvista.Toplevel(self.master)
        ventanaregistro.title("Registro productos")
        ventanaregistro.geometry("600x300")
        ventanaregistro.config(bg="#ecf0f1")
        
        self.crearFormulario(ventanaregistro)
        
    def crearFormulario(self, parent):
        form_frame = self.frame(parent, 950, 150, '#ecf0f1')
        form_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        
        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        menuvista.Label(form_frame, text="Nombre:", bg='#ecf0f1').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        nombre_entry = menuvista.Entry(form_frame, width=30)
        nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        menuvista.Label(form_frame, text="Cantidad:", bg='#ecf0f1').grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.cantidad_entry = menuvista.Entry(form_frame, width=30)
        self.cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

        menuvista.Label(form_frame, text="Precio:", bg='#ecf0f1').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.precio_entry = menuvista.Entry(form_frame, width=30)
        self.precio_entry.grid(row=2, column=1, padx=10, pady=5)

        menuvista.Label(form_frame, text="Fecha:", bg='#ecf0f1').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.fecha_entry = menuvista.Entry(form_frame, width=30)
        self.fecha_entry.grid(row=3, column=1, padx=10, pady=5)

        self.boton = menuvista.Button(form_frame, text="Guardar", command=self.inventario)
        self.boton.place(x=230, y=150)

    def inventario(self):
        try:
            nombre = self.nombre_entry.get()
            cantidad = self.cantidad_entry.get()
            precio = self.precio_entry.get()
            fecha = self.fecha_entry.get()


            if not nombre or not cantidad or not precio or not fecha:
                print("Todos los campos son obligatorios")
                return False

            cantidad = int(cantidad)
            precio = float(precio)

            consulta = "INSERT INTO productos (nombre, cantidad, precio, fecha) VALUES (%s, %s, %s, %s)"
            valores = (nombre, cantidad, precio, fecha)

            self.cursor.execute(consulta, valores)
            self.conexion.commit()

            print("Producto registrado exitosamente")
            return True

        except Exception as e:
            print(f"Error al registrar producto: {e}")
            return False

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
        nombre = self.nombre_entry.get()
        cantidad = self.cantidad_entry.get()
        precio = self.precio_entry.get()
        fecha = self.fecha_entry.get()
        
        if nombre and cantidad and precio and fecha:
            self.productos_table.insert("", "end", values=(nombre, cantidad, precio, fecha))
            self.limpiarFormulario()

    def eliminarProducto(self):
        selected_item = self.productos_table.selection()
        if selected_item:
            self.productos_table.delete(selected_item)

    def editarProducto(self):
        selected_item = self.productos_table.selection()
        if selected_item:
            values = self.productos_table.item(selected_item, "values")
            self.nombre_entry.delete(0, "end")
            self.nombre_entry.insert(0, values[0])
            self.cantidad_entry.delete(0, "end")
            self.cantidad_entry.insert(0, values[1])
            self.precio_entry.delete(0, "end")
            self.precio_entry.insert(0, values[2])
            self.fecha_entry.delete(0, "end")
            self.fecha_entry.insert(0, values[3])
            self.productos_table.delete(selected_item)
    
    def limpiarFormulario(self):
        self.nombre_entry.delete(0, "end")
        self.cantidad_entry.delete(0, "end")
        self.precio_entry.delete(0, "end")
        self.fecha_entry.delete(0, "end")

    def crearinterface(self):
        self.encabezado()
        self.crearbotones(self.master)
        self.crearTabla(self.master)

if __name__ == "__main__":
    root = menuvista.Tk()
    app = GestionProductos(root)
    root.mainloop()
