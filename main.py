import tkinter as tk
from tkinter import ttk
from funciones.nueva_orden import ventana_orden
from funciones.stock_colchones import stock_colchones_window

# Crear la ventana principal
main_window = tk.Tk()
main_window.title("EXUN S.A.")
main_window.geometry("500x500")
main_window.wm_iconbitmap('camion.ico')

# Crear el contenedor de las pestañas
pestanas = ttk.Notebook(main_window)

# Crear las pestañas
pestaña1 = ttk.Frame(pestanas)
pestaña2 = ttk.Frame(pestanas)
pestaña3 = ttk.Frame(pestanas)

# Agregar contenido a las pestañas
ventana_orden(pestaña1);
stock_colchones_window(pestaña2);

# Agregar las pestañas al contenedor
pestanas.add(pestaña1, text="Orden")
pestanas.add(pestaña2, text="ABM Colchones")

# Empacar el contenedor de las pestañas
pestanas.pack(expand=True, fill="both")

# Ejecutar el bucle principal de la aplicación
main_window.mainloop()
