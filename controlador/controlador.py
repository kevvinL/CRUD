import json
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
    
    def enviosDatos(self):
        if self.inicioSesion:
            self.inicioSesion.enviarDatos()
    
    def inicioUsuario(self, datos):
        if not datos['usuario'] or not datos['contraseña']:
            return False
        else:
            usuarioEnviar = self.modelo.inicioSesion(datos)
            print(usuarioEnviar, "trae de modelo")
            print(f"Usuario: {datos['usuario']}, Contraseña: {datos['contraseña']}")
            
            if usuarioEnviar["verificado"] == False:
                return False 
            else:
                self.inicioSesion.sesion.destroy()
                self.iniciarMenu(usuarioEnviar["rol"])

    def cargarProductosDesdeJSON(self, archivo="productos.json"):
        if os.path.exists(archivo):
            with open(archivo, "r") as file:
                self.productos = json.load(file)
                print("Productos cargados desde el archivo JSON.")
        else:
            self.productos = []
            print("Creando Archivo json.")

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
            self.cargarProductosDesdeJSON()
            self.menu.mostrarInforme(controlador=self)
    
    def mostrarProductosPorCategoria(self, categoria):
        if self.menu:
            self.menu.mostrarProductos(categoria)
    
    def cerrarMenu(self):
        if self.menu:
            self.menu.cerrarSesion()
            self.iniciarVista()
    
    def IniciarInventario(self):
        if self.menu:
            self.menu.inventario(controlador=self)
    
    def filtro(self, categoria):
        print(f"Filtrando productos para la categoría: {categoria}")
        self.productos = self.modelo.obtener_productos(categoria)
        print(f"Productos obtenidos: {self.productos}")
        
        if self.productos is None:
            print(f"No se encontraron productos para la categoría: {categoria}")
            self.productos = []  # Asignar una lista vacía si no hay productos

        self.menu.mostrarProductos(self.productos)

    
    def consultaInventario(self, categoria):
        productos = self.productos = self.modelo.obtener_productos(categoria)
        return productos
    
    def inventarioClase(self, inventario): #esencial para los eventos del inventario
        self.inventario = inventario
    
    def iniciarCrearProducto(self):
        self.inventario.abrirVentanaRegistro()
    
    def guardarProductosEnJSON(self, archivo="productos.json"):
        with open(archivo, "w") as file:
            json.dump(self.productos, file, indent=4)
            print("Productos guardados en el archivo JSON.")

    def GuardarProducto(self, productoNuevo):
        if self.inventario:
            enviar = self.modelo.crearProducto(productoNuevo)
            if enviar ==  True:
                self.filtro("todos")
                self.guardarProductosEnJSON()
                return enviar
    
    def iniciarEliminar(self):
        self.inventario.eliminarProducto()
    
    def eliminarProducto(self, eliminar):
        if self.inventario:
            eliminado = self.modelo.eliminar_producto(eliminar)
            self.filtro("todos")
            self.guardarProductosEnJSON()
            return eliminado
    
    def iniciarActualizacion(self):
        self.inventario.editarProducto()
    
    def actualizarProducto(self,productoActualizar):
        if self.inventario:
            print("Datos a actualizar:", productoActualizar)
            enviar = self.modelo.actualizar_producto(productoActualizar)
            if enviar ==  True:
                self.filtro("todos")
                self.guardarProductosEnJSON()
                return enviar


controlador = controladorInicio()
controlador.iniciarVista()