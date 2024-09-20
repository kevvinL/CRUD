import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vista.inicioSesion import inicioSesionVista
from modelo.modelobk import modelo 
from vista.menu import menuInterfaz 
from vista.inventario import GestionProductos
from vista.vistaInformes import Menu


class controladorInicio:
    def __init__(self):
        self.ventana = menuInterfaz() #para utilizarlo con todos
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
        #destruir la ventana del login o antes que llegue aqui ya debe estar destruida
        self.inicioSesion = inicioSesionVista(controlador=self)
        auxFormulario = self.inicioSesion.crearFormulario()
        contenedor = self.inicioSesion.contenedorModelo(auxFormulario)
        self.inicioSesion.vistaInicio(contenedor)
        auxFormulario.mainloop()
    
    def iniciarMenu(self):
        self.menu = menuInterfaz()
        self.menu.iniciar()
    
    def iniciarInventario(self, ventana):
        nueva_ventana = ventana
        menu_informe = Menu(nueva_ventana)
        nueva_ventana.mainloop()
    
    def guardarProducto(self, infoProducto):
        if nombreP and cantidad and precio and fecha:
            modelo_bd = modelo()  
            guardado = modelo_bd.inventario(nombreP, cantidad, precio, fecha)

            if guardado:
                print("Producto guardado correctamente en la base de datos.")
                self.limpiarFormulario()
                self.cargarDatos()
            else:
                print("Error al guardar el producto en la base de datos.")
        else:
            print("Por favor, completa todos los campos.")

controlador = controladorInicio()
controlador.iniciarVista()