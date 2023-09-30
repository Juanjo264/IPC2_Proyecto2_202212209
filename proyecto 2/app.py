from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import tkinter.ttk as ttk

# Creación de la raíz
root = Tk()
# Título de la ventana
root.title("PROYECTO No. 2")
# Definir el tamaño de la ventana (cuadrada)
window_size = 800
root.geometry(f"{window_size}x{window_size}")
# Color de fondo
root.config(bg="lightblue")

# Etiqueta para el título
titulo_label = Label(root, text="PROYECTO No. 2 DRONES", font=("Helvetica", 18), bg="lightblue")
titulo_label.pack(pady=(20, 10))

# Estilo para los botones
boton_style = ttk.Style()
boton_style.configure("TButton", font=("Helvetica", 14), padding=10, width=20)

# Función para inicializar el sistema
def inicializar_sistema():
    # Agrega aquí la lógica para inicializar el sistema
    messagebox.showinfo("Inicialización", "El sistema se ha inicializado correctamente")

# Función para cargar un archivo XML de entrada
def cargar_archivo_entrada():
    file_path = askopenfilename(filetypes=[("XML files", "*.xml")])
    if file_path:
        # Agrega aquí la lógica para cargar el archivo XML
        messagebox.showinfo("Cargar Archivo de Entrada", "Archivo de entrada cargado con éxito")

# Función para generar un archivo XML de salida
def generar_archivo_salida():
    # Agrega aquí la lógica para generar el archivo XML de salida
    messagebox.showinfo("Generar Archivo de Salida", "Archivo de salida generado con éxito")

# Función para ver el listado de drones ordenado alfabéticamente
def ver_listado_drones():
    # Agrega aquí la lógica para mostrar el listado de drones
    messagebox.showinfo("Listado de Drones", "Lista de drones ordenada alfabéticamente")

# Función para agregar un nuevo dron
def agregar_dron():
    # Agrega aquí la lógica para agregar un nuevo dron
    messagebox.showinfo("Agregar Dron", "Nuevo dron agregado con éxito")

# Función para ver gráficamente el listado de sistemas de drones
def ver_listado_sistemas_drones():
    # Agrega aquí la lógica para mostrar gráficamente el listado de sistemas de drones
    messagebox.showinfo("Listado de Sistemas de Drones", "Listado de sistemas de drones gráficamente")

# Función para ver el listado de mensajes y sus instrucciones
def ver_listado_mensajes():
    # Agrega aquí la lógica para mostrar el listado de mensajes e instrucciones
    messagebox.showinfo("Listado de Mensajes", "Lista de mensajes y sus instrucciones")

# Función para ver instrucciones para enviar un mensaje
def ver_instrucciones_mensaje():
    # Agrega aquí la lógica para ver las instrucciones de envío de mensajes
    messagebox.showinfo("Instrucciones de Envío de Mensaje", "Instrucciones para enviar un mensaje")

# Función para mostrar la ayuda
def mostrar_ayuda():
    # Agrega aquí la información del estudiante y un enlace a la documentación del proyecto
    messagebox.showinfo("Ayuda", "Estudiante: Juan Jose Almengor Tizol \nEnlace a la documentación: ...")

# Botones
boton_inicializar = ttk.Button(root, text="Inicializar Sistema", command=inicializar_sistema)
boton_cargar_archivo_entrada = ttk.Button(root, text="Cargar Archivo de Entrada", command=cargar_archivo_entrada)
boton_generar_archivo_salida = ttk.Button(root, text="Generar Archivo de Salida", command=generar_archivo_salida)
boton_ver_listado_drones = ttk.Button(root, text="Ver Listado de Drones", command=ver_listado_drones)
boton_agregar_dron = ttk.Button(root, text="Agregar Nuevo Dron", command=agregar_dron)
boton_ver_listado_sistemas_drones = ttk.Button(root, text="Ver Listado de Sistemas de Drones", command=ver_listado_sistemas_drones)
boton_ver_listado_mensajes = ttk.Button(root, text="Ver Listado de Mensajes", command=ver_listado_mensajes)
boton_ver_instrucciones_mensaje = ttk.Button(root, text="Ver Instrucciones para Enviar Mensaje", command=ver_instrucciones_mensaje)
boton_mostrar_ayuda = ttk.Button(root, text="Ayuda", command=mostrar_ayuda)

# Colocación de los botones en la interfaz
boton_inicializar.pack(pady=10)
boton_cargar_archivo_entrada.pack(pady=10)
boton_generar_archivo_salida.pack(pady=10)
boton_ver_listado_drones.pack(pady=10)
boton_agregar_dron.pack(pady=10)
boton_ver_listado_sistemas_drones.pack(pady=10)
boton_ver_listado_mensajes.pack(pady=10)
boton_ver_instrucciones_mensaje.pack(pady=10)
boton_mostrar_ayuda.pack(pady=10)

# La última instrucción de la raíz ejecutará todo lo que está arriba de ella
root.mainloop()
