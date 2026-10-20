class Remito:
    def __init__(self, numero, fecha, estado, origen, destino):
        self.numero = numero
        self.fecha = fecha
        self.estado = estado
        self.origen = origen
        self.destino = destino
        self.detalle_remito = []

    def get_numero(self):
        pass

    def buscar_documentacion(self):
        pass

    def actualizar_estado_doc(self):
        pass

    def estas_generado(self):
        pass

    def get_datos_remito(self):
        pass

    def modificar_documentacion_incluida(self):
        pass

    def mostrar_informacion_remito(self):
        pass

    def set_estado(self, estado):
        pass

    def tenes_esta_cm_destino(self, cm):
        pass

    def tenes_esta_cm_origen(self, cm):
        pass

    def tomar_documentacion(self, detalle):
        pass

    def set_estado_recibida_y_aceptada(self, estado):
        pass

    def recibir_y_aceptar(self, estado):
        pass