from nodos.nodoSistemasDrones import nodoSistemasDrones
from SistemasDrones import SistemasDrones
from listas.listaContenido import listaContenido

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
        print("==================Sistema De Drones============")
        while actual!= None:
            print("---------------------------------------------------------")
            print(f"Nombre Sistema: {actual.SistemasDrones.nombre_sistema}, Altura maxima: {actual.SistemasDrones.altura_max}, Cantidad Drones: {actual.SistemasDrones.cantidad_drones} ")
            print("---------------------------------------------------------")
            actual.SistemasDrones.listaContenido.imprimir()
            actual=actual.siguiente
        print("_____________________________________________________")
    
    def encontrar_listaContenido(self,sistema):
        actual = self.primero
        while actual!= None:
            if sistema == actual.SistemasDrones.nombre_sistema:
                return actual.SistemasDrones.listaContenido
            actual = actual.siguiente
    
    def generar_dot(self):
        dot_code = ""

        aux = self.primero
        while aux:
            # Utilizamos etiquetas  para personalizar la apariencia del nodo
            dot_code += f'"{aux.SistemasDrones.nombre_sistema}" [label=<<table border="0" cellborder="1" cellspacing="0" bgcolor="skyblue1"><tr><td>{aux.SistemasDrones.nombre_sistema}</td></tr>{aux.SistemasDrones.listaContenido.generar_dot()}{aux.SistemasDrones.listaAlturasSistema.generar_dot()}</table>>];\n'
            aux = aux.siguiente

        return dot_code

    def recorrer_grafica(self):
        f = open('bb.dot', 'w')

        dot_code = f"""
        digraph G {{
            node [shape=plaintext];  // Establecemos la forma del nodo como "plaintext"
            {self.generar_dot()}
        }}
        """

        f.write(dot_code)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f"dot -Tpng bb.dot -o Graficasistemas.png")
        
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