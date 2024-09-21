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

                  if resultado:
                        return "verificado"
                  else:
                        return False

            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False

      def inventario(self, nombreP, cantidad, precio, fecha):
            try:
                  consulta = "INSERT INTO productos (nombreP, cantidad, precio, fecha) VALUES (%s, %s, %s, %s)"
                  self.cursor.execute(consulta, (nombreP, cantidad, precio, fecha))
                  self.conexion.commit()
                  print("Producto insertado correctamente")
                  return True
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False

      def obtener_productos(self):
            try:
                  consulta = "SELECT nombreP, cantidad, precio, fecha FROM productos"
                  self.cursor.execute(consulta)
                  return self.cursor.fetchall()
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
            query = "UPDATE productos SET nombreP=%s, cantidad=%s, precio=%s, fecha=%s WHERE nombreP=%s"
            parametros = (nuevo_nombre, cantidad, precio, fecha, nombreP)
            try:
                  self.cursor.execute(query, parametros)
                  self.conexion.commit()
                  return True
            except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return False
      
      def obtenerProductosPorCategoria(self, categoria):
            # Supongamos que tienes una conexión a la base de datos llamada 'conexion'
            cursor = self.conexion.cursor()
            query = "SELECT nombreP, precio, descripcion FROM productos WHERE categoria = ?"
            cursor.execute(query, (categoria,))
            productos = cursor.fetchall()
            # Estructuramos los datos en un diccionario
            productos_formato = [{"nombreP": row[0], "precio": row[1], "descripcion": row[2]} for row in productos]
            return productos_formato
