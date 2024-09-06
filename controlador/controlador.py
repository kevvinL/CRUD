import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from vista.inicioSesion import inicioSesionVista
from model.modelobk import modelo
from vista.menu import MenuInterfaz


class controladorinicio:
    def __init__(self):
        self.modelo = modelo()
    
    def inicioUsuario(self, datos):
        if not datos["usuario"] or not datos["contraseña"]:
            return False
        else:
            usuarioEnviar = self.modelo.inicioSesion(datos)
            print(f"Usuario: {datos['usuario']}, Contraseña: {datos['contraseña']}")
            if usuarioEnviar == "verificado":
                self.inicioSesion.sesion.destroy()
                self.iniciarMenu()
            else:
                return False
    
    def iniciarVista(self):
        self.inicioSesion = inicioSesionVista()
        self.vista = self.inicioSesion.crearFormulario()
        self.contenedorModelo(self.vista)
        self.vista.mainloop()
    
    def iniciarMenu(self):
        self.menu = MenuInterfaz()
        self.menu.iniciar()

controlador = controladorinicio()
controlador.iniciarVista()