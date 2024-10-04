import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json

from vista.inicioSesion import inicioSesionVista
from modelo.modelobk import modelo 
from vista.menu import menuInterfaz 

class controladorInicio:
    def __init__(self):
        self.modelo = modelo()
        self.inicioSesion = None
        self.menu = None
        self.productosObte = []
    
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

    def iniciarVista(self):
        self.inicioSesion = inicioSesionVista(controlador=self)
        auxFormulario = self.inicioSesion.crearFormulario()
        contenedor = self.inicioSesion.contenedorModelo(auxFormulario)
        self.inicioSesion.vistaInicio(contenedor)
        auxFormulario.mainloop()
    
    def iniciarMenu(self, rol):
        self.menu = menuInterfaz(rol,controlador=self)
        self.menu.iniciar()
    
    def cargarProductosDesdeJSON(self, archivo="productos.json"):
        if os.path.exists(archivo):
            with open(archivo, "r") as file:
                producto = json.load(file)
                if not producto:  # Si el archivo está vacío
                    self.producto = self.productosObte
                    print("Archivo JSON vacío, creando productos por defecto.")
                    self.guardarProductosEnJSON()
                else:
                    self.producto = producto
                    print("Productos cargados desde JSON.")
        else:
            self.producto = self.productosObte
            print("Archivo JSON no encontrado, creando archivo.")
            self.guardarProductosEnJSON()

    def guardarProductosEnJSON(self, archivo="productos.json"):
        with open(archivo, "w") as file:
            json.dump(self.productos, file)
        print("Productos guardados en JSON.")

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
    
    def iniciarGuardarPro(self):
        if self.inventario:
            self.inventario.guardarProducto()
    
    def GuardarProducto(self, productoNuevo):
        if self.inventario:
            enviar = self.modelo.crearProducto(productoNuevo)
            if enviar ==  True:
                self.filtro("todos")
                return enviar
    
    def iniciarEliminar(self):
        self.inventario.eliminarProducto()
    
    def eliminarProducto(self, eliminar):
        if self.inventario:
            eliminado = self.modelo.eliminar_producto(eliminar)
            self.filtro("todos")
            return eliminado
    
    def iniciarActualizacion(self):
        self.inventario.editarProducto()
    
    def actualizarProducto(self,productoActualizar):
        if self.inventario:
            print("Datos a actualizar:", productoActualizar)
            enviar = self.modelo.actualizar_producto(productoActualizar)
            if enviar ==  True:
                self.filtro("todos")
                return enviar
    
    def informesClase(self, informes): #esencial para los eventos de informes
        self.informes = informes
    
    def ProductosInformes(self, categoria):
        self.productos = self.modelo.obtener_productos(categoria)
        print(f"Productos obtenidos: {self.productos}")
        return self.productos
    
    def asignarProductos(self, productos):
        self.productosObte = productos
    
    def guardarInforme(self):
        try:
        # Cargar productos desde el archivo JSON
            with open("productos.json", "r") as json_file:
                productos = json.load(json_file)
            
            if not productos:
                print("No hay productos para incluir en el informe.")
                mensaje = {"confirmacion": "fallido", "mensaje": "No hay productos en el inventario"}
                self.informes.confirmacion(mensaje)
                return
            
            # Generar el informe en el archivo .txt
            with open("informeProductos.txt", "w") as file:
                # Titulo del archivo
                file.write("Informe de Productos\n")
                file.write("=====================\n\n")

                # Revisar que tenga productos disponibles
                for producto in productos:
                    file.write(f"Nombre: {producto['nombreP']}\n")
                    file.write(f"Cantidad: {producto['cantidad']}\n")
                    file.write(f"Precio: {producto['precio']}\n")
                    file.write(f"Categoria: {producto['categoria']}\n")
                    file.write("-------------------------------\n")
                print("Informe generado exitosamente.")
                
                mensaje = {"confirmacion": "creado", "mensaje": "Informe creado correctamente"}
                self.informes.confirmacion(mensaje)
        except Exception as e:
            print(f"Error al guardar el informe: {e}")
            mensaje = {"confirmacion": "fallido", "mensaje": "Error al guardar el informe"}
            self.informes.confirmacion(mensaje)


controlador = controladorInicio()
controlador.iniciarVista()