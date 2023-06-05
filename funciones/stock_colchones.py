from objetos import Colchon;
import json;
import tkinter as tk;
from tkinter import ttk
from tkinter import messagebox

with open('./data/colchones.json') as json_file:
    data = json.load(json_file)

# Store the orders in a Python array
colchones = data;

def add_colchon():
    # Get the values from the input fields
    marca = marca_entry.get()
    tipo = tipo_entry.get()
    posicion = posicion_entry.get()
    medida = medida_entry.get()
    
    colchones.append(Colchon(marca, tipo, posicion, medida))

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

# Create the main window
window = tk.Tk()
window.title("Order Management")

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

# Start the main event loop
window.mainloop()