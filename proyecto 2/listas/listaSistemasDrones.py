from nodos.nodoSistemasDrones import nodoSistemasDrones
from SistemasDrones import SistemasDrones

import os

class listaSistemasDrones:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,SistemasDrones):
        if self.primero is None:
            self.primero=nodoSistemasDrones(SistemasDrones)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoSistemasDrones(SistemasDrones)

    def imprimir(self):
        actual=self.primero
        print("")
        print("SISTEMA DE DRONES")
        while actual!= None:
            print("================================================")
            print(f"Nombre del sistema: {actual.SistemasDrones.nombre_sistema}, Altura maxima :{actual.SistemasDrones.altura_max}, Cantidad de drones :{actual.SistemasDrones.cantidad_drones}")
            print("-----------------------------------------")
            actual.SistemasDrones.listaContenido.imprimir()
            actual=actual.siguiente
        print("============================================")
    
    def encontrar_listaContenido(self,sistema):
        actual = self.primero
        while actual!= None:
            if sistema == actual.SistemasDrones.nombre_sistema:
                return actual.SistemasDrones.listaContenido
            actual = actual.siguiente
