usuarios = [
    {
        "rol": "admin",
        "usuario": "angieg",
        "contraseña": "anshi"
    },
    {
        "rol": "venta",
        "usuario": "yuliana",
        "contraseña": "angie"
    }
]

class modelo:
    def inicioSesion(self, datosUsuario):
        if not datosUsuario['usuario'] or not datosUsuario['contraseña']:
            print("Usuario o contraseña no pueden estar vacíos")
            return False
        else:
            for usuario in usuarios:
                if datosUsuario['usuario'] == usuario['usuario'] and datosUsuario['contraseña'] == usuario['contraseña']:
                    print("Bienvenido", usuario['rol'])
                    return "verificado"
                else:
                    print("Credenciales incorrectas")