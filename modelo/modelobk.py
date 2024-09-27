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
                  if not categoria or categoria == "todos":
                        # Obtener todos los productos si la categoría es "todos" o no se especifica
                        consulta = "SELECT nombreP, cantidad, precio, categoria FROM productos"
                        self.cursor.execute(consulta)
                  else:
                        # Filtrar productos por categoría específica
                        consulta = "SELECT nombreP, cantidad, precio, categoria FROM productos WHERE categoria = %s"
                        self.cursor.execute(consulta, (categoria,))  # Pasar la categoría como parámetro
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
