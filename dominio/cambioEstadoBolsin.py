class CambioEstadoBolsin:
    def __init__(self, estado, fecha_hora_inicio, responsable_ce=None):
        self.estado = estado
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = None
        self.responsable_ce = responsable_ce

    def sos_actual(self):
        pass

    def sos_enviado(self):
        pass

    def set_fecha_hora_fin(self, fecha):
        pass

    def get_fecha_hora_fin(self):
        pass

    def set_fecha_hora_inicio(self, fecha):
        pass

    def get_fecha_hora_inicio(self):
        pass
