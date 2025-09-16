from paprika import *
from localidad import Localidad


@data
class Domicilio:
    calle: str
    numero: int
    cp: int

    localidad: Localidad
