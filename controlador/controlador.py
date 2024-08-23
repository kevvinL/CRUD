from vista.inicioSesion import inicioSesionVista

class controaldor:
    def __init__(self):
        pass
    
    def inicioUsuario(self, datosUsuario):
        if not (datosUsuario.usaurio and not datosUsuario.contraseña):
            print("enviar la informacion")
        
        print(datosUsuario)
        #iniciar = 

    def iniciarVista(self):
        self.iniciar()

controlador = controaldor()
controaldor.iniciarVista()



