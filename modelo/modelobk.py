import mysql.connector

class modelo:
      def __init__(self):
            self.conexion = mysql.connector.connect(
                  host="localhost",
                  user="root", 
                  port = 3306,
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

      def cerrar_conexion(self):
            self.cursor.close()
            self.conexion.close()