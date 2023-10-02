from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from Leerxml import *
from Leerxml import leerxml

class ProyectoDronesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PROYECTO No. 2")
        self.window_size = 800
        self.root.geometry(f"{self.window_size}x{self.window_size}")
        self.root.config(bg="lightblue")
        self.readFile = leerxml()
        self.main_frame = tk.Frame(root,highlightbackground='gray', highlightthickness=1)
        self.main_frame.pack(side=tk.BOTTOM)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=100,width=400)
        self.nuevoDron = StringVar()


        self.titulo_label = tk.Label(root, text="PROYECTO No. 2 DRONES", font=("Helvetica", 18), bg="lightblue")
        self.titulo_label.pack(pady=(20, 10))

        self.boton_style = ttk.Style()
        self.boton_style.configure("TButton", font=("Helvetica", 14), padding=10, width=20)

        self.boton_inicializar = ttk.Button(root, text="Inicializar Sistema", command=self.inicializar_sistema)
        self.boton_cargar_archivo_entrada = ttk.Button(root, text="Cargar Archivo de Entrada", command=self.cargar_archivo_entrada)
        self.boton_generar_archivo_salida = ttk.Button(root, text="Generar Archivo de Salida", command=self.generar_archivo_salida)
        self.boton_ver_listado_drones = ttk.Button(root, text="Ver Listado de Drones", command=self.ver_listado_drones)
        self.boton_agregar_dron = ttk.Button(root, text="Agregar Nuevo Dron", command=self.agregar_dron)
        self.boton_ver_listado_sistemas_drones = ttk.Button(root, text="Ver Listado de Sistemas de Drones", command=self.ver_listado_sistemas_drones)
        self.boton_ver_listado_mensajes = ttk.Button(root, text="Ver Listado de Mensajes", command=self.ver_listado_mensajes)
        self.boton_ver_instrucciones_mensaje = ttk.Button(root, text="Ver Instrucciones para Enviar Mensaje", command=self.ver_instrucciones_mensaje)
        self.boton_mostrar_ayuda = ttk.Button(root, text="Ayuda", command=self.mostrar_ayuda)

        self.boton_inicializar.pack(pady=10)
        self.boton_cargar_archivo_entrada.pack(pady=10)
        self.boton_generar_archivo_salida.pack(pady=10)
        self.boton_ver_listado_drones.pack(pady=10)
        self.boton_agregar_dron.pack(pady=10)
        self.boton_ver_listado_sistemas_drones.pack(pady=10)
        self.boton_ver_listado_mensajes.pack(pady=10)
        self.boton_ver_instrucciones_mensaje.pack(pady=10)
        self.boton_mostrar_ayuda.pack(pady=10)

    def inicializar_sistema(self):
        messagebox.showinfo("Inicialización", "El sistema se ha inicializado correctamente")

    def clear_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

    def cargar_archivo_entrada(self):
        cargar_frame = tk.Frame(self.main_frame)
        lb = tk.Label(cargar_frame,text="CARGAR EL ARCHIVO XML",font=('Bold',20))
        lb.pack()
        cargar_frame.pack(pady=20)
        file_path = filedialog.askopenfilename(filetypes=[("Archivos", "*.xml")])
        self.file_path = file_path 
        if file_path:
            self.readFile.cargarXml(file_path)
            messagebox.showinfo("ARCHIVO CARGADO.","ARCHIVO CARGADO CON EXITO." )


    def generar_archivo_salida(self):
        messagebox.showinfo("Generar Archivo de Salida", "Archivo de salida generado con éxito")

    def ver_listado_drones(self):
        messagebox.showinfo("Listado de Drones", "Lista de drones ordenada alfabéticamente")


    def agregar_dron(self):
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
                    listado_drones = self.readFile.get_listaDrones()
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

    def crear_tabla_listaDrones(self, text_area):
        listado_drones = self.readFile.get_listaDrones()
        for i, dron in enumerate(listado_drones):
            numero_dron = i + 1
            texto_dron = f"{numero_dron}. {dron.Dron.nombre_dron}\n"
            text_area.insert(tk.END, texto_dron)



    def ver_listado_sistemas_drones(self):
        messagebox.showinfo("Listado de Sistemas de Drones", "Listado de sistemas de drones gráficamente")

    def ver_listado_mensajes(self):
        messagebox.showinfo("Listado de Mensajes", "Lista de mensajes y sus instrucciones")

    def ver_instrucciones_mensaje(self):
        messagebox.showinfo("Instrucciones de Envío de Mensaje", "Instrucciones para enviar un mensaje")

    def mostrar_ayuda(self):
        messagebox.showinfo("Ayuda", "Estudiante: Juan Jose Almengor Tizol \nEnlace a la documentación: ...")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProyectoDronesApp(root)
    root.mainloop()
