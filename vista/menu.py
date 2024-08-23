import tkinter as tk

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu principal")
        self.master.geometry("1200x800")
        self.master.configure(bg='#f2f2f2')
        self.crearinterface()

    def frame(self, parent, width, height, bg):
        frame = tk.Frame(parent, width=width, height=height, bg=bg)
        frame.pack_propagate(False)
        return frame

    def encabezado(self):
        encabezadoframe = self.frame(self.master, 900, 100, '#33daff')
        encabezadoframe.pack(side="top", fill="x")
        encabezadolabel = tk.Label(encabezadoframe, text="Nombre de la empresa", font=("Arial", 24), bg='#d9d9d9')
        encabezadolabel.pack(pady=20)
        return encabezadoframe

    def crearmenu(self, parent):
        Menuframe = self.frame(parent, 200, 500, '#e6e6e6')
        Menuframe.pack(side="left", fill="y")

        button1 = tk.Button(Menuframe, text="Apps", width=20, height=2, bg='#bfbfbf', fg='#333333')
        button1.place(x=25, y=300)
        
        button2 = tk.Button(Menuframe, text="Games", width=20, height=2, bg='#bfbfbf', fg='#333333')
        button2.place(x=25, y=350)
        
        button3 = tk.Button(Menuframe, text="Movies", width=20, height=2, bg='#bfbfbf', fg='#333333')
        button3.place(x=25, y=400)
        
        button4 = tk.Button(Menuframe, text="Books", width=20, height=2, bg='#bfbfbf', fg='#333333')
        button4.place(x=25, y=450)
        
        button5 = tk.Button(Menuframe, text="Newspapers", width=20, height=2, bg='#bfbfbf', fg='#333333')
        button5.place(x=25, y=500)

        return Menuframe

    def crearCategorias(self, parent):
        categories_frame = self.frame(parent, 700, 50, 'white')
        categories_frame.pack(side="top", fill="x")

        button1 = tk.Button(categories_frame, text="Categoría 1", width=14, height=2, bg='#a6a6a6', fg='#333333')
        button1.pack(side="left", padx=5, pady=5)
        
        button2 = tk.Button(categories_frame, text="Categoría 2", width=14, height=2, bg='#a6a6a6', fg='#333333')
        button2.pack(side="left", padx=5, pady=5)
        
        button3 = tk.Button(categories_frame, text="Categoría 3", width=14, height=2, bg='#a6a6a6', fg='#333333')
        button3.pack(side="left", padx=5, pady=5)
        
        button4 = tk.Button(categories_frame, text="Categoría 4", width=14, height=2, bg='#a6a6a6', fg='#333333')
        button4.pack(side="left", padx=5, pady=5)
        
        button5 = tk.Button(categories_frame, text="Categoría 5", width=14, height=2, bg='#a6a6a6', fg='#333333')
        button5.pack(side="left", padx=5, pady=5)

        return categories_frame

    def Titulocatalogo(self, parent):
        catalog_title_frame = self.frame(parent, 700, 50, '#d9d9d9')
        catalog_title_frame.pack(side="top", fill="x")
        catalog_title_label = tk.Label(catalog_title_frame, text="Título del Catálogo", font=("Arial", 18), bg='#d9d9d9')
        catalog_title_label.pack(pady=10)
        return catalog_title_frame

    def create_products_area(self, parent):
        products_frame = self.frame(parent, 700, 400, '#ffffff')
        products_frame.pack(side="top", fill="both", expand=True) 
        
        product_frame1 = tk.Frame(products_frame, width=200, height=120, bg="#e6e6e6")
        product_frame1.grid(row=0, column=0, padx=10 , pady=10)
        product_label1 = tk.Label(product_frame1,text="producto ", bg="#e6e6e6" )
        product_label1.pack(expand=True)

        product_frame2 = tk.Frame(products_frame, width=200, height=120, bg='#e6e6e6')
        product_frame2.grid(row=0, column=1, padx=10, pady=10)
        product_label2 = tk.Label(product_frame2, text="Producto ", bg='#e6e6e6')
        product_label2.pack(expand=True)

        product_frame3 = tk.Frame(products_frame, width=200, height=120, bg='#e6e6e6')
        product_frame3.grid(row=0, column=2, padx=10, pady=10)
        product_label3 = tk.Label(product_frame3, text="Producto", bg='#e6e6e6')
        product_label3.pack(expand=True)

        product_frame4 = tk.Frame(products_frame, width=200, height=120, bg='#e6e6e6')
        product_frame4.grid(row=1, column=0, padx=10, pady=10)
        product_label4 = tk.Label(product_frame4, text="Producto ", bg='#e6e6e6')
        product_label4.pack(expand=True)

        product_frame5 = tk.Frame(products_frame, width=200, height=120, bg='#e6e6e6')
        product_frame5.grid(row=1, column=1, padx=10, pady=10)
        product_label5 = tk.Label(product_frame5, text="Producto ", bg='#e6e6e6')
        product_label5.pack(expand=True)

        product_frame6 = tk.Frame(products_frame, width=200, height=120, bg='#e6e6e6')
        product_frame6.grid(row=1, column=2, padx=10, pady=10)
        product_label6 = tk.Label(product_frame6, text="Producto ", bg='#e6e6e6')
        product_label6.pack(expand=True)

        product_frame7 = tk.Frame(products_frame, width=200, height=120, bg='#e6e6e6')
        product_frame7.grid(row=2, column=0, padx=10, pady=10)
        product_label7 = tk.Label(product_frame7, text="Producto", bg='#e6e6e6')
        product_label7.pack(expand=True)

        product_frame8 = tk.Frame(products_frame, width=200, height=120, bg='#e6e6e6')
        product_frame8.grid(row=2, column=1, padx=10, pady=10)
        product_label8 = tk.Label(product_frame8, text="Producto", bg='#e6e6e6')
        product_label8.pack(expand=True)

        product_frame9 = tk.Frame(products_frame, width=200, height=120, bg='#e6e6e6')
        product_frame9.grid(row=2, column=2, padx=10, pady=10)
        product_label9 = tk.Label(product_frame9, text="Producto ", bg='#e6e6e6')
        product_label9.pack(expand=True)

        return products_frame


    def create_footer(self, parent):
        productsframe = self.frame(parent, 700, 50, '#ffffff')
        productsframe.pack(side="bottom", fill="both", expand=True)

        button1 = tk.Button(productsframe, text="Home", width=14, height=2, bg='#bfbfbf', fg='#333333')
        button1.place(x=20, y=10)

        button2 = tk.Button(productsframe, text="Apps", width=14, height=2, bg='#bfbfbf', fg='#333333')
        button2.place(x=150, y=10)

        button3 = tk.Button(productsframe, text="Games", width=14, height=2, bg='#bfbfbf', fg='#333333')
        button3.place(x=300, y=10)

        button4 = tk.Button(productsframe, text="Movies", width=14, height=2, bg='#bfbfbf', fg='#333333')
        button4.place(x=450, y=10)

        button5 = tk.Button(productsframe, text="Books", width=14, height=2, bg='#bfbfbf', fg='#333333')
        button5.place(x=600, y=10)

        return productsframe

    def crearinterface(self):
        self.encabezado()
        self.crearmenu(self.master)
        self.crearCategorias(self.master)
        self.Titulocatalogo(self.master)
        self.create_products_area(self.master)  # Ahora se coloca antes
        self.create_footer(self.master)  # Ahora se coloca después

if __name__ == "__main__":
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()
