from paprika import *
from sucursal import Sucursal


@data
class Empresa:
    id: int
    nombre: str
    razonSocial: str
    cuit: int
    logo: str
    sucursales: set[Sucursal] = set()
