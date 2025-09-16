from paprika import *
from articulo import Articulo

@data
class Articulo_Insumo(Articulo):
    denominacion: str
    precioCompra: float
    stockActual: int
    stockMaximo: int
    esParaElaborar: bool
    id: int

    def calcular_precio_final(self):
        pass