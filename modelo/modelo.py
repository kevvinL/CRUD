
usuarios = [
      {
      "rol": "admin",
      "contraseña": "anshi"
},
{
      "rol": "venta",
      "contraseña": "angie"
}
]

class modelo:
      def inicioSesion(self, datosUsuario):
            if not datosUsuario['usuario'] or not datosUsuario['contraseña']:
                  print("Usuario o contraseña no pueden estar vacíos")
            else:
                  print(f"Usuario: {datosUsuario['usuario']}, Contraseña: {datosUsuario['contraseña']}")  
                  for usuario in usuarios:
                        if datosUsuario['usuario'] == usuarios['rol'] and datosUsuario['contraseña'] == usuarios['contraseña']:
                              print("Bienvenido")
                              return True
                        else:
                              return False
            