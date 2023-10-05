from nodos.nodoMensajeSalida import nodoMensajeSalida
import xml.etree.ElementTree as ET

class listaMensajeSalida:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,Mensajesalida):
        if self.primero is None:
            self.primero=nodoMensajeSalida(Mensajesalida)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoMensajeSalida(Mensajesalida)
    
    def imprimir(self):
        actual=self.primero
        print("")
        print("MENSAJES NUEVOS")
        while actual!= None:
            print("_______________________________________________")
            print(f"Nombre Mensaje :{actual.Mensajesalida.nombreMensaje}, Sistema :{actual.Mensajesalida.sistema}, Mensaje: {actual.Mensajesalida.mensaje}, Tiempo Optimo :{actual.Mensajesalida.tiempoOptimo} ")
            print("_______________________________________________")
            actual=actual.siguiente
        print("===============================================================")
    
    def get_mensaje(self,nombre):
        actual = self.primero
        while actual != None:
            if actual.Mensajesalida.nombreMensaje == nombre:
                return actual.Mensajesalida
            actual = actual.siguiente
    
    def generar_xml(self , listamensajes):
        data = ET.Element('respuesta')
        lista = ET.SubElement(data, 'listaMensajes')

        for mensaje in listamensajes:
            mensaje_buscado = self.get_mensaje(mensaje.Mensajesalida.nombreMensaje)
            mensaje = ET.SubElement(lista, 'mensaje', nombre=f"{mensaje_buscado.nombreMensaje}")

            sistema = ET.SubElement(mensaje, 'sistemaDrones')
            sistema.text = mensaje_buscado.sistema

            tiempo_optimo = ET.SubElement(sistema, 'tiempoOptimo')
            tiempo_optimo.text = str(mensaje_buscado.tiempoOptimo)

            mensaje_recibido = ET.SubElement(sistema, 'mensajeRecibido')
            mensaje_recibido.text = mensaje_buscado.mensaje

        self.prettify_xml(data)
        tree = ET.ElementTree(data)
        tree.write("archivo_salida.xml",encoding="UTF-8",xml_declaration=True)
        
    def prettify_xml(self,element, indent='    '):
        queue = [(0, element)]  # (level, element)
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level+1) 
            if queue:
                element.tail = '\n' + indent * queue[0][0]  
            else:
                element.tail = '\n' + indent * (level-1)  
            queue[0:0] = children 
    
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
        
    def eliminar_datos(self):
        while self.primero:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual