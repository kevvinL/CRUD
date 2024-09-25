import tkinter as menuvista
from vista.vistaInformes import Menu
from vista.inventario import GestionProductos
from modelo.modelobk import modelo

class menuInterfaz:
    def __init__(self):
        self.master = menuvista.Tk()
        self.master.title("Menu principal")
        self.master.geometry("1200x800")
        self.master.configure(bg='#f5f5f5')
        self.producto_frame = None
        self.crearinterface()

    def crearinterface(self):
        self.encabezado()
        self.crearMenu(self.master)
        self.crearCategorias(self.master)
        self.Titulocatalogo(self.master)
        self.mostrarProductos() 

    def frame(self, parent, width, height, bg):
        frame = menuvista.Frame(parent, width=width, height=height, bg=bg)
        frame.pack_propagate(False)
        return frame

    def encabezado(self):
        encabezadoframe = self.frame(self.master, 1200, 100, '#2c3e50')
        encabezadoframe.pack(side="top", fill="x")
        encabezadolabel = menuvista.Label(encabezadoframe, text="Reposteria SugarCode ", font=("Helvetica", 24, "bold"), bg='#2c3e50', fg='white')
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
        menu_inventario = GestionProductos(nueva_ventana)
        nueva_ventana.mainloop()

    def crearCategorias(self, parent):
        CategoriaFrame = self.frame(parent, 950, 50, '#ecf0f1')
        CategoriaFrame.pack(side="top", fill="x")

        self.CrearCategoriaBoton(CategoriaFrame, "Pasteles y Tartas", 10, self.mostrarProductos)
        self.CrearCategoriaBoton(CategoriaFrame, "Galletas", 190, self.mostrarProductos2)
        self.CrearCategoriaBoton(CategoriaFrame, "Postres Frios", 370, self.mostrarProductos3)
        self.CrearCategoriaBoton(CategoriaFrame, "Cupcakes", 550, self.mostrarProductos4)
        self.CrearCategoriaBoton(CategoriaFrame, "Inventario", 730 , command=self.inventario)
        return CategoriaFrame

    def CrearCategoriaBoton(self, parent, text, x_position, command=None):
        button = menuvista.Button(parent, text=text, width=15, height=2, 
                                  bg='#3498db', fg='white', activebackground='#2980b9',
                                  bd=0, highlightthickness=0, command=command)
        button.place(x=x_position, y=5)

    def mostrarProductos(self):
        modelo_bd = modelo()
        productos = modelo_bd.obtener_productos()

        productos_formato = [(p['nombreP'], f"${p['precio']}", f"Descripción: {p['nombreP']}", 10 + (i % 3) * 320, 10 + (i // 3) * 170) 
                            for i, p in enumerate(productos)]
        
        self.actualizarProductos(productos_formato)


    def mostrarProductos2(self):
        modelo_bd = modelo()
        productos = modelo_bd.obtener_productos()

        productos_formato = [(p['nombreP'], f"${p['precio']}", f"Descripción: {p['nombreP']}", 10 + (i % 3) * 320, 10 + (i // 3) * 170) 
                            for i, p in enumerate(productos)]
        
        self.actualizarProductos(productos_formato)

    def mostrarProductos3(self):
        modelo_bd = modelo()
        productos = modelo_bd.obtener_productos()

        productos_formato = [(p['nombreP'], f"${p['precio']}", f"Descripción: {p['nombreP']}", 10 + (i % 3) * 320, 10 + (i // 3) * 170) 
                            for i, p in enumerate(productos)]
        
        self.actualizarProductos(productos_formato)

    def mostrarProductos4(self):
        modelo_bd = modelo()
        productos = modelo_bd.obtener_productos()

        productos_formato = [(p['nombreP'], f"${p['precio']}", f"Descripción: {p['nombreP']}", 10 + (i % 3) * 320, 10 + (i // 3) * 170) 
                            for i, p in enumerate(productos)]
        
        self.actualizarProductos(productos_formato)

    def actualizarProductos(self, productos):
        if self.producto_frame:
            self.producto_frame.destroy()
        self.producto_frame = self.frame(self.master, 950, 500, '#ecf0f1')
        self.producto_frame.pack(side="top", fill="both", expand=True)

        for nombre, precio, descripcion, x, y in productos:
            self.CrearProducto(self.producto_frame, nombre, precio, descripcion, x, y)

    def CrearProducto(self, parent, nombre, precio, descripcion, x_position, y_position):
        producto_frame = menuvista.Frame(parent, width=280, height=200, bg='white', relief='solid', bd=1)
        producto_frame.place(x=x_position, y=y_position)

        nombre_label = menuvista.Label(producto_frame, text=nombre, font=("Helvetica", 14, "bold"), bg='white', fg='#2c3e50')
        nombre_label.pack(anchor='n', pady=5)

        precio_label = menuvista.Label(producto_frame, text=precio, font=("Helvetica", 12, "bold"), bg='white', fg='#e74c3c')
        precio_label.pack(anchor='n')

        descripcion_label = menuvista.Label(producto_frame, text=descripcion, font=("Helvetica", 10), bg='white', fg='#7f8c8d', wraplength=260, justify='left')
        descripcion_label.pack(anchor='n', pady=5)

        agregar_btn = menuvista.Button(producto_frame, text="Agregar al carrito", bg='#3498db', fg='white', activebackground='#2980b9', relief='raised')
        agregar_btn.pack(anchor='s', pady=10)

        producto_frame.config(relief="groove", bd=2)



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
