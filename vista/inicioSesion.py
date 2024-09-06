import tkinter as vistaInicioSesion
from tkinter import messagebox

class inicioSesionVista:
    def __init__(self, controlador):
        self.controlador = controlador
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
        labelTitulo.place(x=110, y=35, width= 180, height=30)
        labelTitulo.config(bg= self.colorLabel )
        
        labelUser = vistaInicioSesion.Label(datoContenedor, text= "User:", font=("Arial", 12))
        labelUser.place(x=80, y=90, width= 50, height= 20)
        labelUser.config(bg= self.colorLabel )
        
        self.entryUser = vistaInicioSesion.StringVar()
        user = vistaInicioSesion.Entry(datoContenedor, textvariable=self.entryUser)
        user.place(x=82, y=110, width=240, height=20)
        user.config(bg="#e3e4e9")
        
        labelContraseña =vistaInicioSesion.Label(datoContenedor, text= "Password:", font=("Arial", 12))
        labelContraseña.place(x=85, y=150, width= 75, height=20)
        labelContraseña.config(bg= self.colorLabel )
        
        self.entryContraseña = vistaInicioSesion.StringVar()
        contraseña = vistaInicioSesion.Entry(datoContenedor, textvariable=self.entryContraseña, font=("Arial", 11), show="*")
        contraseña.place(x=81, y=170, width=240, height=20)
        contraseña.config(bg="#e3e4e9")
        
        botonInicio = vistaInicioSesion.Button(text= "Iniciar Sesión", font=("Arial", 11), command=self.enviarDatos)
        botonInicio.place(x=200, y=290, width=95, height= 30)
<<<<<<< HEAD
    
    def enviarDatos(self):
        
        
        datos = {
            'usuario': self.entryUser.get(),
            'contraseña': self.entryContraseña.get()
        }
        
        if datos['usuario'] != None and datos['contraseña'] != None:
            verificacion = self.controlador.inicioUsuario(datos)
            if verificacion == False:
                messagebox.showinfo("Error", "Datos incorrectos")

#boton desplegable
"""class inicioSesion:
    def __init__ (self):
        self.user = None
        self.contraseña = None
=======
>>>>>>> anshi
    
    def enviarDatos(self):
        
        
        datos = {
            'usuario': self.entryUser.get(),
            'contraseña': self.entryContraseña.get()
        }
        
        if datos['usuario'] != None and datos['contraseña'] != None:
            verificacion = self.controlador.inicioUsuario(datos)
            if verificacion == False:
                messagebox.showinfo("Error", "Datos incorrectos")

<<<<<<< HEAD
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
=======
>>>>>>> anshi
