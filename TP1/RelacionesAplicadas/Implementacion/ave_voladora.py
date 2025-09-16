from abc import ABC, abstractmethod

# Interfaz (Clase Base Abstracta)
class AveVoladora(ABC):
    @abstractmethod
    def volar(self):
        pass