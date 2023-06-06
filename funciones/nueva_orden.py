#Esta función sirve para crear una nueva orden.
from objetos import Colchon;
from objetos import Orden;
import json;
import tkinter as tk;
from tkinter import ttk;
from tkinter import messagebox;
from funciones.stock_colchones import select_colchones;
from funciones.abm_vehiculos import select_vehiculos;
from funciones.logistica import generar_logistica;

# Defino los entrys de manera global, ya que si no, estarían guardados dentro de una función y sería dificil acceder a ellos.
fecha_entry = None 
origen_entry = None
destino_entry = None
colchones_entry = None 
logistica_entry = None
colchonesElegidos = None
vehiculoElegido = None

# Traigo el json de ordenes.
with open('./data/ordenes.json') as json_file:
    ordenes = json.load(json_file)
  
# Función para mandar una orden nueva.
def submit_order():
    # Traigo los valores de los inputs.
    id = len(ordenes) + 1
    fecha = fecha_entry.get()
    origen = origen_entry.get()
    destino = destino_entry.get()
    if colchonesElegidos == None: # Este if me va a obligar a seleccionar colchones en caso de que no lo haya hecho previamente.
        colchones = select_colchones();
    else:
        colchones = colchonesElegidos;
    vehiculo = vehiculoElegido;
    logistica = logistica_entry.get()

    # Llamo a la función generar logística que esta dentro del archivo logistica.py
    generar_logistica(origen, destino, colchones, vehiculo)
    ordenes.append(Orden(id, fecha, origen, destino, colchones, vehiculo, logistica))

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
        messagebox.showinfo("Ya elegiste un vehiculo", vehiculoElegido[0])

def ventana_orden(window):
    global fecha_entry,origen_entry, destino_entry, colchones_entry, logistica_entry

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

    destino_label = tk.Label(window, text="Destino/s:")
    destino_label.pack()
    destino_entry = tk.Entry(window)
    destino_entry.pack()

    colchones_label = tk.Label(window, text='Colchones: ')
    colchones_label.pack()
    lista_colchones = tk.Button(window, text="Colchones a distribuir", command=colchones_distribuir)
    lista_colchones.pack()
    add_colchon_button = tk.Button(window, text="Importar colchon", command=colchones_elegidos)
    add_colchon_button.pack()

    vehiculos_label = tk.Label(window, text="Vehículo:")
    vehiculos_label.pack()
    vehiculos_entry = tk.Entry(window)
    vehiculos_entry.pack()
    add_vehilcle_button = tk.Button(window, text="Importar Vehículo", command=vehiculo_elegido)
    add_vehilcle_button.pack()

    logistica_label = tk.Label(window, text="Logistica:")
    logistica_label.pack()
    logistica_entry = tk.Entry(window)
    logistica_entry.pack()

    new_order_button = tk.Button(window, text="New Order", command=submit_order)
    new_order_button.pack()