import mysql.connector

class Usuario:
      def __init__(self, nombre, correo, rol):
            self._nombre = nombre
            self._correo = correo
            self._rol = rol

      @property
      def nombre(self):
            return self._nombre

      # Setter para nombre
      @nombre.setter
      def nombre(self, nuevoNombre):
            if isinstance(nuevoNombre, str) and nuevoNombre.strip():
                  self._nombre = nuevoNombre
            else:
                  raise ValueError("El nombre debe ser una cadena de texto válida.")

      # Getter para correo
      @property
      def correo(self):
            return self._correo

      # Setter para correo
      @correo.setter
      def correo(self, nuevoCorreo):
            if "@" in nuevoCorreo and "." in nuevoCorreo:  # Comprobación básica para validar el correo
                  self._correo = nuevoCorreo
            else:
                  raise ValueError("Correo no válido.")

      # Getter para rol
      @property
      def rol(self):
            return self._rol

      # Setter para rol
      @rol.setter
      def rol(self, nuevoRol):
            if nuevoRol in ["Vendedor", "Administrador"]:  # Comprobación para limitar los roles
                  self._rol = nuevoRol
            else:
                  raise ValueError("Rol no válido. Debe ser 'Vendedor' o 'Administrador'.")

      def mostrar_info(self):
            print(f"Nombre: {self.nombre}, Correo: {self.correo}, Rol: {self.rol}")

      def iniciar_sesion(self, datos):
            if datos['usuario'] == self.correo:
                  print(f"Inicio de sesión exitoso para {self.nombre}")
            else:
                  print(f"Error en inicio de sesión para {self.nombre}")
                  
class Vendedor(Usuario):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo, rol="Vendedor") #Vendedor no tiene un metodo unico

class Administrador(Usuario):
      def __init__(self, nombre, correo):
        super().__init__(nombre, correo, rol="Administrador")
      
      def generar_informes(self):
        # Método específico para el administrador
        print(f"{self.nombre} puede generar informes.")

class modelo:
      def __init__(self):
            self._conexion = None
            self.conectar() 

      @property
      def conexion(self):
            return self._conexion

      def conectar(self):
            try:
                  self._conexion = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  port=3306,
                  password="",
                  database="negocio"  # Nombre de la base de datos fijo
                  )
                  self.cursor = self._conexion.cursor(dictionary=True)
                  print("Conexión establecida con la base de datos.")
            except mysql.connector.Error as err:
                  print(f"Error al conectar a la base de datos: {err}")
      
      def inicioSesion(self, datos):
            try:
                  consulta = "SELECT * FROM usuarios WHERE gmail = %s AND contraseña = %s"
                  self.cursor.execute(consulta, (datos['usuario'], datos['contraseña']))
                  resultado = self.cursor.fetchone()
                  print(resultado)
                  if resultado:
                        necesario = {"rol": resultado["rol"], "verificado": True}
                  else:
                        necesario = {"verificado": False}
                  return necesario
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False

      def crearProducto(self, producto):
            try:
                  consulta = "INSERT INTO productos (nombreP, cantidad, precio, categoria) VALUES (%s, %s, %s, %s)"
                  self.cursor.execute(consulta, (producto["nombreP"], producto["cantidad"], producto["precio"], producto["categoria"]))
                  self._conexion.commit()
                  print("Producto insertado correctamente")
                  return True
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False

      def obtener_productos(self, categoria=None):
            try:
                  print(categoria, "modelo")
                  if not categoria or categoria == "todos":
                        consulta = "SELECT nombreP, cantidad, precio, categoria FROM productos"
                        self.cursor.execute(consulta)
                  else:
                        consulta = "SELECT nombreP, cantidad, precio, categoria FROM productos WHERE categoria = %s"
                        self.cursor.execute(consulta, (categoria,))
                  print(consulta)

                  productos = self.cursor.fetchall()
                  print(f"Productos devueltos por la consulta: {productos}")
                  return productos
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return []

      def eliminar_producto(self, nombreP):
            try:
                  consulta = "DELETE FROM productos WHERE nombreP = %s"
                  self.cursor.execute(consulta, (nombreP,))
                  self._conexion.commit()
                  return self.cursor.rowcount > 0 
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False

      def actualizar_producto(self, producto):
            query = "UPDATE productos SET nombreP=%s, cantidad=%s, precio=%s, categoria=%s WHERE nombreP=%s"
            producto_tuple = (producto["nombreP"], producto["cantidad"], producto["precio"], producto["categoria"], producto["nombre_nuevo"])
            try:
                  self.cursor.execute(query, producto_tuple)
                  self._conexion.commit()
                  return True
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False

      def cerrar_conexion(self):
            if self._conexion:
                  self.cursor.close() 
                  self._conexion.close() 
                  print("Conexión cerrada")


vendedor = Vendedor('vendedor', 'vendedor@gmail.com')
administrador = Administrador('administrador', 'admin@gmail.com')