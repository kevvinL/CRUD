import tkinter as menuvista
from vista.vistaInventario import Inventario
from vista.vistaInformes import Menu

class menuInterfaz:
    def __init__(self):
        self.master = menuvista.Tk()
        self.master.title("Menu principal")
        self.master.geometry("1200x800")
        self.master.configure(bg='#f5f5f5')
        self.producto_frame = None  # Para almacenar el frame actual de productos
        self.crearinterface()

    def crearinterface(self):
        self.encabezado()
        self.crearMenu(self.master)
        self.crearCategorias(self.master)
        self.Titulocatalogo(self.master)
        self.mostrarProductosCategoria1()  # Muestra los productos de la primera categoría por defecto

    def frame(self, parent, width, height, bg):
        frame = menuvista.Frame(parent, width=width, height=height, bg=bg)
        frame.pack_propagate(False)
        return frame

    def encabezado(self):
        encabezadoframe = self.frame(self.master, 1200, 100, '#2c3e50')
        encabezadoframe.pack(side="top", fill="x")
        encabezadolabel = menuvista.Label(encabezadoframe, text="Nombre de la empresa ", font=("Helvetica", 24, "bold"), bg='#2c3e50', fg='white')
        encabezadolabel.pack(pady=20)
        return encabezadoframe

    def cerrarSesion(self):
        self.master.destroy()
        self.abrirInicioSesion()

    def abrirInicioSesion(self):
        from vista.inicioSesion import inicioSesionVista
        login = inicioSesionVista(None)  
        sesion = login.crearFormulario()
        contenedor = login.contenedorModelo(sesion)
        login.vistaInicio(contenedor)
        sesion.mainloop()

    def informe(self):
        nueva_ventana = menuvista.Tk()
        menu_informe = Menu(nueva_ventana)
        nueva_ventana.mainloop()

    def crearMenu(self, parent):
        Menuframe = self.frame(parent, 250, 600, '#34495e')
        Menuframe.pack(side="left", fill="y")

        self.CrearBotonMenu(Menuframe, "Apps", 10)
        self.CrearBotonMenu(Menuframe, "Games", 60)
        self.CrearBotonMenu(Menuframe, "Movies", 110)
        self.CrearBotonMenu(Menuframe, "Books", 160)
        self.CrearBotonMenu(Menuframe, "Newspapers", 210)
        self.CrearBotonMenu(Menuframe, "Cerrar sesion", 600, command=self.cerrarSesion)
        self.CrearBotonMenu(Menuframe, "Informe", 500 , command=self.informe)
        return Menuframe

    def CrearBotonMenu(self, parent, text, y_position, command=None):
        button = menuvista.Button(parent, text=text, width=25, height=2, bg='#34495e', fg='white', 
                        activebackground='#2c3e50', activeforeground='white',
                        bd=0, highlightthickness=0 , command=command)
        button.place(x=10, y=y_position)

    def inventario(self):
        nueva_ventana = menuvista.Tk()
        menu_informe = Inventario(nueva_ventana)
        nueva_ventana.mainloop()

    def crearCategorias(self, parent):
        CategoriaFrame = self.frame(parent, 950, 50, '#ecf0f1')
        CategoriaFrame.pack(side="top", fill="x")

        self.CrearCategoriaBoton(CategoriaFrame, "Categoría 1", 10, self.mostrarProductosCategoria1)
        self.CrearCategoriaBoton(CategoriaFrame, "Categoría 2", 190, self.mostrarProductosCategoria2)
        self.CrearCategoriaBoton(CategoriaFrame, "Categoría 3", 370, self.mostrarProductosCategoria3)
        self.CrearCategoriaBoton(CategoriaFrame, "Categoría 4", 550, self.mostrarProductosCategoria4)
        self.CrearCategoriaBoton(CategoriaFrame, "Inventario", 730 , command=self.inventario)
        return CategoriaFrame

    def CrearCategoriaBoton(self, parent, text, x_position, command=None):
        button = menuvista.Button(parent, text=text, width=15, height=2, 
                                  bg='#3498db', fg='white', activebackground='#2980b9',
                                  bd=0, highlightthickness=0, command=command)
        button.place(x=x_position, y=5)

    # Métodos para mostrar productos según la categoría seleccionada
    def mostrarProductosCategoria1(self):
        self.actualizarProductos([("Pastel de chocolate", "$5000", "Pastel de bizcocho de chocolate con ganache de chocolate", 10, 10), 
                                  ("Producto 2", "$12", "Descripción del producto 2", 320, 10), 
                                  ("Producto 3", "$15", "Descripción del producto 3", 630, 10)])

    def mostrarProductosCategoria2(self):
        self.actualizarProductos([("Producto 4", "$20", "Descripción del producto 4", 10, 10), 
                                  ("Producto 5", "$25", "Descripción del producto 5", 320, 10)])

    def mostrarProductosCategoria3(self):
        self.actualizarProductos([("Producto 6", "$30", "Descripción del producto 6", 10, 10)])

    def mostrarProductosCategoria4(self):
        self.actualizarProductos([("Producto 7", "$35", "Descripción del producto 7", 10, 10), 
                                  ("Producto 8", "$40", "Descripción del producto 8", 320, 10)])

    # Método para actualizar el frame de productos
    def actualizarProductos(self, productos):
        if self.producto_frame:
            self.producto_frame.destroy()  # Elimina el frame anterior de productos
        self.producto_frame = self.frame(self.master, 950, 500, '#ecf0f1')
        self.producto_frame.pack(side="top", fill="both", expand=True)

        for nombre, precio, descripcion, x, y in productos:
            self.CrearProducto(self.producto_frame, nombre, precio, descripcion, x, y)

    def CrearProducto(self, parent, nombre, precio, descripcion, x_position, y_position):
        producto_frame = menuvista.Frame(parent, width=270, height=160, bg='white', relief='raised', bd=2)
        producto_frame.place(x=x_position, y=y_position)

        nombre_label = menuvista.Label(producto_frame, text=nombre, font=("Helvetica", 12, "bold"), bg='white')
        nombre_label.pack(anchor='n', pady=5)

        precio_label = menuvista.Label(producto_frame, text=precio, font=("Helvetica", 10), bg='white')
        precio_label.pack(anchor='n')

        descripcion_label = menuvista.Label(producto_frame, text=descripcion, font=("Helvetica", 9), bg='white', wraplength=250)
        descripcion_label.pack(anchor='n')

        agregar_btn = menuvista.Button(producto_frame, text="Agregar", bg='#3498db', fg='white')
        agregar_btn.pack(anchor='s', pady=5)

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

    def iniciar(self):
        self.master.mainloop()




