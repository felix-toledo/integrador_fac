#Acá va a estar todo el código principal, este es el archivo que hay que ejecutar para iniciar el programa.

import tkinter as tk
from tkinter import ttk
from funciones.nueva_orden import ventana_orden
from funciones.stock_colchones import stock_colchones_window
from funciones.abm_vehiculos import abm_vehiculos_window
from tkinter import messagebox

import json
import os

# Defino variables globales que voy a utilizar en el window, posteriormente llamare a los valores que contienen estas variables.
root = None
username_entry = None 
password_entry = None

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Verificar las credenciales con check_credentials si esta bien entra al sistema, si no.. Error.
    if check_credentials(username, password):
        root.destroy() 
        ventana_principal() 
    else:
        messagebox.showerror("Error", "Credenciales inválidas")

# Funcion que retorna t o f dependiendo de si username y password se encuentra en users.json o no.
def check_credentials(username, password):
    if not os.path.exists("./data/users.json"):
        return False

    with open('./data/users.json') as json_file:
        users = json.load(json_file)

    return username in users and users[username] == password

# Creo la interfaz de inicio sesion.
def sesion_window():
    global username_entry, password_entry, root
    
    root = tk.Tk()
    root.title("Inicio de sesión")
    root.iconbitmap('camion.ico')
    root.geometry("500x500")
    # Etiqueta y campo de entrada para el nombre de usuario
    username_label = tk.Label(root, text="Nombre de usuario:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    # Etiqueta y campo de entrada para la contraseña
    password_label = tk.Label(root, text="Contraseña:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # Botón de inicio de sesión
    login_button = tk.Button(root, text="Iniciar sesión", command=login)
    login_button.pack()

    root.mainloop()

# Creo la ventana principal
def ventana_principal():
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

    # Agregar contenido a las pestañas, llamando a las funciones que estan dentro de la carpeta /funciones.
    ventana_orden(pestaña1);
    stock_colchones_window(pestaña2);
    abm_vehiculos_window(pestaña3);


    # Agregar las pestañas al contenedor
    pestanas.add(pestaña1, text="Orden")
    pestanas.add(pestaña2, text="ABM Colchones")
    pestanas.add(pestaña3, text="ABM Vehiculos")

    # Empacar el contenedor de las pestañas
    pestanas.pack(expand=True, fill="both")

    # Ejecutar el bucle principal de la aplicación
    main_window.mainloop()

# Llamo a sesion window, va a ser la funcion que INICIA EL SISTEMA
sesion_window();
