import tkinter as tk
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
        # Cabecera
        cabecera = tk.Frame(contenedor, bg="lightgray", height=100)
        cabecera.pack(side="top", fill="x")

        # Nombre de la empresa
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
        # Barra lateral
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
        bHome.pack(fill="left", padx=5, pady=5)

        bApps=tk.Button(piePagFrame, text="Apps")
        bApps.pack(fill="left", padx=5, pady=5)

        bGames=tk.Button(piePagFrame, text="Games")
        bGames.pack(fill="left", padx=5, pady=5)

        bMovies=tk.Button(piePagFrame, text="Movies")
        bMovies.pack(fill="left", padx=5, pady=5)

        bBooks=tk.Button(piePagFrame, text="Books")
        bBooks.pack(fill="left", padx=5, pady=5)

        return piePagFrame


# Crear la aplicación
app = EmpresaInterfaz()
ventana = app.crearVentana()
app.crearCabecera(ventana)
app.crearBarraL(ventana)
app.crearCuerpo(ventana)
app.crearPiePagina(ventana)

# Ejecutar la aplicación
ventana.mainloop()