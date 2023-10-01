import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog, messagebox
import tkinter.ttk as ttk
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
        messagebox.showinfo("Agregar Dron", "Nuevo dron agregado con éxito")

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
