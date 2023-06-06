from objetos import Colchon;
import json;
import tkinter as tk;
from tkinter import ttk
from tkinter import messagebox

with open('./data/colchones.json') as json_file:
    data = json.load(json_file)

marca_entry = None
tipo_entry = None
posicion_entry = None
medida_entry = None

# Store the orders in a Python array
colchones = data;

def add_colchon():
    # Get the values from the input fields
    id = len(colchones)+1;
    marca = marca_entry.get()
    tipo = tipo_entry.get()
    posicion = posicion_entry.get()
    medida = medida_entry.get()
    
    colchones.append(Colchon(id, marca, tipo, posicion, medida))

    # Convertir el objeto "ordenes" a formato JSON
    colchones_json = json.dumps(colchones, default=lambda o: o.__dict__, indent=4)

    # Especificar la ruta del archivo JSON
    ruta_archivo = "./data/colchones.json"

    # Guardar el objeto "ordenes" en el archivo JSON
    with open(ruta_archivo, "w") as archivo:
        archivo.write(colchones_json)
    
    # Display the order details in a message box
    colchon_details = f"Marca: {marca}\nTipo: {tipo}\nPosicion: {posicion}\nMedida: {medida}"
    messagebox.showinfo("Colchon agregado", colchon_details)

def select_colchones():
    with open('./data/colchones.json') as json_file:
        colchones = json.load(json_file)
        
    selected_colchones = []

    def add_colchon():
        selected_colchones.append(tree.item(tree.focus())['values'])
        state_lavel.config(text="Agregado")

    def finish_selection():
        selector_colchones.destroy()
        

    selector_colchones = tk.Tk()
    selector_colchones.title("Elegir Colchones")
    selector_colchones.geometry("1250x500")
    selector_colchones.wm_iconbitmap('camion.ico')

    tree = ttk.Treeview(selector_colchones, columns=("ID","Marca", "Tipo", "Posición", "Medida"))
    tree.heading("ID", text="ID")
    tree.heading("Marca", text="Marca")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Posición", text="Posición")
    tree.heading("Medida", text="Medida")

    for i, colchon_data in enumerate(colchones):
        colchon = Colchon(colchon_data["id"], colchon_data["marca"], colchon_data["tipo"], colchon_data["posicion"], colchon_data["medida"])
        tree.insert("", "end", values=(colchon.id, colchon.marca, colchon.tipo, colchon.posicion, colchon.medida))


    tree.pack()

    add_button = ttk.Button(selector_colchones, text="Agregar colchón", command=add_colchon)
    add_button.pack()

    finish_button = ttk.Button(selector_colchones, text="Terminar selección", command=finish_selection)
    finish_button.pack()

    state_lavel = ttk.Label(selector_colchones, text="");
    state_lavel.pack()

    
    return selected_colchones;
    


def stock_colchones_window(window):
    global marca_entry, tipo_entry, posicion_entry, medida_entry

    # Create the form components
    titulo_label = tk.Label(window, text="ABM Colchones", font=("Arial", 16))
    titulo_label.pack()

    marca_label = tk.Label(window, text="Marca:")
    marca_label.pack()
    marca_entry = tk.Entry(window)
    marca_entry.pack()

    tipo_label = tk.Label(window, text="Tipo:")
    tipo_label.pack()
    tipo_entry = tk.Entry(window)
    tipo_entry.pack()

    posicion_label = tk.Label(window, text="Posicion:")
    posicion_label.pack()
    posicion_entry = tk.Entry(window)
    posicion_entry.pack()

    medida_label = tk.Label(window, text="Medida:")
    medida_label.pack()
    medida_entry = tk.Entry(window)
    medida_entry.pack()

    new_colchon_button = tk.Button(window, text="Agregar Colchon", command=add_colchon)
    new_colchon_button.pack()