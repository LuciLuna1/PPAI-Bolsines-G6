class Empleado:
    def __init__(self, nombre, apellido, email, comision_medica=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.comision_medica = comision_medica

    def es_tu_usuario(self, usuario):
        pass

    def get_cm(self):
        pass