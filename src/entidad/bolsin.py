from datetime import date
from typing import List, Optional
from src.entity.remito import Remito  # O la ruta donde se ubique Remito


class Bolsin:
    def __init__(
        self,
        nro_precinto: int,
        fecha: date,
        nro_bolsin: int,
        peso: float,
       
    ):
        self._nro_precinto = nro_precinto
        self._fecha = fecha
        self._nro_bolsin = nro_bolsin
        self._peso = peso
