import tkinter as menuvista
from tkinter import ttk

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu principal")
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
        encabezadolabel = menuvista.Label(encabezadoframe, text="Nombre de la empresa", font=("Helvetica", 24, "bold"), bg='#2c3e50', fg='white')
        encabezadolabel.pack(pady=20)
        return encabezadoframe

    def crearMenu(self, parent):
        Menuframe = self.frame(parent, 250, 600, '#34495e')
        Menuframe.pack(side="left", fill="y")

        self.CrearBotonMenu(Menuframe, "Apps", 10)
        self.CrearBotonMenu(Menuframe, "Games", 60)
        self.CrearBotonMenu(Menuframe, "Movies", 110)
        self.CrearBotonMenu(Menuframe, "Books", 160)
        self.CrearBotonMenu(Menuframe, "Newspapers", 210)

        return Menuframe

    def CrearBotonMenu(self, parent, text, y_position):
        button = menuvista.Button(parent, text=text, width=25, height=2, bg='#34495e', fg='white', 
                           activebackground='#2c3e50', activeforeground='white',
                           bd=0, highlightthickness=0)
        button.place(x=10, y=y_position)

    def crearCategorias(self, parent):
        CategoriaFrame = self.frame(parent, 950, 50, '#ecf0f1')
        CategoriaFrame.pack(side="top", fill="x")

        self.CrearCategoriaBoton(CategoriaFrame, "Categoría 1", 10)
        self.CrearCategoriaBoton(CategoriaFrame, "Categoría 2", 190)
        self.CrearCategoriaBoton(CategoriaFrame, "Categoría 3", 370)
        self.CrearCategoriaBoton(CategoriaFrame, "Categoría 4", 550)
        self.CrearCategoriaBoton(CategoriaFrame, "Categoría 5", 730)

        return CategoriaFrame

    def CrearCategoriaBoton(self, parent, text, x_position):
        button = menuvista.Button(parent, text=text, width=15, height=2, 
                           bg='#3498db', fg='white', activebackground='#2980b9',
                           bd=0, highlightthickness=0)
        button.place(x=x_position, y=5)

    def Titulocatalogo(self, parent):
        CatalogoTituloFrame = self.frame(parent, 950, 50, '#ecf0f1')
        CatalogoTituloFrame.pack(side="top", fill="x")
        CatalogoTituloLabel = menuvista.Label(CatalogoTituloFrame, text="Informe de Productos", font=("Helvetica", 18, "bold"), bg='#ecf0f1')
        CatalogoTituloLabel.pack(pady=10)

        return CatalogoTituloFrame

    def Productos(self, parent):
        ProductoFrame = self.frame(parent, 950, 400, '#ecf0f1')
        ProductoFrame.pack(side="top", fill="both", expand=True)

        self.CrearTabla(ProductoFrame, "Más Vendidos", 10, 10)
        self.CrearTabla(ProductoFrame, "Menos Vendidos", 10, 280)

        return ProductoFrame

    def CrearTabla(self, parent, titulo, x_position, y_position):
        # Creamos el frame para la tabla más grande (800x300)
        tableframe = menuvista.Frame(parent, width=1000, height=300, bg='white', bd=1, relief=menuvista.RAISED)
        tableframe.place(x=x_position, y=y_position)

        menuvista.Label(tableframe, text=titulo, font=("Helvetica", 12, "bold"), bg='white').pack(anchor="w")
        
        # Creamos un Treeview (tabla) con columnas más amplias
        columnas = ("Producto", "Cantidad", "Precio", "Fecha")
        treeview = ttk.Treeview(tableframe, columns=columnas, show="headings", height=10)  # La tabla tendrá 10 filas visibles

        # Definimos los encabezados y ajustamos el ancho de las columnas
        treeview.heading("Producto", text="Producto")
        treeview.heading("Cantidad", text="Cantidad")
        treeview.heading("Precio", text="Precio")
        treeview.heading("Fecha", text="Fecha")

        # Ajustamos el tamaño de las columnas
        treeview.column("Producto", anchor='center', width=200)
        treeview.column("Cantidad", anchor='center', width=100)
        treeview.column("Precio", anchor='center', width=100)
        treeview.column("Fecha", anchor='center', width=150)

        # Empaquetamos la tabla para que sea visible
        treeview.pack(fill="both", expand=True)

        return treeview

    def CrearBotonesIzquierda(self, parent):
        IzquierdaFrame = self.frame(parent, 1200, 50, '#2c3e50')
        IzquierdaFrame.pack(side="bottom", fill="x")

        self.CrearIzquierdaBoton(IzquierdaFrame, "Home", 20)
        self.CrearIzquierdaBoton(IzquierdaFrame, "Apps", 260)
        self.CrearIzquierdaBoton(IzquierdaFrame, "Games", 500)
        self.CrearIzquierdaBoton(IzquierdaFrame, "Movies", 740)
        self.CrearIzquierdaBoton(IzquierdaFrame, "Books", 980)

        return IzquierdaFrame

    def CrearIzquierdaBoton(self, parent, text, x_position):
        button = menuvista.Button(parent, text=text, bg='#2c3e50', fg='white', 
                           activebackground='#34495e', activeforeground='white',
                           bd=0, highlightthickness=0)
        button.place(x=x_position, y=10)

    def crearinterface(self):
        self.encabezado()
        self.crearMenu(self.master)
        self.crearCategorias(self.master)
        self.Titulocatalogo(self.master)
        self.Productos(self.master)
        self.CrearBotonesIzquierda(self.master)

if __name__ == "__main__":
    iniciar = menuvista.Tk()
    menu = Menu(iniciar)
    iniciar.mainloop()