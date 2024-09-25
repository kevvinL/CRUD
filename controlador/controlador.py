import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vista.inicioSesion import inicioSesionVista
from modelo.modelobk import modelo 
from vista.menu import menuInterfaz 
from vista.inventario import GestionProductos

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
            print(usuarioEnviar, "trae de modelo")
            print(f"Usuario: {datos['usuario']}, Contraseña: {datos['contraseña']}")
            
            if usuarioEnviar["verificado"] == True:
                self.inicioSesion.sesion.destroy()
                self.iniciarMenu(usuarioEnviar["rol"])
            else:
                return False

    def iniciarVista(self):
        self.inicioSesion = inicioSesionVista(controlador=self)
        auxFormulario = self.inicioSesion.crearFormulario()
        contenedor = self.inicioSesion.contenedorModelo(auxFormulario)
        self.inicioSesion.vistaInicio(contenedor)
        auxFormulario.mainloop()
    
    def iniciarMenu(self, rol):
        self.menu = menuInterfaz(rol,controlador=self)
        self.menu.iniciar()
    
    def informe(self):
        if self.menu:
            self.menu.mostrarInforme()
    
    def mostrarProductosPorCategoria(self, categoria):
        productos = self.modelo.obtener_productos(categoria)  # Se asegura de no enviar una lista vacia
        return productos
    
    def cerrarMenu(self):
        if self.menu:
            self.menu.cerrarSesion()
            self.iniciarVista()
    
    def IniciarInventario(self):
        if self.menu:
            self.menu.inventario(controlador=self)
    
    def filtro(self, categoria):
        print(categoria, "controlador")
        self.productos = self.modelo.obtener_productos(categoria)
        return self.productos
    
    def consultaInventario(self, categoria):
        productos = self.productos = self.modelo.obtener_productos(categoria)
        return productos
    
    def inventarioClase(self, inventario): #esencial para los eventos del inventario
        self.inventario = inventario
    
    def iniciarCrearProducto(self):
        self.inventario.abrirVentanaRegistro()
    
    def GuardarProducto(self, productoNuevo):
        if self.inventario:
            enviar = self.modelo.crearProducto(productoNuevo)
            self.filtro("todos")
            return enviar
    
    def eliminarProducto(self, eliminar):
        if self.inventario:
            eliminado = self.modelo.eliminar_producto(eliminar)
            self.filtro("todos")
            return eliminado


controlador = controladorInicio()
controlador.iniciarVista()