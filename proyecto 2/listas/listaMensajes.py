from nodos.nodoMensajes import nodoMensajes
from Mensajes import Mensajes
import xml.etree.ElementTree as ET

class listaMensajes:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,Mensajes):
        nuevo_nodo = nodoMensajes(Mensajes)
        
        if self.primero is None or Mensajes.nombre_mensaje < self.primero.Mensajes.nombre_mensaje:
            nuevo_nodo.siguiente = self.primero
            self.primero=nuevo_nodo
            return
        actual=self.primero
        while actual.siguiente and actual.siguiente.Mensajes.nombre_mensaje < Mensajes.nombre_mensaje:
            actual=actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente=nodoMensajes(Mensajes)

    def imprimir(self):
        actual=self.primero
        print("CONTENIDO")
        while actual!= None:
            print("============================================")
            print(f"Nombre del mensaje: {actual.Mensajes.nombre_mensaje}, Sistema de drones: {actual.Mensajes.sistema_drones}")
            print("============================================")
            actual.Mensajes.listaInstrucciones.imprimir()
            actual=actual.siguiente
    
    def encontrar_sistema(self,nombre):
        actual = self.primero
        while actual!= None:
            if nombre == actual.Mensajes.sistema_drones:
                return actual.Mensajes.listaInstrucciones
            actual = actual.siguiente
    
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