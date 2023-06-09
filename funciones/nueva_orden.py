#Esta función sirve para crear una nueva orden.
from objetos import Colchon;
from objetos import Orden;
import json;
import tkinter as tk;
from tkinter import ttk;
from tkinter import messagebox;
from funciones.stock_colchones import select_colchones;
from funciones.abm_vehiculos import select_vehiculos;
from funciones.logistica import generar_logistica, definir_empresa;


# Defino los entrys de manera global, ya que si no, estarían guardados dentro de una función y sería dificil acceder a ellos.
fecha_entry = None 
origen_entry = None
destino_entry = None
colchones_entry = None 
logistica_entry = None
colchonesElegidos = None
vehiculoElegido = None
vehiculo_elegido_label = None
destinos_label = None

def detalles_orden_window(orden):

    window = tk.Tk()
    window.title("EXUN S.A.")
    window.geometry("300x600")
    window.wm_iconbitmap('camion.ico')
    
    # Creo el form en la UI
    text = "Orden número: " +str(orden.id)
    titulo_label = tk.Label(window, text=text, font=("Arial", 10))
    titulo_label.pack()

    textoFecha = 'Fecha: '+ str(orden.fecha)
    fecha_label = tk.Label(window, text=textoFecha)
    fecha_label.pack()

    textoOrigen = 'Origen: '+ str(orden.origen)
    origen_label = tk.Label(window, text=textoOrigen)
    origen_label.pack()

    textoRuta = 'Ruta recomendada: '+ str(orden.logistica.distribucion)
    ruta_label = tk.Label(window, text=textoRuta)
    ruta_label.pack()



'''
    new_order_button = tk.Button(window, text="New Order", command=submit_order)
    new_order_button.pack()
'''

# Traigo el json de ordenes.
with open('./data/ordenes.json') as json_file:
    ordenes = json.load(json_file)
  
# Función para mandar una orden nueva.
def submit_order():
    # Traigo los valores de los inputs.
    id = len(ordenes) + 1
    fecha = fecha_entry.get()
    origen = origen_entry.get()
    destino = destinos_seleccionados
    if colchonesElegidos == None: # Este if me va a obligar a seleccionar colchones en caso de que no lo haya hecho previamente.
        colchones = select_colchones();
    else:
        colchones = colchonesElegidos;
    vehiculo = vehiculoElegido;
    logistica = generar_logistica(origen, destino, colchones, vehiculo)

    orden = Orden(id, fecha, origen, destino, colchones, vehiculo, logistica)
    # Llamo a la función generar logística que esta dentro del archivo logistica.py
    detalles_orden_window(orden);
    ordenes.append(orden)

    # Convertir el objeto "ordenes" a formato JSON
    ordenes_json = json.dumps(ordenes, default=lambda o: o.__dict__, indent=4)

    # Especificar la ruta del archivo JSON
    ruta_archivo = "./data/ordenes.json"

    # Guardar el objeto "ordenes" en el archivo JSON
    with open(ruta_archivo, "w") as archivo:
        archivo.write(ordenes_json)
    
    # Display the order details in a message box
    order_details = f"Fecha: {fecha}\nOrigen: {origen}\nDestino/s: {destino}\nColchones: {colchones}\nLogistica: {logistica}"
    messagebox.showinfo("Order Details", order_details)

def colchones_elegidos():
    global colchonesElegidos;
    colchonesElegidos = select_colchones();
    
def colchones_distribuir():
    if colchonesElegidos == None:
        messagebox.showinfo("NO HAY COLCHONES", 'Primero necesitas importar colchones')
    else: 
        window_colchones = tk.Tk();
        window_colchones.title("Colchones a distribuir")
        window_colchones.geometry("1250x500")
        window_colchones.wm_iconbitmap('camion.ico')

        tree = ttk.Treeview(window_colchones, columns=("ID","Marca", "Tipo", "Posición"))
        tree.heading("ID", text="ID")
        tree.heading("Marca", text="Marca")
        tree.heading("Tipo", text="Tipo")
        tree.heading("Posición", text="Posición")

        for i, colchon_data in enumerate(colchonesElegidos):
            colchon = Colchon(colchon_data[0], colchon_data[1], colchon_data[2], colchon_data[3])
            tree.insert("", "end", values=(colchon.id, colchon.marca, colchon.tipo, colchon.posicion))

        tree.pack()
    
