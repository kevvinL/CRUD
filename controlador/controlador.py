import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vista.inicioSesion import inicioSesionVista
from modelo.modelobk import modelo 
from vista.menu import menuInterfaz 
from vista.vistaInformes import Menu
import tkinter as menuvista

class controladorInicio:
    def __init__(self):
        self.modelo = modelo()
    
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
        nueva_ventana = menuvista.Tk()  # Crear la nueva ventana
        menu_informe = Menu(nueva_ventana)
        
        # Añadir contenido a la nueva ventana (si es necesario)
        
        # Mantener la ventana abierta
        nueva_ventana.mainloop()

controlador = controladorInicio()
controlador.iniciarVista()