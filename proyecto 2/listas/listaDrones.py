from nodos.nodoDron import nodoDron
from Dron import Dron

class listaDrones:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,Dron):
        nuevo_nodo = nodoDron(Dron)
        
        if self.primero is None or Dron.nombre_dron < self.primero.Dron.nombre_dron:
            nuevo_nodo.siguiente = self.primero
            self.primero=nuevo_nodo
            return
        actual=self.primero
        while actual.siguiente and actual.siguiente.Dron.nombre_dron < Dron.nombre_dron:
            actual=actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente=nodoDron(Dron)

    def imprimir(self):
        print("")
        actual=self.primero
        print("DRONES ENCONTRADOS")
        while actual!= None:
            print("Dron:",actual.Dron.nombre_dron)
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