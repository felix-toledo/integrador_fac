# Este es uno de los archivos mas importantes ya que con este vamos a crear una nueva orden.

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
destinos_window = None
centros = None
carga_entry = []
descarga_entry = []
distribuir_entry = []
tipo_carga_entry = []
tipo_descarga_entry = []
destinos_seleccionados = [] 
empresa = definir_empresa()
centros = empresa.grafo.nodes

# Ventana que será llamada cuando creemos una orden. Esta va a mostrar todos los datos importantes de logística de la nueva orden.
def detalles_orden_window(orden):
    window = tk.Tk()
    window.title("EXUN S.A.")
    window.geometry("300x600")
    window.wm_iconbitmap('camion.ico')
    
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

    textoTiempo = 'Tiempo estimado: '+ str(orden.logistica.tiempo)
    textoTiempo_label = tk.Label(window, text=textoTiempo)
    textoTiempo_label.pack()

    textoDistancia = 'Distancia: '+ str(int(orden.logistica.distancia)) +"KM"
    textoDistancia_label = tk.Label(window, text=textoDistancia)
    textoDistancia_label.pack()

    textoVehiculo = 'Vehiculo: ' + str(orden.vehiculo[0][1])
    vehiculo_label = tk.Label(window, text=textoVehiculo)
    vehiculo_label.pack()

    table_label = tk.Label(window, text="DISTRIBUCIÓN", font=("Arial", 12))
    table_label.pack();
    tree = ttk.Treeview(window)
    tree["columns"] = ("Ciudad", "Cantidad a Descargar", "Tipo a Descargar", "Cantidad a Cargar", "Tipo a Cargar")

    tree.heading("Ciudad", text="Ciudad")
    tree.heading("Cantidad a Descargar", text="Cantidad a Descargar")
    tree.heading("Tipo a Descargar", text="Tipo a Descargar")
    tree.heading("Cantidad a Cargar", text="Cantidad a Cargar")
    tree.heading("Tipo a Cargar", text="Tipo a Cargar")
    
    for item in orden.logistica.destinos:
        ciudad = item[0]
        cantidad_descargar = int(item[5][1])
        tipo_descargar = item[4]
        cantidad_cargar = int(item[5][0])
        tipo_cargar = item[2]
        tree.insert("", "end", values=(ciudad, cantidad_descargar, tipo_descargar, cantidad_cargar, tipo_cargar))

    tree.pack()

    # Esta y todas las tablas (treeview) va a ser definidas.
    costoLabel = tk.Label(window, text="COSTOS", font=("Arial", 12))
    costoLabel.pack()
    treeCosto = ttk.Treeview(window)
    treeCosto["columns"] = ("Salario", "Combustible", "Peaje", "Viatico", "Total")
    treeCosto.config(height=1)

    # Define los encabezados de columna
    treeCosto.heading("Salario", text="Salario")
    treeCosto.heading("Combustible", text="Combustible")
    treeCosto.heading("Peaje", text="Peaje")
    treeCosto.heading("Viatico", text="Viatico")
    treeCosto.heading("Total", text="Total")

    # Obtiene los valores de los atributos del objeto Costo
    salario = int(orden.logistica.costo.salario)
    combustible = int(orden.logistica.costo.combustible)
    peaje = int(orden.logistica.costo.peaje)
    viatico = int(orden.logistica.costo.viatico)
    total = salario+combustible+peaje+viatico;

    # Agrega los datos a la tabla
    treeCosto.insert("", "end", values=(salario, combustible, peaje, viatico, total))
    
    # Empaquetar tabla en la ventana
    treeCosto.pack()

# Traigo el json de ordenes.
with open('./data/ordenes.json') as json_file:
    ordenes = json.load(json_file)
  
# Función para mandar una orden nueva.
def submit_order():
    # Traigo los valores de los inputs.
    id = len(ordenes) + 1
    fecha = fecha_entry.get()
    origen = origen_entry.get()
    destinos = destinos_seleccionados
    if colchonesElegidos == None: # Este if me va a obligar a seleccionar colchones en caso de que no lo haya hecho previamente.
        colchones = select_colchones();
    else:
        colchones = colchonesElegidos;
    vehiculo = vehiculoElegido;
    logistica = generar_logistica(origen, destinos, colchones, vehiculo)

    orden = Orden(id, fecha, origen, destinos, colchones, vehiculo, logistica)
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
    
