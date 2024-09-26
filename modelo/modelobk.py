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
                  consulta = "INSERT INTO productos (nombreP, cantidad, precio, categoria) VALUES (%s, %s, %s, %s)"
                  self.cursor.execute(consulta, (producto["nombreP"], producto["cantidad"], producto["precio"], producto["categoria"]))
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
                        consulta = "SELECT nombreP, cantidad, precio, categoria FROM productos"
                        self.cursor.execute(consulta)
                  else:
                        # De lo contrario, filtrar por categoría
                        consulta = "SELECT nombreP, cantidad, precio, categoria FROM productos"
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
      
      def actualizar_producto(self, producto):
            query = "UPDATE productos SET nombreP=%s, cantidad=%s, precio=%s, categoria=%s WHERE nombreP=%s"
            producto = (producto["nombreP"], producto["cantidad"], producto["precio"], producto["categoria"], producto["nombre_nuevo"])
            try:
                  self.cursor.execute(query, producto)
                  self.conexion.commit()
                  return True
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False
      
      def obtenerProductosPorCategoria(self, categoria):
            cursor = self.conexion.cursor()
            query = "SELECT nombreP, precio, descripcion FROM productos WHERE categoria = ?"
            cursor.execute(query, (categoria,))
            productos = cursor.fetchall()
            # Los guardamos en el diccionario
            productos_formato = [{"nombreP": row[0], "precio": row[1], "descripcion": row[2]} for row in productos]
            return productos_formato
