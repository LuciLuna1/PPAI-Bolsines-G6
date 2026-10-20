class Estado:
    def __init__(self, ambito, nombre, descripcion=""):
        self.ambito = ambito
        self.nombre = nombre
        self.descripcion = descripcion

    def es_ambito_bolsin(self):
        pass

    def es_ambito_documentacion(self):
        pass

    def es_ambito_remito(self):
        pass

    def es_enviado(self):
        pass

    def es_recibida_y_aceptada(self):
        pass

    def es_recibido_en_cm_destino(self):
        pass

    def es_recibido_y_aceptado(self):
        pass

    def get_ambito(self):
        pass

    def set_ambito(self, ambito):
        pass

    def get_descripcion(self):
        pass

    def set_descripcion(self, descripcion):
        pass

    def get_nombre(self):
        pass

    def set_nombre(self, nombre):
        pass
