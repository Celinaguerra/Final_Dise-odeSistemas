from abc import ABC, abstractmethod

# Abstract Product
class InterfazUI(ABC):
    @abstractmethod
    def render(self):
        pass

# Abstract Product
class MetodoEnvio(ABC):
    @abstractmethod
    def describir_envio(self):
        pass

# Concrete Product
class AdminUI(InterfazUI):
    def render(self):
        print("UI para Administrador: [Panel de Control, Reportes, Gestión de Usuarios]")

# Concrete Product
class EnvioExpress(MetodoEnvio):
    def describir_envio(self):
        print("Método de Envío: Express (Prioritario para Admins, entrega en 24hs)")

# Concrete Product
class UsuarioUI(InterfazUI):
    def render(self):
        print("UI para Usuario: [Catálogo de Libros, Mi Perfil, Carrito de Compras]")

# Concrete Product
class EnvioNormal(MetodoEnvio):
    def describir_envio(self):
        print("Método de Envío: Normal (Estándar para Usuarios, entrega en 3-5 días)")

# Abstract Factory
class ExperienciaUsuarioFactory(ABC):
    @abstractmethod
    def crear_interfaz_ui(self) -> InterfazUI:
        pass

    @abstractmethod
    def crear_metodo_envio(self) -> MetodoEnvio:
        pass

# Concrete Factory
class AdminFactory(ExperienciaUsuarioFactory):
    def crear_interfaz_ui(self) -> InterfazUI:
        return AdminUI()

    def crear_metodo_envio(self) -> MetodoEnvio:
        return EnvioExpress()

# Concrete Factory
class UsuarioFactory(ExperienciaUsuarioFactory):
    def crear_interfaz_ui(self) -> InterfazUI:
        return UsuarioUI()

    def crear_metodo_envio(self) -> MetodoEnvio:
        return EnvioNormal()