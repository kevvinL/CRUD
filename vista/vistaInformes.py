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

        self.filtro_frame = menuvista.Frame(ProductoFrame, bg='#ecf0f1')
        self.filtro_frame.pack(side="top", fill="x", padx=10, pady=5)

        generarInforme = menuvista.Button(self.filtro_frame, text="Generar Informe", bg='#3498db', fg='white', command= self.controlador.guardarInforme)
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
        self.productos = self.controlador.ProductosInformes("todos")
        print(self.productos, "informes")  # Para verificar el contenido cargado
        if not self.productos:
            print("No hay productos para incluir en el informe.")
        else:
            # Ordenar y actualizar tabla
            self.productos = sorted(self.productos, key=lambda x: x["cantidad"], reverse=True)
            self.controlador.asignarProductos(self.productos)
            self.actualizar_tabla(self.productos)

    def actualizar_tabla(self, productos):
        # Limpiar tabla antes de actualizar
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        # Insertar productos en la tabla
        for producto in productos:
            self.treeview.insert("", "end", values=(producto["nombreP"], producto["cantidad"], producto["precio"], producto["categoria"]))
    
    def confirmacion(self, mensaje):
        mensajes = mensaje["mensaje"]
        if mensaje["confirmacion"] == "creado":
            messagebox.showinfo("Confirmación", mensajes)
        elif mensaje["confirmacion"] == "fallido":
            messagebox.showerror("ERROR", mensajes)

