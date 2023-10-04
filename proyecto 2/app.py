from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from Leerxml import *
from Leerxml import leerxml
from listas.listaMensajeSalida import listaMensajeSalida
from MensajeSalida import MensajeSalida
import os
import webbrowser

class ProyectoDrones:
    def __init__(self, root):
        self.root = root
        self.root.title("PROYECTO No. 2")
        window_size = 800
        self.root.geometry(f"{window_size}x{window_size}")
        self.root.config(bg="lightblue")
        self.leerxml = leerxml()
        self.nuevoDron = StringVar()
        self.tiempoTemp = 0
        self.cadenaTiempo = ""
        self.existeTabla = False
        self.tablaTemp = ""
        self.create_widgets()
        self.main_frame = tk.Frame(root,highlightbackground='gray', highlightthickness=1)
        self.main_frame.pack(side=tk.BOTTOM)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=100,width=400)
        self.lista_mensajeCreado_temp = listaMensajeSalida()


    def create_widgets(self):
        self.titulo_label = ttk.Label(self.root, text="PROYECTO No. 2 DRONES", font=("Helvetica", 18), background="lightblue")
        self.titulo_label.pack(pady=(20, 10))

        boton_style = ttk.Style()
        boton_style.configure("TButton", font=("Helvetica", 14), padding=20, width=40)

        self.boton_inicializar = ttk.Button(self.root, text="Inicializar Sistema", command=self.inicializar_sistema)
        self.boton_cargar_archivo_entrada = ttk.Button(self.root, text="Cargar Archivo de Entrada", command=self.cargar_archivo_entrada)
        self.boton_generar_archivo_salida = ttk.Button(self.root, text="Generar Archivo de Salida", command=self.generar_archivo_salida)
        self.boton_gestionar_drones = ttk.Button(self.root, text="Gestión de Drones", command=self.gestionar_drones)
        self.boton_gestionar_sistemas_drones = ttk.Button(self.root, text="Gestión de Sistemas de Drones", command=self.gestionar_sistemas_drones)
        self.boton_gestionar_mensajes = ttk.Button(self.root, text="Gestión de Mensajes", command=self.Gestión_de_Mensajes)
        self.boton_mostrar_ayuda = ttk.Button(self.root, text="Ayuda", command=self.mostrar_ayuda)

        self.boton_inicializar.pack(pady=10)
        self.boton_cargar_archivo_entrada.pack(pady=10)
        self.boton_generar_archivo_salida.pack(pady=10)
        self.boton_gestionar_drones.pack(pady=10)
        self.boton_gestionar_sistemas_drones.pack(pady=10)
        self.boton_gestionar_mensajes.pack(pady=10)
        self.boton_mostrar_ayuda.pack(pady=10)

    def inicializar_sistema(self):
        self.leerxml.borrarListas()
        self.lista_mensajeCreado_temp = listaMensajeSalida()
        archivo_xml = "archivo_salida.xml"
        
        # Verifica si el archivo existe antes de eliminarlo
        if os.path.exists(archivo_xml):
            # Elimina el archivo existente
            os.remove(archivo_xml)
            messagebox.showinfo("Inicialización", "El sistema se ha inicializado correctamente y el archivo XML se ha eliminado.")
        else:
            messagebox.showinfo("Inicialización", "El sistema se ha inicializado correctamente, pero el archivo XML no existe.")

    def clear_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()    

    def cargar_archivo_entrada(self):
        self.clear_page()
        cargar_frame = tk.Frame(self.main_frame)
        lb = tk.Label(cargar_frame,text="Cargar Archivo",font=('Arial',20))
        lb.pack()
        cargar_frame.pack(pady=20)
        file_path = filedialog.askopenfilename(filetypes=[("Archivos", "*.xml")])
        self.file_path = file_path 
        if file_path:
            self.leerxml.cargarXml(file_path)
            messagebox.showinfo("ARCHIVO CARGADO.","ARCHIVO CARGADO CON EXITO." )

    def generar_archivo_salida(self):
        listado_mensajes = self.leerxml.get_listaMensajes()
        for mensaje in listado_mensajes:
            sistema = mensaje.Mensajes.sistema_drones
            nombreMensaje = mensaje.Mensajes.nombre_mensaje
            listaInstrucciones = listado_mensajes.encontrar_sistema(sistema)
            self.mostrar_instrucciones(listaInstrucciones, sistema, nombreMensaje)
        
        # Verifica si self.lista_mensajeCreado_temp no está vacía
        if self.lista_mensajeCreado_temp is not None and self.lista_mensajeCreado_temp.primero is not None:
            self.lista_mensajeCreado_temp.generar_xml(self.lista_mensajeCreado_temp)
            messagebox.showinfo("xml salida", "Se generó archivo xml")
        else:
            messagebox.showwarning("xml salida", "La lista de mensajes está vacía, no se generó archivo xml")

    def gestionar_drones(self):
        # Crear una nueva ventana para la gestión de drones
        gestion_drones_window = tk.Toplevel(self.root)
        gestion_drones_window.title("Gestión de Drones")

        def mostrar_lista_drones():
            # Crear una ventana para mostrar la lista de drones
            lista_drones_window = tk.Toplevel(gestion_drones_window)
            lista_drones_window.title("Listado de Drones")

            # Crear un área de texto para mostrar la lista de drones
            text_area = tk.Text(lista_drones_window, height=10, width=40)
            text_area.pack(padx=20, pady=10)

            # Llamar a la función para mostrar la lista de drones en el área de texto
            self.crear_tabla_listaDrones(text_area)

        def mostrar_agregar_dron():
            # Crear un cuadro de entrada de texto para el nombre del dron
            nombre_input = tk.Entry(gestion_drones_window)
            nombre_input.pack(pady=10)

            # Función para agregar un nuevo dron
            def agregar_dron():
                nombre_dron = nombre_input.get()
                if nombre_dron:
                    listado_drones = self.leerxml.get_listaDrones()
                    for dron in listado_drones:
                        if nombre_dron == dron.Dron.nombre_dron:
                            messagebox.showinfo("Error", "El dron ya se encuentra en la lista.")
                            return

                    dron_nuevo = Dron(nombre_dron)
                    listado_drones.insertar(dron_nuevo)
                    messagebox.showinfo("Agregar Dron", "Dron agregado exitosamente.")
                    nombre_input.delete(0, tk.END)  # Limpiar la entrada de texto
                    # Actualizar el área de texto en la ventana de lista de drones
                    mostrar_lista_drones()

            # Crear un botón "Agregar" para agregar el dron
            agregar_btn = tk.Button(gestion_drones_window, text="Agregar", command=agregar_dron)
            agregar_btn.pack(pady=10)

        # Crear un botón "Listado Drones" en la nueva ventana principal
        listado_drones_btn = ttk.Button(gestion_drones_window, text="Listado Drones", command=mostrar_lista_drones)
        listado_drones_btn.pack(pady=10)

        # Crear un botón "Agregar Dron" en la nueva ventana principal
        agregar_dron_btn = ttk.Button(gestion_drones_window, text="Agregar Dron", command=mostrar_agregar_dron)
        agregar_dron_btn.pack(pady=10)


    def ver_listado_drones(self):
        messagebox.showinfo("Listado de Drones", "Lista de drones ordenada alfabéticamente")

    def agregar_dron(self):
        messagebox.showinfo("Agregar Dron", "Nuevo dron agregado con éxito")

    def gestionar_sistemas_drones(self):
        self.leerxml.graficar()
        messagebox.showinfo("GRAFICA CREADA", "GRAFICA CREADA CON EXITO")


    def ver_listado_sistemas_drones(self):
        messagebox.showinfo("Listado de Sistemas de Drones", "Listado de sistemas de drones gráficamente")

    def Gestión_de_Mensajes(self):
        gestion_mensajes_window = tk.Toplevel(self.root)
        gestion_mensajes_window.geometry("900x450")  # Cambia las dimensiones 

        # Crear los botones en la ventana de gestión de mensajes
        listado_mensajes_btn = ttk.Button(gestion_mensajes_window, text="Listado Mensajes", command=self.crear_tabla_listaMensajes)
        listado_mensajes_btn.pack(pady=10)

        ver_instrucciones_btn = ttk.Button(gestion_mensajes_window, text="Ver instrucciones de mensajes", command=self.mostrar_tablaMensajes)
        ver_instrucciones_btn.pack(pady=10)

        grafica_instrucciones_btn = ttk.Button(gestion_mensajes_window, text="Gráfica instrucciones", command=self.grafica_intrucciones)
        grafica_instrucciones_btn.pack(pady=10)

    def crear_tabla_listaMensajes(self):
        self.clear_page()
        listaMensajes_frame = tk.Toplevel(self.main_frame)
        tvMensajes = ttk.Treeview(listaMensajes_frame,columns=("colMensajes"))
        tvMensajes.column("#0",width=200)
        tvMensajes.column("colMensajes",width=200,anchor=CENTER)
        
        tvMensajes.heading("#0",text="Nombre",anchor=CENTER)
        tvMensajes.heading("colMensajes", text="Sistema", anchor=CENTER)
        
        lb = tk.Label(listaMensajes_frame,text="Lista de mensajes",font=('Arial',20))
        listado_mensajes = self.leerxml.get_listaMensajes()
        
        for i, mensaje in enumerate(listado_mensajes):
            tvMensajes.insert("", "end", text=(mensaje.Mensajes.nombre_mensaje), values=(mensaje.Mensajes.sistema_drones))
        
        def item_selected(event):
            for selected_item in tvMensajes.selection():
                item = tvMensajes.item(selected_item)
                valuesList = item['values']
                if valuesList:
                    sistema = valuesList[0]
                    print(sistema)

                    listaImstrucciones = listado_mensajes.encontrar_sistema(sistema)
                    
                    self.crear_tabla_listaInstrucciones(listaImstrucciones)
                
        tvMensajes.bind('<<TreeviewSelect>>',item_selected)
        
        lb.pack()
        tvMensajes.pack()
        tvMensajes.pack(side="left") 

    def mostrar_tablaMensajes(self):
        self.clear_page()
        tablaMensajes_frame = tk.Toplevel(self.main_frame)
        tvMensajes = ttk.Treeview(tablaMensajes_frame,columns=("colMensajes"))
        tvMensajes.column("#0",width=200)
        tvMensajes.column("colMensajes",width=200,anchor=CENTER)
        
        tvMensajes.heading("#0",text="Nombre",anchor=CENTER)
        tvMensajes.heading("colMensajes", text="Sistema", anchor=CENTER)
        
        lb = tk.Label(tablaMensajes_frame,text="Lista de Mensajes",font=('Arial',20))
        listado_mensajes = self.leerxml.get_listaMensajes()
        
        for i, mensaje in enumerate(listado_mensajes):
            tvMensajes.insert("", "end", text=(mensaje.Mensajes.nombre_mensaje), values=(mensaje.Mensajes.sistema_drones))
        
        def item_selected(event):
            for selected_item in tvMensajes.selection():
                item = tvMensajes.item(selected_item)
                nombreMensaje = item['text']
                valuesList = item['values']
                if valuesList:
                    sistema = valuesList[0]
                    print(sistema)

                    listaImstrucciones = listado_mensajes.encontrar_sistema(sistema)
                    
                    self.mostrar_instrucciones(listaImstrucciones,sistema,nombreMensaje)
                
        tvMensajes.bind('<<TreeviewSelect>>',item_selected)
        lb.pack()
        tvMensajes.pack()
        tvMensajes.pack(side="left") 

    def crear_tabla_listaDrones(self, text_area):
        text_area.delete("1.0", tk.END)  # Limpiar el contenido actual del área de texto
        listado_drones = self.leerxml.get_listaDrones()
        for i, dron in enumerate(listado_drones):
            numero_dron = i + 1
            texto_dron = f"{numero_dron}. {dron.Dron.nombre_dron}\n"
            text_area.insert(tk.END, texto_dron)

    def grafica_intrucciones(self):
        self.leerxml.graficar_instrucciones()
        messagebox.showinfo("GRAFICA", "GRAFICA CREADA CON EXITO")

        messagebox.showinfo("GRAFICA CREADA CON EXITO")
    def crear_tabla_listaInstrucciones(self,listaInstrucciones):
        
        listaMensajes_frame = tk.Toplevel(self.main_frame)
        tvInstrucciones = ttk.Treeview(listaMensajes_frame,columns=("colInstrucciones"))
        self.tablaTemp = tvInstrucciones
        tvInstrucciones.column("#0",width=200)
        tvInstrucciones.column("colInstrucciones",width=200,anchor=CENTER)
        self.existeTabla = True
        tvInstrucciones.heading("#0",text="Dron",anchor=CENTER)
        tvInstrucciones.heading("colInstrucciones", text="AlturaDron", anchor=CENTER)
        
        lb = tk.Label(listaMensajes_frame,text="Lista de instrucciones",font=('Arial',20))
        for i, instruccion in enumerate(listaInstrucciones):
            tvInstrucciones.insert("", "end", text=(instruccion.Instrucciones.dron_actual), values=(instruccion.Instrucciones.posicion))
        
        
        lb.pack()
        tvInstrucciones.pack()
        tvInstrucciones.pack(side="left") 
        
    
    def mostrar_instrucciones(self, listaInstrucciones,sistema,nombreMensaje):
        self.tiempoTemp = 0
        tablaMensajes_frame = tk.Toplevel(self.main_frame)
        Vpasos = ttk.Treeview(tablaMensajes_frame, columns=( "Altura", "Mensaje", "Tiempo"))
        
        Vpasos.column("#0", width=90)
        Vpasos.column("Altura", width=90, anchor=tk.CENTER)
        Vpasos.column("Mensaje", width=90, anchor=tk.CENTER)
        Vpasos.column("Tiempo", width=90, anchor=tk.CENTER)
        
        Vpasos.heading("#0", text="Dron", anchor=tk.CENTER)
        Vpasos.heading("Altura", text="Altura", anchor=tk.CENTER)
        Vpasos.heading("Mensaje", text="Mensaje", anchor=tk.CENTER)
        Vpasos.heading("Tiempo", text="Tiempo", anchor=tk.CENTER)
        
        lb = tk.Label(tablaMensajes_frame, text="Instrucciones para los drones", font=('Arial', 16))
        listado_sistemasDrones = self.leerxml.get_listaSistemasDrones()
        listado_contenido = listado_sistemasDrones.encontrar_listaContenido(sistema)
        
        mensaje_completo = ""
        for instruccion in listaInstrucciones:
            dron_temp = instruccion.Instrucciones.dron_actual
            lista_alturas = listado_contenido.get_listaAlturas(dron_temp)
            altura_temp = instruccion.Instrucciones.posicion

            letra_temp = lista_alturas.encontrar_letra(altura_temp)
            mensaje_completo += letra_temp
            tiempoOptimo = self.calcular_tiempo(int(altura_temp),dron_temp)


            Vpasos.insert("", "end", text=instruccion.Instrucciones.dron_actual, values=(instruccion.Instrucciones.posicion, letra_temp, tiempoOptimo))
    
        self.lista_mensajeCreado_temp.insertar(MensajeSalida(nombreMensaje,sistema,mensaje_completo,tiempoOptimo))
        lbMensaje = tk.Label(tablaMensajes_frame, text="Mensaje decifrado: " + mensaje_completo, font=('Arial', 12))
        lbTiempoOptimo = tk.Label(tablaMensajes_frame, text="Mejor tiempo: " + str(tiempoOptimo), font=('Arial', 12))
        
        lb.pack()
        Vpasos.pack()
        Vpasos.pack(side="left")
        lbMensaje.pack()
        lbTiempoOptimo.pack()

    def calcular_tiempo(self, alturaTemp, dron_temp):
        if alturaTemp >= self.tiempoTemp:
            self.tiempoTemp = alturaTemp + 1
        elif alturaTemp <= self.tiempoTemp:
            self.tiempoTemp += 1
        elif str(self.tiempoTemp) in self.cadenaTiempo: 
            self.tiempoTemp += 1
        tiempo_original = self.tiempoTemp
        tiempoAsString = str(self.tiempoTemp)
        self.cadenaTiempo += tiempoAsString

        return self.tiempoTemp
    

    def ver_listado_mensajes(self):
        messagebox.showinfo("Listado de Mensajes", "Lista de mensajes y sus instrucciones")

    def ver_instrucciones_mensaje(self):
        messagebox.showinfo("Instrucciones de Envío de Mensaje", "Instrucciones para enviar un mensaje")

    def mostrar_ayuda(self):
        ensayo_url = 'https://www.google.com/search?client=opera&q=traduoctr&sourceid=opera&ie=UTF-8&oe=UTF-8'
        
        ayuda_window = tk.Toplevel(self.root)
        ayuda_window.title("Datos del estudiante")

        mensaje = (
            f"Estudiante: Juan Jose Almengor Tizol\n"
            f"carnet: 202212209\n"
            f"Curso: INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2\n"
            f"seccion: D\n"
        )

        mensaje_label = tk.Label(ayuda_window, text=mensaje)
        mensaje_label.pack(padx=10, pady=10)

        enlace_label = tk.Label(ayuda_window, text="Enlace al ensayo", cursor="hand2", fg="blue")
        enlace_label.pack(pady=(0, 10))
        enlace_label.bind("<Button-1>", lambda e: webbrowser.open(ensayo_url))

if __name__ == "__main__":
    root = tk.Tk()
    app = ProyectoDrones(root)
    root.mainloop()
