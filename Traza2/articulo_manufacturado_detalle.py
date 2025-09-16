from paprika import *
from articulo_insumo import Articulo_Insumo

@data
class Articulo_Manufacturado_Detalle:
    cantidad: int
    id: int

    articulo_insumo: Articulo_Insumo