from documento import Documento

class Impresora:
    def imprimir(self, doc: Documento):
        print(f"Imprimiendo: {doc.contenido}")