"""from vista.vistaInformes import Menu
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
        encabezadolabel = menuvista.Label(encabezadoframe, text="Nombre de la empresa ", font=("Helvetica", 24, "bold"), bg='#2c3e50', fg='white')
        encabezadolabel.pack(pady=20)
        
        return encabezadoframe

    def cerrarSesion(self):
        self.master.destroy()
        self.abrirInicioSesion()

    def abrirInicioSesion(self):
        from vista.inicioSesion import inicioSesionVista
        login = inicioSesionVista(None)  
        sesion = login.crearFormulario()
        contenedor = login.contenedorModelo(sesion)
        login.vistaInicio(contenedor)
        sesion.mainloop()

    def informe(self):
        nueva_ventana = menuvista.Tk()
        menu_informe = Menu(nueva_ventana)
        
        nueva_ventana.mainloop()

    def crearMenu(self, parent):
        Menuframe = self.frame(parent, 250, 600, '#34495e')
        Menuframe.pack(side="left", fill="y")

        self.CrearBotonMenu(Menuframe, "Apps", 10)
        self.CrearBotonMenu(Menuframe, "Games", 60)
        self.CrearBotonMenu(Menuframe, "Movies", 110)
        self.CrearBotonMenu(Menuframe, "Books", 160)
        self.CrearBotonMenu(Menuframe, "Newspapers", 210)
        self.CrearBotonMenu(Menuframe, "Cerrar sesion", 600, command=self.cerrarSesion)
        self.CrearBotonMenu(Menuframe, "Informe", 500 , command=self.informe)
        
        return Menuframe

    def CrearBotonMenu(self, parent, text, y_position, command=None):
        button = menuvista.Button(parent, text=text, width=25, height=2, bg='#34495e', fg='white', 
                        activebackground='#2c3e50', activeforeground='white',
                        bd=0, highlightthickness=0 , command=command)
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

    def mostrarProductosCategoria1(self):
        self.actualizarProductos([("Producto 1", 10, 10), ("Producto 2", 320, 10), 
                                  ("Producto 3", 630, 10), ("Producto 4", 10, 180), 
                                  ("Producto 5", 320, 180), ("Producto 6", 630, 180),
                                  ("Producto 7", 10, 350), ("Producto 8", 320, 350),
                                  ("Producto 9", 630, 350)])

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
        self.master.mainloop()"""

