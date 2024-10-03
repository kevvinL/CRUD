import mysql.connector

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
