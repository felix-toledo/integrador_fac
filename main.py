import tkinter as tk
from tkinter import ttk

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
etiqueta1 = ttk.Label(pestaña1, text="Nueva Orden")
etiqueta1.pack(padx=10, pady=10)

etiqueta2 = ttk.Label(pestaña2, text="Contenido de la pestaña 2")
etiqueta2.pack(padx=10, pady=10)

etiqueta3 = ttk.Label(pestaña3, text="Contenido de la pestaña 3")
etiqueta3.pack(padx=10, pady=10)

# Agregar las pestañas al contenedor
pestanas.add(pestaña1, text="Orden")

# Empacar el contenedor de las pestañas
pestanas.pack(expand=True, fill="both")

# Ejecutar el bucle principal de la aplicación
main_window.mainloop()
