import tkinter as menuvista
from tkinter import ttk
from tkinter import messagebox
import json

class Menu:
    def __init__(self, master, controlador):
        self.master = master
        self.controlador = controlador
        self.master.title("Informes")
        self.master.geometry("1200x800")
        self.master.configure(bg='#f5f5f5')
        self.crearinterface()
        self.productos = []  # Lista para almacenar los productos
        self.filtrados = []  # Lista para almacenar productos filtrados
    
    def frame(self, parent, width, height, bg):
        frame = menuvista.Frame(parent, width=width, height=height, bg=bg)
        frame.pack_propagate(False)
        return frame

    def encabezado(self):
        encabezadoframe = self.frame(self.master, 1200, 100, '#2c3e50')
        encabezadoframe.pack(side="top", fill="x")
        encabezadolabel = menuvista.Label(encabezadoframe, text="Reposteria sugarCode", font=("Helvetica", 24, "bold"), bg='#2c3e50', fg='white')
        encabezadolabel.pack(pady=20)
        return encabezadoframe

    def Titulocatalogo(self, parent):
        CatalogoTituloFrame = self.frame(parent, 950, 50, '#ecf0f1')
        CatalogoTituloFrame.pack(side="top", fill="x")
        CatalogoTituloLabel = menuvista.Label(CatalogoTituloFrame, text="Informe de Productos - Más Vendidos", font=("Helvetica", 18, "bold"), bg='#ecf0f1')
        CatalogoTituloLabel.pack(pady=10)
        return CatalogoTituloFrame

    def Productos(self, parent):
        ProductoFrame = self.frame(parent, 950, 600, '#ecf0f1')  # Agrandar la tabla a 600px de alto
        ProductoFrame.pack(side="top", fill="both", expand=True)

        # Agregar campo de búsqueda y botón de filtrar
        self.filtro_frame = menuvista.Frame(ProductoFrame, bg='#ecf0f1')
        self.filtro_frame.pack(side="top", fill="x", padx=10, pady=5)

        generarInforme = menuvista.Button(self.filtro_frame, text="Generar Informe", bg='#3498db', fg='white', command="dnsdj")
        generarInforme.pack(side="left", padx=5)

        self.treeview = self.CrearTabla(ProductoFrame, "Más Vendidos", 10, 50)

        return ProductoFrame

    def CrearTabla(self, parent, titulo, x_position, y_position):
        tableframe = menuvista.Frame(parent, width=1000, height=500, bg='white', bd=1, relief=menuvista.RAISED)
        tableframe.place(x=x_position, y=y_position)

        columnas = ("Producto", "Cantidad", "Precio", "Categoria")
        treeview = ttk.Treeview(tableframe, columns=columnas, show="headings", height=20)  # Altura ajustada

        treeview.heading("Producto", text="Producto")
        treeview.heading("Cantidad", text="Cantidad")
        treeview.heading("Precio", text="Precio")
        treeview.heading("Categoria", text="Categoria")

        # Ajustar el tamaño de las columnas
        treeview.column("Producto", anchor='center', width=300)
        treeview.column("Cantidad", anchor='center', width=100)
        treeview.column("Precio", anchor='center', width=100)
        treeview.column("Categoria", anchor='center', width=150)

        treeview.pack(fill="both", expand=True)

        return treeview

    def crearinterface(self):
        self.encabezado()
        self.Titulocatalogo(self.master)
        self.Productos(self.master)
        self.cargar_productos()  # Cargar productos iniciales

    def cargar_productos(self):
        # Obtener productos desde la base de datos
        self.productos = self.controlador.ProductosInformes("todos")
        print(self.productos, "informes")
        #self.modelo.obtener_productos()  # Cambia a tu método real

        # Ordenar los productos por cantidad de mayor a menor
        self.productos = sorted(self.productos, key=lambda x: x["cantidad"], reverse=True)

        self.actualizar_tabla(self.productos)

    def guardarInforme(self):
        try:
            # Cargar productos desde el archivo JSON
            with open("productos.json", "r") as json_file:
                productos = json.load(json_file)

            # Generar el informe en el archivo .txt
            with open("informeProductos.txt", "w") as file:
                # Titulo del archivo
                file.write("Informe de Productos\n")
                file.write("=====================\n\n")

                # Revisa que tenga productos disponibles
                if productos:
                    for producto in productos:
                        file.write(f"Nombre: {producto['nombreP']}\n")
                        file.write(f"Cantidad: {producto['cantidad']}\n")
                        file.write(f"Precio: {producto['precio']}\n")
                        file.write(f"Categoria: {producto['categoria']}\n")
                        file.write("-------------------------------\n")
                    print("Informe generado exitosamente.")
                    messagebox.showinfo("Confirmación", "Informe creado correctamente")
                else:
                    file.write("No hay productos disponibles en el inventario.\n")
                    print("No hay productos para incluir en el informe.")
                    messagebox.showerror("ERROR", "Error al crear el informe")
        except Exception as e:
            print(f"Error al guardar el informe: {e}")
            messagebox.showerror("ERROR", "Error al guardar el informe")
    
    def actualizar_tabla(self, productos):
        # Limpiar tabla antes de actualizar
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        # Insertar productos en la tabla
        for producto in productos:
            self.treeview.insert("", "end", values=(producto["nombreP"], producto["cantidad"], producto["precio"], producto["categoria"]))

