from nodos.nodoContenido import nodoContenido


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
        while actual!= None:
            print(f"Dron: {actual.Contenido.dron}")
            actual.Contenido.listaAlturas.imprimir()
            actual=actual.siguiente
            print("---------------------------------------------------------")
    
    def get_listaAlturas(self,dron):
        actual = self.primero
        while actual!= None:
            if dron == actual.Contenido.dron:
                return actual.Contenido.listaAlturas
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
    
    def generar_dot(self):
        dot_code = """
        
            <tr>
                <td>Dron</td>
                
            
        """
        aux = self.primero
        while aux:
            dot_code += f"""
                    
                    <td>{aux.Contenido.dron}</td>
                    
            """
            aux = aux.siguiente
        dot_code += f"""
        </tr>
        """

        actual1 = self.primero
        dot_code += """<tr><td border="0"></td>"""
        while actual1:
            dot_code += """
        
            
            """   
            actual1 = actual1.siguiente
        dot_code += "</tr>"
        return dot_code