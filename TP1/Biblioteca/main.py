from database import Database
from libro import LogisticaLibro, LogisticaFisica, LogisticaDigital
from abstract_factory import ExperienciaUsuarioFactory, AdminFactory, UsuarioFactory

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

