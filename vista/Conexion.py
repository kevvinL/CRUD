import mysql.connector


class CConexion:
    def conexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                port = 3306,
                user="root",
                password = "",
                database="Negocio",
            )
            
            if conexion.is_connected():
                print("conexion correcta")
            return conexion
        except mysql.connector.Error as e:
            print("Error en la conexion: {}".format(e))
            return conexion
    conexionBaseDeDatos()