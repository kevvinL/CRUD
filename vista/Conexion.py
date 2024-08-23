import mysql.connector


class CConexion:
    def conexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password = "",
                database="Negocio",
            )
            print("conexion correcta")
            return conexion
        except mysql.connector.Error as e:
            print("Error en la conexion: {}".format(e))
            return conexion

    conexionBaseDeDatos()