import mysql.connector

class modelo:
      def __init__(self):
            self.conexion = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  port=3306,
                  password="",
                  database="negocio"
            )
            self.cursor = self.conexion.cursor(dictionary=True)

      def inicioSesion(self, datos):
            try:
                  consulta = "SELECT * FROM usuarios WHERE gmail = %s AND contraseña = %s"
                  self.cursor.execute(consulta, (datos['usuario'], datos['contraseña']))
                  resultado = self.cursor.fetchone()
                  print(resultado)
                  if resultado:
                        necesario = {"rol": resultado["rol"], "verificado": True}
                        return necesario
                  else:
                        return False

            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False

      def crearProducto(self, producto):
            try:
                  consulta = "INSERT INTO productos (nombreP, cantidad, precio) VALUES (%s, %s, %s)"
                  self.cursor.execute(consulta, (producto["nombreP"], producto["cantidad"], producto["precio"]))
                  self.conexion.commit()
                  print("Producto insertado correctamente")
                  return True
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False

      def obtener_productos(self, categoria=None):
            try:
                  print(categoria, "modelo")
                  # Si no hay categoría o la categoría es 'todos', obtener todos los productos
                  if not categoria or categoria == "todos":
                        consulta = "SELECT nombreP, cantidad, precio FROM productos"
                        self.cursor.execute(consulta)
                  else:
                        # De lo contrario, filtrar por categoría
                        consulta = "SELECT nombreP, cantidad, precio FROM productos"
                        self.cursor.execute(consulta)
                  
                  productos = self.cursor.fetchall()
                  print(f"Productos devueltos por la consulta: {productos}")
                  return productos
                  #return self.cursor.fetchall()
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return []

      def eliminar_producto(self, nombreP):
            try:
                  consulta = "DELETE FROM productos WHERE nombreP = %s"
                  self.cursor.execute(consulta, (nombreP,))
                  self.conexion.commit()
                  return self.cursor.rowcount > 0 
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False
      
      def actualizar_producto(self, nombreP, nuevo_nombre, cantidad, precio, fecha):
            query = "UPDATE productos SET nombreP=%s, cantidad=%s, precio=%s WHERE nombreP=%s"
            parametros = (nuevo_nombre, cantidad, precio, fecha, nombreP)
            try:
                  self.cursor.execute(query, parametros)
                  self.conexion.commit()
                  return True
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False
      
      def obtener_categorias(self):
        self.cursor.execute("SELECT nombre FROM categorias")
        categorias = self.cursor.fetchall()
        return [categoria[0] for categoria in categorias]