from objetos import Colchon;
import json;
import tkinter as tk;
from tkinter import ttk
from tkinter import messagebox

# Traigo toda la data que esta en colchones.json y lo guardo en un array colchones.
with open('./data/colchones.json') as json_file:
    colchones = json.load(json_file)

# Variables globales
marca_entry = None
tipo_entry = None
posicion_entry = None

# Funcion que va a anadir un colchon (usando el objeto colchon) nuevo al array colchones y posteriormente, lo guarda en el json.
def add_colchon():
    id = len(colchones)+1;
    marca = marca_entry.get()
    tipo = tipo_entry.get()
    posicion = posicion_entry.get()
    
    colchones.append(Colchon(id, marca, tipo, posicion))
    # Convertir el objeto "colchones" a formato JSON
    colchones_json = json.dumps(colchones, default=lambda o: o.__dict__, indent=4)

    # Especificar la ruta del archivo JSON
    ruta_archivo = "./data/colchones.json"

    # Guardar el objeto "colchones" en el archivo JSON
    with open(ruta_archivo, "w") as archivo:
        archivo.write(colchones_json)
    
    # Muestra que se creo el colchon satisfactoriamente con un messagebox.
    colchon_details = f"Marca: {marca}\nTipo: {tipo}\nPosicion: {posicion}"
    messagebox.showinfo("Colchon agregado", colchon_details)

# Ventana que voy a llamar cuando este crando una nueva orden, voy a poder ver la lista de todos los colchones para poder seleccionar.
# Esta ventana, retorna los colchones seleccionados.
def select_colchones():
    with open('./data/colchones.json') as json_file:
        colchones = json.load(json_file)
        
    # Creo el array selected_colchones que va a ir guardando los colchones seleccionados
    selected_colchones = []

    # Agrega el colchon seleccionado de la lista a selected_colchones.
    def add_colchon():
        selected_colchones.append(tree.item(tree.focus())['values'])
        state_lavel.config(text="Agregado")

    def finish_selection():
        selector_colchones.destroy()
        
    # Creo la nueva ventana con una tabla adentro.
    selector_colchones = tk.Tk()
    selector_colchones.title("Elegir Colchones")
    selector_colchones.geometry("1250x500")
    selector_colchones.wm_iconbitmap('camion.ico')

    tree = ttk.Treeview(selector_colchones, columns=("ID","Marca", "Tipo", "Posición"))
    tree.heading("ID", text="ID")
    tree.heading("Marca", text="Marca")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Posición", text="Posición")

    # Muestro todos los colchones existentes en la tabla.
    for i, colchon_data in enumerate(colchones):
        colchon = Colchon(colchon_data["id"], colchon_data["marca"], colchon_data["tipo"], colchon_data["posicion"])
        tree.insert("", "end", values=(colchon.id, colchon.marca, colchon.tipo, colchon.posicion))

    tree.pack()

    add_button = ttk.Button(selector_colchones, text="Agregar colchón", command=add_colchon)
    add_button.pack()

    finish_button = ttk.Button(selector_colchones, text="Terminar selección", command=finish_selection)
    finish_button.pack()

    state_lavel = ttk.Label(selector_colchones, text="");
    state_lavel.pack()
    
    return selected_colchones;
    
# Esta es la sección que existe para dar de alta un colchon nuevo. Completamos el formulario y damos click en agregar colchon.
def stock_colchones_window(window):
    global marca_entry, tipo_entry, posicion_entry

    titulo_label = tk.Label(window, text="ABM Colchones", font=("Arial", 16))
    titulo_label.pack()

    marca_label = tk.Label(window, text="Marca: ")
    marca_label.pack()
    marca_entry = tk.Entry(window)
    marca_entry.pack()

    tipo_label = tk.Label(window, text='Tipo: ')
    tipo_label.pack()
    tipo_values = ['1 PLAZA', '1.5 PLAZAS', '2 PLAZAS']
    tipo_entry = ttk.Combobox(window, values=tipo_values)
    tipo_entry.pack()

    posicion_label = tk.Label(window, text="Posicion:")
    posicion_label.pack()
    posicion_entry = tk.Entry(window)
    posicion_entry.pack()

    new_colchon_button = tk.Button(window, text="Agregar Colchon", command=add_colchon)
    new_colchon_button.pack()