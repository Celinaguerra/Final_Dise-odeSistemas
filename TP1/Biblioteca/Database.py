import threading
import time

class Database:
    """
    Clase Database que implementa el patrón Singleton.
    Esta clase asegura que solo exista una única instancia de la base de datos
    en toda la aplicación, de una manera segura para entornos multi-hilo.
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """
        El método __new__ es el responsable de crear la instancia.
        Aquí implementamos la lógica del Singleton.
        """
        if cls._instance:
            return cls._instance


        with cls._lock:
            if cls._instance is None:
                print("Creando base de datos...")
                # Lazy Initialization
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """
        El inicializador se encarga de preparar el estado del objeto.
        Nos aseguramos de que solo se ejecute una vez.
        """
        if self._initialized:
            return
        
        self.libros = []
        self._initialized = True

    def agregar_libro(self, titulo: str, autor: str):
        """
        Agrega un nuevo libro a nuestra base de datos.
        """
        print(f"Agregando libro '{titulo}' de {autor}.")
        self.libros.append({"titulo": titulo, "autor": autor})

    def listar_libros(self):
        """
        Muestra todos los libros actualmente en la base de datos.
        """
        print("\n--- Catálogo de Libros ---")
        if not self.libros:
            print("Base de datos vacía.")
        else:
            for libro in self.libros:
                print(f"- Título: {libro['titulo']}, Autor: {libro['autor']}")
        print("------------------------------------------")

if __name__ == "__main__":

    # 1. Obtenemos dos "instancias" de la base de datos.
    print("Intentando obtener la primera instancia (db1)...")
    db1 = Database()

    print("\nIntentando obtener la segunda instancia (db2)...")
    db2 = Database()

    # 2. Comprobamos si ambas variables apuntan al mismo objeto en memoria.
    print(f"\nID de db1: {id(db1)}")
    print(f"ID de db2: {id(db2)}")

    if id(db1) == id(db2):
        print("¡Éxito! Ambas variables apuntan a la MISMA instancia.")
    else:
        print("¡Error! Se crearon dos instancias diferentes.")
    
    assert db1 is db2, "Las instancias no son las mismas."
    print("Las instancias son las mismas.\n")

    db1.agregar_libro("El Aleph", "Jorge Luis Borges")
    db1.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez")

    db2.listar_libros()