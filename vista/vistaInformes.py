import tkinter as menuvista

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
        ProductoFrame = self.frame(parent, 950, 500, '#ecf0f1')
        ProductoFrame.pack(side="top", fill="both", expand=True)

        self.CrearTabla(ProductoFrame, "Más Vendidos", 10, 10)
        self.CrearTabla(ProductoFrame, "Menos Vendidos", 320, 10)

        return ProductoFrame

    def CrearTabla(self, parent, titulo, x_position, y_position):
        tableframe = menuvista.Frame(parent, width=280, height=150, bg='white', bd=1, relief=menuvista.RAISED)
        tableframe.place(x=x_position, y=y_position)
        
        menuvista.Label(tableframe, text=titulo, font=("Helvetica", 12, "bold"), bg='white').pack(anchor="w")
        # Puedes añadir una tabla aquí si es necesario usando grid o alguna librería externa

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


"""import tkinter as tk
from tkinter import ttk



class EmpresaInterfaz:
    def __init__(self):
        self.root = None

    def crearVentana(self):
        self.root = tk.Tk()
        self.root.title("Nombre de la empresa")
        self.root.geometry("800x600")
        return self.root

    def crearCabecera(self, contenedor):
        #Cabecera
        cabecera = tk.Frame(contenedor, bg="lightgray", height=100)
        cabecera.pack(side="top", fill="x")

        #Nombre de la empresa
        nombreE = tk.Label(cabecera, text="Nombre de la empresa", font=("Arial", 24), bg="lightgray")
        nombreE.pack(side="left", padx=20, pady=20)

        navFrame = tk.Frame(cabecera)
        navFrame.pack(side="bottom", fill="x")

        botonH=tk.Button(navFrame, text="Home")
        botonH.pack(side="left", padx=5, pady=5)

        botonP=tk.Button(navFrame, text="Products")
        botonP.pack(side="left", padx=5, pady=5)

        botonA=tk.Button(navFrame, text="About")
        botonA.pack(side="left", padx=5, pady=5)

        botonC=tk.Button(navFrame, text="Contact")
        botonC.pack(side="left", padx=5, pady=5)

        return cabecera

    def crearCuerpo(self, contenedor):
        menuFrame = tk.Frame(contenedor)
        menuFrame.pack(fill="both", expand=True)

        #Categorías
        topFrame = tk.Frame(menuFrame)
        topFrame.pack(fill="x")

        cat1 = tk.Button(topFrame, text="Categoría 1")
        cat1.pack(side="left", padx=5, pady=5)

        cat2 = tk.Button(topFrame, text="Categoría 2")
        cat2.pack(side="left", padx=5, pady=5)

        cat3 = tk.Button(topFrame, text="Categoría 3")
        cat3.pack(side="left", padx=5, pady=5)

        cat4 = tk.Button(topFrame, text="Categoría 4")
        cat4.pack(side="left", padx=5, pady=5)

        cat5 = tk.Button(topFrame, text="Categoría 5")
        cat5.pack(side="left", padx=5, pady=5)

        #Informes
        reportesFrame = tk.LabelFrame(menuFrame, text="Informe de Productos", padx=10, pady=10)
        reportesFrame.pack(fill="both", expand=True)

        #Mas Vendidos
        mayorFrame = tk.LabelFrame(reportesFrame, text="Mas Vendidos")
        mayorFrame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        mayorVenta = ttk.Treeview(mayorFrame, columns=("nombre", "cantidad"), show="headings")
        mayorVenta.heading("nombre", text="Nombre Producto")
        mayorVenta.heading("cantidad", text="Cantidad")
        mayorVenta.pack(fill="both", expand=True)

        #Menos Vendidos
        menorFrame = tk.LabelFrame(reportesFrame, text="Menos Vendidos")
        menorFrame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        menorVenta = ttk.Treeview(menorFrame, columns=("nombre", "cantidad"), show="headings")
        menorVenta.heading("nombre", text="Nombre Producto")
        menorVenta.heading("cantidad", text="Cantidad")
        menorVenta.pack(fill="both", expand=True)

        #Botón generar informes
        gInforme = tk.Button(reportesFrame, text="Generar Informe")
        gInforme.pack(pady=10)

        return menuFrame

    def crearBarraL(self, contenedor):
        #Barra lateral
        BarraFrame = tk.Frame(contenedor, bg="gray", width=150)
        BarraFrame.pack(side="left", fill="y")

        bApps=tk.Button(BarraFrame, text="Apps")
        bApps.pack(fill="x", padx=5, pady=5)

        bGames=tk.Button(BarraFrame, text="Games")
        bGames.pack(fill="x", padx=5, pady=5)

        bMovies=tk.Button(BarraFrame, text="Movies")
        bMovies.pack(fill="x", padx=5, pady=5)

        bBooks=tk.Button(BarraFrame, text="Books")
        bBooks.pack(fill="x", padx=5, pady=5)

        bNewspapers=tk.Button(BarraFrame, text="Newspapers")
        bNewspapers.pack(fill="x", padx=5, pady=5)

        return BarraFrame

    def crearPiePagina(self, contenedor):
        #Pie de la pagina
        piePagFrame = tk.Frame(contenedor, bg="lightgray", height=50)
        piePagFrame.pack(side="bottom", fill="x")

        bHome=tk.Button(piePagFrame, text="Home")
        bHome.pack(fill="x", padx=5, pady=5)

        bApps=tk.Button(piePagFrame, text="Apps")
        bApps.pack(fill="x", padx=5, pady=5)

        bGames=tk.Button(piePagFrame, text="Games")
        bGames.pack(fill="x", padx=5, pady=5)

        bMovies=tk.Button(piePagFrame, text="Movies")
        bMovies.pack(fill="x", padx=5, pady=5)

        bBooks=tk.Button(piePagFrame, text="Books")
        bBooks.pack(fill="x", padx=5, pady=5)

        return piePagFrame

#Iniciar ventana
app = EmpresaInterfaz()
ventana = app.crearVentana()
app.crearCabecera(ventana)
app.crearBarraL(ventana)
app.crearCuerpo(ventana)
app.crearPiePagina(ventana)

ventana.mainloop()
# Ejecutar la aplicación
ventana.mainloop()"""