import tkinter as vistaInicioSesion
from tkinter import messagebox

class inicioSesion:
    def init (self):
        self.user = None
        self.contraseña = None
    
    def crearFormulario(self):
        self.sesion = vistaInicioSesion.Tk()
        self.sesion.title("Inicio Sesión")
        self.sesion.geometry("500x400")
        self.sesion.config(bg="white")
        return self.sesion
    
    def contenedorModelo (self,datoContenedor):
        contenedor = vistaInicioSesion.Frame(datoContenedor)
        contenedor.config(bg="#396cc0", width=400, height=280)
        contenedor.pack(padx=50, pady=60, side=vistaInicioSesion.LEFT)
        return contenedor

    def vistaInicio(self, datoContenedor):
        self.colorLabel = "#396cc0"
        labelTitulo = vistaInicioSesion.Label(datoContenedor, text="Inicio Sesión",font=("Arial", 18))
        labelTitulo.place(x=110, y= 25, width= 180, height=30)
        labelTitulo.config(bg= self.colorLabel )
        
        labelUser = vistaInicioSesion.Label(datoContenedor, text= "User:", font=("Arial", 12))
        labelUser.place(x=80, y=75, width= 50, height= 20)
        labelUser.config(bg= self.colorLabel )
        
        self.entryUser = vistaInicioSesion.StringVar()
        user = vistaInicioSesion.Entry(datoContenedor, textvariable=self.entryUser)
        user.place(x=82, y=95, width=240, height=20)
        user.config(bg="#e3e4e9")
        
        labelContraseña =vistaInicioSesion.Label(datoContenedor, text= "Password:", font=("Arial", 12))
        labelContraseña.place(x=85, y=130, width= 75, height=20)
        labelContraseña.config(bg= self.colorLabel )
        
        self.entryContraseña = vistaInicioSesion.StringVar()
        contraseña = vistaInicioSesion.Entry(datoContenedor, textvariable=self.entryContraseña)
        contraseña.place(x=81, y=150, width=240, height=20)
        contraseña.config(bg="#e3e4e9")
        
        labelRol = vistaInicioSesion.Label(datoContenedor, text="Usuario Rol:",font=("Arial", 12))
        labelRol.place(x=85, y=178, width=90, height=30)
        labelRol.config(bg= self.colorLabel )
        
        self.opcionSeleccionada = vistaInicioSesion.StringVar(value="Administrador")
        radio1 = vistaInicioSesion.Radiobutton(datoContenedor, text="Administrador", variable=self.opcionSeleccionada, value="Administrador")
        radio2 = vistaInicioSesion.Radiobutton(datoContenedor, text="Vendedor", variable=self.opcionSeleccionada, value="Vendedor")
        radio1.config(bg=self.colorLabel)
        radio2.config(bg=self.colorLabel)
        radio1.place(x=80, y=200)
        radio2.place(x=190, y=200)
        
        botonInicio = vistaInicioSesion.Button(text= "Iniciar Sesión", font=("Arial", 11))
        botonInicio.place(x=200, y=305, width=95, height= 30)


#boton desplegable
"""class inicioSesion:
    def __init__ (self):
        self.user = None
        self.contraseña = None
    
    def crearFormulario(self):
        self.sesion = vistaInicioSesion.Tk()
        self.sesion.title("Inicio Sesión")
        self.sesion.geometry("500x400")
        self.sesion.config(bg="white")
        return self.sesion
    
    def contenedorModelo (self,datoContenedor):
        contenedor = vistaInicioSesion.Frame(datoContenedor)
        contenedor.config(bg="#396cc0", width=400, height=300)
        contenedor.pack(padx=40, pady=40, side=vistaInicioSesion.LEFT)
        return contenedor

    def vistaInicio(self, datoContenedor):
        self.colorLabel = "#396cc0"
        labelTitulo = vistaInicioSesion.Label(datoContenedor, text="Inicio Sesión",font=("Arial", 18))
        labelTitulo.place(x=110, y= 25, width= 180, height=30)
        labelTitulo.config(bg= self.colorLabel )
        
        
        self.opcionSeleccionada = vistaInicioSesion.StringVar(value="Rol Usuario")
        botonRol = vistaInicioSesion.Menubutton(datoContenedor, textvariable=self.opcionSeleccionada, relief=vistaInicioSesion.RAISED, direction="below")
        botonRol.place(x=80, y=85, width=100, height=20)

        rolOpciones = vistaInicioSesion.Menu(botonRol, tearoff=0)
        botonRol.config(menu=rolOpciones)

        rolOpciones.add_command(label="Administrador", command=lambda: self.cambiarOpcion("Administrador"))
        rolOpciones.add_command(label="Vendedor", command=lambda: self.cambiarOpcion("Vendedor"))
        
        labelUser = vistaInicioSesion.Label(datoContenedor, text= "User:", font=("Arial", 12))
        labelUser.place(x=80, y=125, width= 50, height= 20)
        labelUser.config(bg= self.colorLabel )
        
        self.entryUser = vistaInicioSesion.StringVar()
        user = vistaInicioSesion.Entry(datoContenedor, textvariable=self.user)
        user.place(x=82, y=145, width=240, height=20)
        user.config(bg="#e3e4e9")
        
        labelContraseña =vistaInicioSesion.Label(datoContenedor, text= "Password", font=("Arial", 12))
        labelContraseña.place(x=80, y=190, width= 80, height=20)
        labelContraseña.config(bg= self.colorLabel )
        
        self.entryContraseña = vistaInicioSesion.StringVar()
        contraseña = vistaInicioSesion.Entry(datoContenedor, textvariable=self.contraseña)
        contraseña.place(x=80, y=210, width=240, height=20)
        contraseña.config(bg="#e3e4e9")
        
        botonInicio = vistaInicioSesion.Button(text= "Iniciar Sesión", font=("Arial", 11))
        botonInicio.place(x=200, y=310, width=95, height= 30)
        
    def cambiarOpcion(self, opcion):
        self.opcionSeleccionada.set(opcion)"""

formulario =inicioSesion()
auxFormulario = formulario.crearFormulario()
contenedor = formulario.contenedorModelo(auxFormulario)
formulario.vistaInicio(contenedor)
auxFormulario.mainloop()