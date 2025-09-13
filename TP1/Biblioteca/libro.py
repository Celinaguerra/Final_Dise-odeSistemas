from abc import ABC, abstractmethod
from database import Database

# Product
class Libro(ABC):
    @abstractmethod
    def obtener_info(self) -> str:
        pass

# Concrete Product
class LibroFisico(Libro):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def obtener_info(self) -> str:
        return f"Libro Físico: '{self.titulo}' por {self.autor}."

# Concrete Product
class LibroDigital(Libro):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def obtener_info(self) -> str:
        return f"Libro Digital: '{self.titulo}' por {self.autor}."

# Creator
class LogisticaLibro(ABC):
    @abstractmethod
    def factory_method(self, titulo: str, autor: str) -> Libro:
        pass

    def crear_libro(self, titulo: str, autor: str) -> str:
        libro = self.factory_method(titulo, autor)
        info = libro.obtener_info()
        print(f"Libro creado con éxito. {info}")
        
        db = Database()
        db.agregar_libro(titulo, autor, tipo=libro.__class__.__name__)
        
        return info

# Concrete Creator
class LogisticaFisica(LogisticaLibro):
    def factory_method(self, titulo: str, autor: str) -> Libro:
        return LibroFisico(titulo, autor)

# Concrete Creator
class LogisticaDigital(LogisticaLibro):
    def factory_method(self, titulo: str, autor: str) -> Libro:
        return LibroDigital(titulo, autor)