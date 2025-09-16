from habitacion import Habitacion

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = [
            Habitacion("Dormitorio"),
            Habitacion("Baño"),
            Habitacion("Cocina")
        ]

    def __del__(self):
        print(f"La casa en {self.direccion} ha sido demolida, y con ella las habitaciones.")