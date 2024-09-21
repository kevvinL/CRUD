import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vista.inicioSesion import inicioSesionVista
from modelo.modelobk import modelo 
from vista.menu import menuInterfaz 

class controladorInicio:
    def __init__(self):
        self.modelo = modelo()
        self.inicioSesion = None
        self.menu = None
    
    def inicioUsuario(self, datos):
        if not datos['usuario'] or not datos['contraseña']:
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
        self.inicioSesion = inicioSesionVista(controlador=self)
        auxFormulario = self.inicioSesion.crearFormulario()
        contenedor = self.inicioSesion.contenedorModelo(auxFormulario)
        self.inicioSesion.vistaInicio(contenedor)
        auxFormulario.mainloop()
    
    def iniciarMenu(self):
        self.menu = menuInterfaz(controlador=self)
        self.menu.iniciar()
    
    def informe(self):
        if self.menu:
            self.menu.mostrarInforme()
    
    def mostrarProductosPorCategoria(self, categoria):
        if self.menu:
            self.menu.mostrarProductos(categoria)


controlador = controladorInicio()
controlador.iniciarVista()