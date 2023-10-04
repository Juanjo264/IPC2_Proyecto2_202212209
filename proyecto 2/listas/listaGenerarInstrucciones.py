from nodos.nodoGenerarInstrucciones import nodoGenerarInstrucciones
import os

class listaGenerarInstrucciones:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,Instrucciones):
        if self.primero is None:
            self.primero=nodoGenerarInstrucciones(Instrucciones)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoGenerarInstrucciones(Instrucciones)

    def imprimir(self):
        actual=self.primero
        print("------------------Lista Instrucciones----------")
        while actual!= None:
            print(f"nombre: {actual.Instrucciones.nombremensjae}")
            print(f"Dron: {actual.Instrucciones.dron_actual}, Posicion: {actual.Instrucciones.posicion}")
            actual=actual.siguiente
        print("------------------------------------------------------")
    
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
        dot_code = "node [shape=box];\n"
        aux = self.primero
        previous_message_name = None  # Nombre del mensaje anterior

        while aux:
            # Comprobar si el nombre del mensaje ha cambiado
            if aux.Instrucciones.nombremensjae != previous_message_name:
                # Cerrar el subgrafo del mensaje anterior (si existe)
                if previous_message_name:
                    dot_code += "}\n"

                # Iniciar un nuevo subgrafo (cluster) para el mensaje actual
                dot_code += f'subgraph cluster_{id(aux)}' + "{\n"
                dot_code += f'label="{aux.Instrucciones.nombremensjae}";\n'
                previous_message_name = aux.Instrucciones.nombremensjae

            # Crear un cuadrito con estilo 'filled' y color verde según la altura de subida
            altura_subida = int(aux.Instrucciones.posicion)
            dron_actual = aux.Instrucciones.dron_actual  # Obtener el nombre del dron
            nivel = int(aux.Instrucciones.posicion)  # Obtener el nivel si está disponible en tu estructura

            # Agregar el nombre del dron y, si es posible, el nivel
            label = f'Dron: {dron_actual}, Posicion: {aux.Instrucciones.posicion}'
            if nivel is not None:
                label += f', Nivel: {nivel}'

            if altura_subida > 0:
                dot_code += f'"{id(aux)}" [label="{label}", shape=box, style=filled, fillcolor=green];\n'
                for _ in range(altura_subida - 1):
                    dot_code += f'"{id(aux)}_{_}" [label="", shape=box];\n'
            else:
                dot_code += f'"{id(aux)}" [label="{label}", shape=box];\n'

            aux = aux.siguiente

        # Cerrar el último subgrafo (cluster) si existe
        if previous_message_name:
            dot_code += "}\n"

        return dot_code

    def recorrer_grafica_instrucciones(self):
        dot_code = f"""
        digraph G {{
            rankdir=LR;
            {self.generar_dot_instrucciones()}
        }}
        """

        with open('instrucciones.dot', 'w') as f:
            f.write(dot_code)

        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f"dot -Tpng instrucciones.dot -o Instrucciones.png")
