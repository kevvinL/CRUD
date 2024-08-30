import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vista.inicioSesion import inicioSesionVista

class controladorInicio:
    def __init__(self):
        pass
    
    
    def inicioUsuario(self, datos):
        if not datos['usuario'] or not datos['contraseña']:
            print("Usuario o contraseña no pueden estar vacíos")
        else:
            print(f"Usuario: {datos['usuario']}, Contraseña: {datos['contraseña']}")

    def iniciarVista(self):
        self.inicioSesion = inicioSesionVista(controlador=self)
        auxFormulario = self.inicioSesion.crearFormulario()
        contenedor = self.inicioSesion.contenedorModelo(auxFormulario)
        self.inicioSesion.vistaInicio(contenedor)
        auxFormulario.mainloop()

controlador = controladorInicio()
controlador.iniciarVista()



