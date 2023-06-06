from objetos import Vehiculo;
import json;
import tkinter as tk;
from tkinter import ttk
from tkinter import messagebox

with open('./data/vehiculos.json') as json_file:
    data = json.load(json_file)

unidad_entry = None
marca_entry = None
modelo_entry = None
cdg_entry = None

# Store the orders in a Python array
vehiculos = data;

def add_colchon():
    # Get the values from the input fields
    id = len(vehiculos)+1;
    marca = marca_entry.get()
    unidad = unidad_entry.get()
    modelo = modelo_entry.get()
    cdg = cdg_entry.get()
    
    vehiculos.append(Vehiculo(id, unidad, marca, modelo, cdg))

    # Convertir el objeto "ordenes" a formato JSON
    vehiculos_json = json.dumps(vehiculos, default=lambda o: o.__dict__, indent=4)

    # Especificar la ruta del archivo JSON
    ruta_archivo = "./data/vehiculos.json"

    # Guardar el objeto "ordenes" en el archivo JSON
    with open(ruta_archivo, "w") as archivo:
        archivo.write(vehiculos_json)
    
    # Display the order details in a message box
    vehiculos_details = f"Unidad: {unidad}\nMarca: {marca}\Modelo: {modelo}\nCapacidad de carga: {cdg}"
    messagebox.showinfo("Vehiculo agregado", vehiculos_details)


def abm_vehiculos_window(window):
    global unidad_entry, marca_entry, modelo_entry, cdg_entry

    # Create the form components
    titulo_label = tk.Label(window, text="ABM Vehiculos", font=("Arial", 16))
    titulo_label.pack()

    unidad_label = tk.Label(window, text="Marca:")
    unidad_label.pack()
    unidad_entry = tk.Entry(window)
    unidad_entry.pack()

    marca_label = tk.Label(window, text="Marca:")
    marca_label.pack()
    marca_entry = tk.Entry(window)
    marca_entry.pack()

    modelo_label = tk.Label(window, text="Modelo:")
    modelo_label.pack()
    modelo_entry = tk.Entry(window)
    modelo_entry.pack()

    cdg_label = tk.Label(window, text="Capacidad de carga:")
    cdg_label.pack()
    cdg_entry = tk.Entry(window)
    cdg_entry.pack()

    new_colchon_button = tk.Button(window, text="Agregar Vehiculo", command=add_colchon)
    new_colchon_button.pack()