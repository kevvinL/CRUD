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
        contraseña = vistaInicioSesion.Entry(datoContenedor, textvariable=self.entryContraseña)
        contraseña.place(x=81, y=170, width=240, height=20)
        contraseña.config(bg="#e3e4e9")
        
        botonInicio = vistaInicioSesion.Button(text= "Iniciar Sesión", font=("Arial", 11))
        botonInicio.place(x=200, y=290, width=95, height= 30)


formulario =inicioSesion()
auxFormulario = formulario.crearFormulario()
contenedor = formulario.contenedorModelo(auxFormulario)
formulario.vistaInicio(contenedor)
auxFormulario.mainloop()