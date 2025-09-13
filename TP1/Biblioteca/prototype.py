import copy
from datetime import date, timedelta
from usuario import Usuario

class Prestamo:
    """
    Representa un préstamo de un libro a un usuario.
    Implementa el patrón Prototype para facilitar la creación de nuevos préstamos
    basados en uno existente.
    """
    def __init__(self, libro: dict, usuario: Usuario, fecha_inicio: date, dias_prestamo: int = 15):
        self.libro = libro
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_inicio + timedelta(days=dias_prestamo)

    def __str__(self):
        info = (f"  - Libro: '{self.libro.get('titulo', 'N/A')}'\n"
                f"  - Usuario: {self.usuario.nombre}\n"
                f"  - Fecha de Inicio: {self.fecha_inicio}\n"
                f"  - Fecha de Vencimiento: {self.fecha_fin}")
        return info

    def clone(self):
        """
        Crea una copia profunda (deep copy) del objeto préstamo.
        Esto asegura que todas las estructuras de datos, incluso las mutables
        como el diccionario 'libro', sean completamente nuevas en el clon.
        """
        return copy.deepcopy(self)