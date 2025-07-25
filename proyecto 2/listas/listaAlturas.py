from nodos.nodoAlturas import nodoAlturas
from Alturas import Alturas

class listaAlturas:
    def __init__(self):
        self.Count = 0
        self.status = ""
        self.primero = None
        self.ultimo = None
        
    def insertar(self,Alturas):
        self.Count +=  1
        self.status = self.status + "Altura: " + Alturas.altura + "Letra: " + Alturas.letra +"\n"
        if self.primero is None:

            self.primero=nodoAlturas(Alturas)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoAlturas(Alturas)

    def insertar_alturas(self, Alturas):
        nuevo_nodo = nodoAlturas(Alturas)
        if self.Count == 0:

            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            actual = self.primero
            anterior = None
            while actual is not None and (int(actual.Alturas.altura) < int(nuevo_nodo.Alturas.altura) or (int(actual.Alturas.altura) == int(nuevo_nodo.Alturas.altura) and int(actual.Alturas.contador) < int(nuevo_nodo.Alturas.contador))):
                anterior = actual
                actual = actual.siguiente
            if anterior is None:

                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                nuevo_nodo.siguiente = actual
                anterior.siguiente = nuevo_nodo
        self.Count += 1

    def imprimir(self):
        print("")
        actual=self.primero
        while actual!= None:
            print(f"Altura: {actual.Alturas.altura}, Letra: {actual.Alturas.letra}")

            actual=actual.siguiente
    
    def encontrar_letra(self,valor):
        actual = self.primero
        while actual!= None:
            if valor == actual.Alturas.altura:

                return actual.Alturas.letra
            
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


        dot_code = f"""<tr><td border="0"></td>"""
        actual =self.primero
        sentinela_de_filas=actual.Alturas.altura 
        fila_iniciada=False
        while actual != None:
            if int(sentinela_de_filas)!=int(actual.Alturas.altura) :

                dot_code += f"""</tr><tr><td border="0"></td>"""
                sentinela_de_filas=actual.Alturas.altura 
                fila_iniciada=False 
            if fila_iniciada==False:

                fila_iniciada=True
                dot_code+="""<td>"""+str(actual.Alturas.letra)+"""</td>\n"""
            else:
                dot_code+="""<td>"""+str(actual.Alturas.letra)+"""</td>\n"""
            actual = actual.siguiente

        dot_code += f"""</tr>"""


        return dot_code       