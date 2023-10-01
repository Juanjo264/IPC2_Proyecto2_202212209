from nodos.nodoContenido import nodoContenido
from Contenido import Contenido
from listas.listaAlturas import listaAlturas

class listaContenido:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,Contenido):
        if self.primero is None:
            self.primero=nodoContenido(Contenido)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoContenido(Contenido)

    def imprimir(self):
        actual=self.primero
        print("LISTA DE CONTENIDOS")
        while actual!= None:
            print(f"Dron: {actual.Contenido.dron}")
            actual.Contenido.listaAlturas.imprimir()
            actual=actual.siguiente
            print("=====================================")
    
    def get_listaAlturas(self,dron):
        actual = self.primero
        while actual!= None:
            if dron == actual.Contenido.dron:
                return actual.Contenido.listaAlturas
            actual = actual.siguiente
