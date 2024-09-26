import tkinter as menuvista
from tkinter import ttk
from modelo.modelobk import modelo

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu principal")
        self.master.geometry("1200x800")
        self.master.configure(bg='#f5f5f5')
        self.modelo = modelo()  # Crear una instancia del modelo
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

        self.buscador_entry = menuvista.Entry(self.filtro_frame, width=40)
        self.buscador_entry.pack(side="left", padx=5)

        buscar_btn = menuvista.Button(self.filtro_frame, text="Buscar", bg='#3498db', fg='white', command=self.aplicar_filtro)
        buscar_btn.pack(side="left", padx=5)

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
        self.productos = self.modelo.obtener_productos()  # Cambia a tu método real

        # Ordenar los productos por cantidad de mayor a menor
        self.productos = sorted(self.productos, key=lambda x: x["cantidad"], reverse=True)

        self.actualizar_tabla(self.productos)

    def actualizar_tabla(self, productos):
        # Limpiar tabla antes de actualizar
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        # Insertar productos en la tabla
        for producto in productos:
            self.treeview.insert("", "end", values=(producto["nombreP"], producto["cantidad"], producto["precio"], producto["categoria"]))

    def aplicar_filtro(self):
        termino = self.buscador_entry.get().lower()
        self.filtrados = [p for p in self.productos if termino in p["nombreP"].lower() or termino in p["categoria"].lower()]
        self.actualizar_tabla(self.filtrados)
