import re


class Usuario:
    # __slots__ previene la adición de nuevos atributos.
    __slots__ = ['_nombre', '_email', '_direccion', '_telefono']

    def __init__(self, nombre, email, direccion=None, telefono=None):
        self._nombre = nombre
        self._email = email
        self._direccion = direccion
        self._telefono = telefono
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @property
    def direccion(self):
        return self._direccion

    @property
    def telefono(self):
        return self._telefono

    def __str__(self):
        info = f"  Nombre: {self.nombre}\n  Email: {self.email}"
        if self.direccion:
            info += f"\n  Dirección: {self.direccion}"
        if self.telefono:
            info += f"\n  Teléfono: {self.telefono}"
        return info

# Builder
class UsuarioBuilder:
    def __init__(self, nombre: str, email: str):
        self.usuario = Usuario(nombre, email)

    def con_direccion(self, direccion: str):
        self.usuario._direccion = direccion
        return self

    def con_telefono(self, telefono: str):
        self.usuario._telefono = telefono
        return self

    def construir(self) -> Usuario:
        """
        Valida los datos y devuelve la instancia final e inmutable del Usuario.
        """
        if not self.usuario.nombre or not self.usuario.email:
            raise ValueError("El nombre y el email son campos obligatorios.")
        
        # validación de formato de email
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", self.usuario.email):
            raise ValueError("El formato del email no es válido.")
        
        return self.usuario