def vehiculo_elegido():
    global vehiculoElegido;
    if vehiculoElegido == None:
        vehiculoElegido = select_vehiculos();
    else:
        vehiculoElegido = select_vehiculos();

def vehiculo_ya_elegido():
    global vehiculo_elegido_label
    vehiculo_elegido_label.config(text=vehiculoElegido[0][1])

destinos_window = None
centros = None
carga_entry = []
descarga_entry = []
sino_entry = []
destinos_seleccionados = []  # Variable global para almacenar los destinos seleccionados
empresa = definir_empresa()
centros = empresa.grafo.nodes

def guardar_destinos():
    global destinos_label;
    destinos_seleccionados.clear()  # Limpiar la lista antes de guardar los destinos
    centros = list(empresa.grafo.nodes)  # Obtener la lista de centros de distribución
    for i in range(len(centros)):
        if sino_entry[i].get() == "1":
            ciudad = centros[i]
            carga = carga_entry[i].get()
            descarga = descarga_entry[i].get()
            destinos_seleccionados.append([ciudad, carga, descarga])
        else:
            print('no entro')
    destinos_label.config(text=str(destinos_seleccionados))
    destinos_window.destroy()

def acceder_destinos():
    ventana_destinos()

def ventana_destinos():
    global destinos_window, empresa, destinos_vars;

    destinos_window = tk.Tk()
    print(centros)
    destinos_vars = []  # Mover aquí la creación de las variables IntVar
    
    for i, centro in enumerate(centros):
        sino_label = tk.Label(destinos_window, text=f"1. Si, 2.No:")
        sino_entry.append(tk.Entry(destinos_window))
        carga_label = tk.Label(destinos_window, text=f"Carga {centro}:")
        carga_entry.append(tk.Entry(destinos_window))
        descarga_label = tk.Label(destinos_window, text=f"Descarga {centro}:")
        descarga_entry.append(tk.Entry(destinos_window))
        
        sino_label.grid(row=i, column=0, sticky=tk.W)
        sino_entry[i].grid(row=i, column=1)
        carga_label.grid(row=i, column=2)
        carga_entry[i].grid(row=i, column=3)
        descarga_label.grid(row=i, column=4)
        descarga_entry[i].grid(row=i, column=5)
    
    guardar_button = tk.Button(destinos_window, text="Guardar", command=guardar_destinos)
    guardar_button.grid(row=len(centros), column=0, columnspan=5)
    
    destinos_window.mainloop()


def ventana_orden(window):
    global fecha_entry, origen_entry, destino_entry, colchones_entry, logistica_entry, vehiculo_elegido_label, empresa, destinos_label

    # Creo el form en la UI
    titulo_label = tk.Label(window, text="Generar nueva orden", font=("Arial", 16))
    titulo_label.pack()

    fecha_label = tk.Label(window, text="Fecha:")
    fecha_label.pack()
    fecha_entry = tk.Entry(window)
    fecha_entry.pack()

    origen_label = tk.Label(window, text="Origen:")
    origen_label.pack()
    origen_entry = tk.Entry(window)
    origen_entry.pack()

    lista_colchones = tk.Button(window, text="Elegir destinos", command=acceder_destinos)
    lista_colchones.pack()
    destinos_label = tk.Label(window, text='Vas a ver los destinos aquí!')
    destinos_label.pack()

    colchones_label = tk.Label(window, text='Colchones: ')
    colchones_label.pack()
    lista_colchones = tk.Button(window, text="Colchones a distribuir", command=colchones_distribuir)
    lista_colchones.pack()
    add_colchon_button = tk.Button(window, text="Importar colchon", command=colchones_elegidos)
    add_colchon_button.pack()

    vehiculos_label = tk.Label(window, text="Vehículo:")
    vehiculos_label.pack()
    vehiculo_elegido_label = tk.Label(window, text="")
    vehiculo_elegido_label.pack()
    add_vehilcle_button = tk.Button(window, text="Importar Vehículo", command=vehiculo_elegido)
    add_vehilcle_button.pack()

    new_order_button = tk.Button(window, text="New Order", command=submit_order)
    new_order_button.pack()

