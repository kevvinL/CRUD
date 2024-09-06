import tkinter as menuvista

class menuInterfaz:
    def __init__(self):
        self.master = menuvista.Tk()
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
        CatalogoTituloLabel = menuvista.Label(CatalogoTituloFrame, text="Catálogo de Productos", font=("Helvetica", 18, "bold"), bg='#ecf0f1')
        CatalogoTituloLabel.pack(pady=10)

        ContenedorFrame = menuvista.Frame(CatalogoTituloFrame, bg='#ecf0f1')
        ContenedorFrame.pack(side="right", padx=20)
        ContenedorEntry = menuvista.Entry(ContenedorFrame, width=30)
        ContenedorEntry.pack(side="left")
        BotonB = menuvista.Button(ContenedorFrame, text="Buscar", bg='#3498db', fg='white')
        BotonB.pack(side="left", padx=5)

        return CatalogoTituloFrame

    def Productos(self, parent):
        ProductoFrame = self.frame(parent, 950, 500, '#ecf0f1')
        ProductoFrame.pack(side="top", fill="both", expand=True)

        self.CrearProducto(ProductoFrame, "Producto 1", 10, 10)
        self.CrearProducto(ProductoFrame, "Producto 2", 320, 10)
        self.CrearProducto(ProductoFrame, "Producto 3", 630, 10)
        self.CrearProducto(ProductoFrame, "Producto 4", 10, 180)
        self.CrearProducto(ProductoFrame, "Producto 5", 320, 180)
        self.CrearProducto(ProductoFrame, "Producto 6", 630, 180)
        self.CrearProducto(ProductoFrame, "Producto 7", 10, 350)
        self.CrearProducto(ProductoFrame, "Producto 8", 320, 350)
        self.CrearProducto(ProductoFrame, "Producto 9", 630, 350)

        return ProductoFrame

    def CrearProducto(self, parent, product_name, x_position, y_position):
        productframe = menuvista.Frame(parent, width=280, height=150, bg='white', bd=1, relief=menuvista.RAISED)
        productframe.place(x=x_position, y=y_position)
        
        ProductoImagen = menuvista.Frame(productframe, width=100, height=100, bg='#bdc3c7')
        ProductoImagen.pack(side="left", padx=10, pady=10)
        
        Info = menuvista.Frame(productframe, bg='white')
        Info.pack(side="left", fill="both", expand=True)
        
        menuvista.Label(Info, text=product_name, font=("Helvetica", 12, "bold"), bg='white').pack(anchor="w")
        menuvista.Label(Info, text="Descripción breve", bg='white').pack(anchor="w")
        menuvista.Label(Info, text="$XX.XX", font=("Helvetica", 10, "bold"), bg='white').pack(anchor="w")

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
    
    def iniciar(self):
        self.master.mainloop()


