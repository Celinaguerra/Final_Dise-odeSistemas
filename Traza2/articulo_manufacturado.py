from paprika import *
from articulo import Articulo
from typing import Set
from articulo_manufacturado_detalle import Articulo_Manufacturado_Detalle

@data
class Articulo_Manufacturado(Articulo):
    denominacion: str
    precioVenta: float
    id: int
    descripcion: str
    tiempoEstimadoMinutos: int
    preparacion: str
    detalles: Set["Articulo_Manufacturado_Detalle"]

    def calcular_precio_final(self):
        pass