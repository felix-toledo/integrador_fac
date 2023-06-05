from objetos import Orden, Colchon, Logistica;
import json;
import tkinter as tk;
from tkinter import ttk;
from tkinter import messagebox;

with open('./data/ordenes.json') as json_file:
    ordenes = json.load(json_file)
    
with open('./data/colchones.json') as json_file:
    colchones = json.load(json_file)

def submit_order():
    # Get the values from the input fields
    fecha = fecha_entry.get()
    origen = origen_entry.get()
    destino = destino_entry.get()
    colchones = colchones_entry.get()
    logistica = logistica_entry.get()
    
    ordenes.append(Orden(fecha, origen, destino, colchones, logistica))

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

# Create the main window
window = tk.Tk()
window.title("Order Management")

# Create the form components
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

colchones_label = tk.Label(window, text="Colchones:")
colchones_label.pack()
colchones_entry = tk.Entry(window)
colchones_entry.pack()

logistica_label = tk.Label(window, text="Logistica:")
logistica_label.pack()
logistica_entry = tk.Entry(window)
logistica_entry.pack()

new_order_button = tk.Button(window, text="New Order", command=submit_order)
new_order_button.pack()

# Start the main event loop
window.mainloop()

