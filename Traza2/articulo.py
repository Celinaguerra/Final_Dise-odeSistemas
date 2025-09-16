from paprika import *
from abc import ABC, abstractmethod
from imagen import Imagen
from typing import Set
from unidad_medida import Unidad_Medida

@data
class Articulo(ABC):
    denominacion: str
    precioVenta: float
    #id: int

    imagen: Set["Imagen"]
    unidad_medida: Unidad_Medida


    @abstractmethod
    def calcular_precio_final(self):
        pass