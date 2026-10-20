class Documentacion:
    def __init__(self, asunto, fecha_pase, numero, tipo_documentacion):
        self.asunto = asunto
        self.fecha_pase = fecha_pase
        self.numero = numero
        self.tipo_documentacion = tipo_documentacion
        self.cambio_estado_documentacion = []

    def get_asunto(self):
        pass

    def get_tipo_documentacion(self):
        pass

    def set_estado_recibida_y_aceptada(self, estado):
        pass

    def get_cambio_estado_actual(self):
        pass

    def crear_cambio_estado(self, estado, fecha_hora):
        pass

    def incluir_en_remito(self):
        pass

    def asignar_documentacion_a_bolsin(self):
        pass

    def desasignar_bolsin(self):
        pass

    def eliminar_del_bolsin(self):
        pass

    def comenzar_traslado(self):
        pass

    def asignar_no_recibida(self):
        pass

    def aceptar(self):
        pass

    def rechazar(self):
        pass

    def redirigir(self):
        pass

    def solicitar_documentacion(self):
        pass

    def dar_de_baja(self):
        pass

    def reasignar(self):
        pass
