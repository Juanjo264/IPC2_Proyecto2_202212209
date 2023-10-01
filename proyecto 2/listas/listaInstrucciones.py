from nodos.nodoInstrucciones import nodoInstrucciones
from Instrucciones import Instrucciones

class listaInstrucciones:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,Instrucciones):
        if self.primero is None:
            self.primero=nodoInstrucciones(Instrucciones)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoInstrucciones(Instrucciones)

    def imprimir(self):
        
        actual=self.primero
        print("INSTRUCCIONES")
        while actual!= None:
            print(f"Dron: {actual.Instrucciones.dron_actual},pocicion: {actual.Instrucciones.posicion}")
            actual=actual.siguiente
        print("=======================")
    
    def eliminar_datos(self):
        while self.primero:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual
    
    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is not None:
            valor_actual = self.actual
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration