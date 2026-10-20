class Bolsin:
    def __init__(self, nro_precinto, fecha, numero_bolsin, peso, origen, destino):
        self.nro_precinto = nro_precinto
        self.fecha = fecha
        self.numero_bolsin = numero_bolsin
        self.peso = peso
        self.origen = origen
        self.destino = destino
        self.remito = []
        self.cambio_estado = []

    def es_tu_cm_destino(self, cm):
        pass

    def esta_enviado(self):
        pass

    def get_nro_precinto(self):
        pass

    def get_cm_origen(self):
        pass

    def obtener_remitos(self):
        pass

    def recibir_bolsin(self, estado, fecha_hora):
        pass

    def set_fecha_hora_fin(self, fecha):
        pass

    def crear_cambio_estado_bolsin(self, estado, fecha_hora, responsable=None):
        pass