# Esta funcion es llamada desde el boton de elegir colchones y llama a la funcion select_colchones que va a hacer la ventana especificada que explicamos más arriba.
def colchones_elegidos():
    global colchonesElegidos;
    colchonesElegidos = select_colchones();
    
# Ventana para ver los colchones que estamos por distribuir, en caso de no tener colchones elegidos, nos tira un aviso de que primero hay que importar.
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

# Ventana que es llamada cuando se apreta el boton de 
def vehiculo_elegido():
    global vehiculoElegido;
    if vehiculoElegido == None:
        vehiculoElegido = select_vehiculos();
    else:
        vehiculoElegido = select_vehiculos();

# Pone en el label el vehiculo elegido una vez que ya lo importamos
def vehiculo_ya_elegido():
    global vehiculo_elegido_label
    vehiculo_elegido_label.config(text=vehiculoElegido[0][1])

def guardar_destinos():
    global destinos_label;
    destinos_seleccionados.clear()  # Limpiar la lista antes de guardar los destinos
    centros = list(empresa.grafo.nodes)  # Obtener la lista de centros de distribución
    for i in range(len(centros)):
        if distribuir_entry[i].get() == "DISTRIBUIR":
            ciudad = centros[i]
            carga = carga_entry[i].get()
            descarga = descarga_entry[i].get()
            tipo_carga = tipo_carga_entry[i].get()
            tipo_descarga = tipo_descarga_entry[i].get()
            destinos_seleccionados.append([ciudad, carga, tipo_carga, descarga, tipo_descarga ])
    destinos_label.config(text=str(destinos_seleccionados))
    destinos_window.destroy()

def ventana_destinos():
    global destinos_window, empresa, destinos_vars;

    destinos_window = tk.Tk()
    destinos_vars = []  # Mover aquí la creación de las variables IntVar
    
    for i, centro in enumerate(centros):
        ciudad_label = tk.Label(destinos_window, text=f"{centro}", font=("Arial", 16))
        distribuir_label = tk.Label(destinos_window, text=f"Distribuir?")
        distribuye = ["DISTRIBUIR"]
        distribuir_entry.append(ttk.Combobox(destinos_window, values=distribuye))
        carga_label = tk.Label(destinos_window, text=f"Carga:")
        valores_porcentajes = ["05%","10%","15%","20%","25%","30%","35%","40%","45%","50%","55%","60%","65%","70%","75%","80%","85%","90%","95%","100%"]
        carga_entry.append(ttk.Combobox(destinos_window, values=valores_porcentajes))
        descarga_label = tk.Label(destinos_window, text=f"Descarga:")
        descarga_entry.append(ttk.Combobox(destinos_window, values=valores_porcentajes))
        tipo_carga_label = tk.Label(destinos_window, text='Tipo de colchones de carga: ')
        colchones_values = ['1 PLAZA', '1.5 PLAZAS', '2 PLAZAS']
        tipo_carga_entry.append(ttk.Combobox(destinos_window, values=colchones_values))
        tipo_descarga_label = tk.Label(destinos_window, text='Tipo de colchones de descarga: ')
        tipo_descarga_entry.append(ttk.Combobox(destinos_window, values=colchones_values))

        ciudad_label.grid(row=i, column=0, sticky=tk.W)
        distribuir_label.grid(row=i, column=1, sticky=tk.W)
        distribuir_entry[i].grid(row=i, column=2)
        carga_label.grid(row=i, column=3)
        carga_entry[i].grid(row=i, column=4)
        descarga_label.grid(row=i, column=5)
        descarga_entry[i].grid(row=i, column=6)
        descarga_label.grid(row=i, column=7)
        descarga_entry[i].grid(row=i, column=8)
        tipo_carga_label.grid(row=i, column=9)
        tipo_carga_entry[i].grid(row=i, column=10)
        tipo_descarga_label.grid(row=i, column=11)
        tipo_descarga_entry[i].grid(row=i, column=12)
    
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

    lista_colchones = tk.Button(window, text="Elegir destinos", command=ventana_destinos)
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

    new_order_button = tk.Button(window, text="Agregar Orden", command=submit_order)
    new_order_button.pack()

