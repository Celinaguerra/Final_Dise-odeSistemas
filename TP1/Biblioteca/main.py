from database import Database
from libro import LogisticaLibro, LogisticaFisica, LogisticaDigital
from abstract_factory import ExperienciaUsuarioFactory, AdminFactory, UsuarioFactory
from usuario import UsuarioBuilder
from prototype import Prestamo
from datetime import date, timedelta


def client_code(creador: LogisticaLibro, titulo: str, autor: str):
    """
    Función cliente que trabaja con un creador abstracto.
    """
    creador.crear_libro(titulo, autor)

def configurar_abstract_factory(factory: ExperienciaUsuarioFactory):
    interfaz = factory.crear_interfaz_ui()
    envio = factory.crear_metodo_envio()

    interfaz.render()
    envio.describir_envio()

if __name__ == "__main__":

#------ Parte 1 ------

    db1 = Database()
    db2 = Database()
    assert db1 is db2
    print("Ambas instancias son la misma (verifica Singleton).")

#------ Parte 2 ------

    print("\nCreando libro físico con LogisticaFisica...")
    logistica_envio = LogisticaFisica()
    client_code(logistica_envio, "Ficciones", "Jorge Luis Borges")

    print("\nCreando libro digital con LogisticaDigital...")
    logistica_descarga = LogisticaDigital()
    client_code(logistica_descarga, "El Túnel", "Ernesto Sábato")
    
    db1.listar_libros()

#------ Parte 3 ------

    # El usuario es un Administrador
    print("\n--- Configurando para un Administrador ---")
    admin_factory = AdminFactory()
    configurar_abstract_factory(admin_factory)

    # El usuario es un cliente normal
    print("\n--- Configurando para un Usuario ---")
    usuario_factory = UsuarioFactory()
    configurar_abstract_factory(usuario_factory)

#------ Parte 4 ------
    
    # Usuario con todos sus datos opcionales.
    usuario_completo = (UsuarioBuilder("Juan Pérez", "juan.perez@example.com")
                        .con_direccion("Av. Siempre Viva 742")
                        .con_telefono("555-1234")
                        .construir())
    print("\nInformación del Usuario 1:")
    print(usuario_completo)

    # Usuario solo con los datos obligatorios.
    usuario_simple = (UsuarioBuilder("Ana Gómez", "ana.gomez@example.com")
                        .construir())
    print("\nInformación del Usuario 2:")
    print(usuario_simple)

#------ Parte 5 ------
    libro_prototipo = {"titulo": "Guía del Autoestopista Galáctico", "autor": "Douglas Adams"}
    
    # Crear un préstamo estándar.
    print("\n--- Creando Préstamo Estándar ---")
    prestamo_prototipo = Prestamo(libro=libro_prototipo, 
                                    usuario=usuario_completo, 
                                    fecha_inicio=date(2025, 9, 12))
    print("Préstamo Original:")
    print(prestamo_prototipo)
    print(f"ID del objeto original: {id(prestamo_prototipo)}")

    # Clonar el prototipo para un nuevo préstamo de otro libro.
    print("\n--- Clonando para un segundo préstamo ---")
    prestamo_clon1 = prestamo_prototipo.clone()
    prestamo_clon1.libro = {"titulo": "El Restaurante del Fin del Mundo", "autor": "Douglas Adams"}
    print("Primer Clon:")
    print(prestamo_clon1)
    print(f"ID del primer clon: {id(prestamo_clon1)}")

    # Clonar el prototipo para una modificación del préstamo original.
    print("\n--- Clonando para una modificación ---")
    prestamo_clon2 = prestamo_prototipo.clone()
    prestamo_clon2.fecha_fin += timedelta(days=15) # Le sumamos 15 días a la fecha de fin
    print("Segundo Clon:")
    print(prestamo_clon2)
    print(f"ID del segundo clon: {id(prestamo_clon2)}")

    print("\n--- Verificación Final ---")
    print(f"Fecha fin original: {prestamo_prototipo.fecha_fin}")
    print(f"Fecha fin clon 2 (modificada): {prestamo_clon2.fecha_fin}")
    print("Los clones son independientes y las modificaciones no afectan al original.")