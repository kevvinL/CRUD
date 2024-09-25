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
        self.ventana = menuInterfaz()
        self.venInventario =GestionProductos()
        self.modelo = modelo()

    def inicioUsuario(self, datos):
        if not datos['usuario'] or not datos['contraseña']:
            print("Faltan datos")
            return False
        else:
            # Enviar datos al modelo para validación
            usuarioEnviar = self.modelo.inicioSesion(datos)
            print(f"Usuario: {datos['usuario']}, Contraseña: {datos['contraseña']}")

            if usuarioEnviar == "verificado":
                # Destruir la ventana de sesión solo si está abierta
                if hasattr(self, 'inicioSesion') and self.inicioSesion.sesion.winfo_exists():
                    self.inicioSesion.sesion.destroy()
                self.iniciarMenu()  # Ir al menú principal
            else:
                print("Credenciales incorrectas")
                return False

    def iniciarVista(self):
        #destruir la ventana del login o antes que llegue aqui ya debe estar destruida
        self.inicioSesion = inicioSesionVista(controlador=self)
        auxFormulario = self.inicioSesion.crearFormulario()
        contenedor = self.inicioSesion.contenedorModelo(auxFormulario)
        self.inicioSesion.vistaInicio(contenedor)
        auxFormulario.mainloop()

    def iniciarMenu(self):
        self.menu = menuInterfaz(controlador=self)
        self.menu.iniciar()

    def iniciarInventario(self):
        inventarioVista = GestionProductos(self)
        inventarioVista.iniciarVista()

    def guardarProducto(self, infoProducto):
        nombreP = infoProducto['nombreP']
        cantidad = infoProducto['cantidad']
        precio = infoProducto['precio']
        fecha = infoProducto['fecha']
        categoria = infoProducto['categoria']

        if nombreP and cantidad and precio and fecha and categoria:
            return self.modelo.inventario(nombreP, cantidad, precio, fecha, categoria)
        else:
            print("Error: Falta información del producto.")
            return False

    def mostrarP(self):
        productos = modelo.obtener_productos()
        return productos

    def obtenerProductos(self):
        return self.modelo.obtener_productos()

    def eliminarProducto(self, nombreP):
        return self.modelo.eliminar_producto(nombreP)

    def actualizarProducto(self, nombre_original, nombreP, cantidad, precio, fecha, categoria):
        return self.modelo.actualizar_producto(nombre_original, nombreP, cantidad, precio, fecha, categoria)


controlador = controladorInicio()
controlador.iniciarVista()