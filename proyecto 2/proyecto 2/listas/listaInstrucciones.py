from nodos.nodoInstrucciones import nodoInstrucciones
import os

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
        print("--------------Lista Instrucciones----------")
        while actual!= None:
            print(f"Dron: {actual.Instrucciones.dron_actual}, Posicion: {actual.Instrucciones.posicion}")
            actual=actual.siguiente
        print("---------------------------------------------------------")
    
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
        
    def generar_dot_instrucciones(self):
        dot_code = "node [shape=box];\n"  # forma de los nodos

        aux = self.primero
        while aux:
            # Utiliza un formato para el nodo
            dot_code += f'"{id(aux)}" [label="Dron: {aux.Instrucciones.dron_actual} | Posicion: {aux.Instrucciones.posicion}"];\n'
            aux = aux.siguiente

        return dot_code

    def recorrer_grafica_instrucciones(self):
        dot_code = f"""
        digraph G {{
            rankdir=LR;  // Cambia la dirección del grafo de arriba a abajo
            {self.generar_dot_instrucciones()}
        }}
        """

        with open('instrucciones.dot', 'w') as f:
            f.write(dot_code)

        # comando 'dot' en el PATH
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

        # Ejecuta el comando dot para generar la imagen PNG
        os.system(f"dot -Tpng instrucciones.dot -o Instrucciones.png")