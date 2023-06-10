from funciones.calculoDistancia import Empresa, calcular_ruta_mas_corta
import json
import tkinter as tk;
from objetos import Logistica
from objetos import Costo;
from objetos import Orden;


precioNaftaXLitro = 306.1;
gananciaXHora = 480;

with open('./data/vehiculos.json') as json_file:
    vehiculos = json.load(json_file)

with open('./data/logisticas.json') as json_file:
    logisticas = json.load(json_file)


def definir_empresa():
    # Crear una instancia de la clase Empresa
    empresa = Empresa()

    # Agregar centros de distribución
    empresa.agregar_centro('Puerto Tirol')
    empresa.agregar_centro('Corrientes')
    empresa.agregar_centro('Empedrado')
    empresa.agregar_centro('Perugorria')
    empresa.agregar_centro('Goya')
    empresa.agregar_centro('Esquina')
    
    # Agregar conexiones entre centros de distribución
    empresa.agregar_conexion('Puerto Tirol', 'Corrientes', 34.3, con_peaje=True) #PEAJE 700
    empresa.agregar_conexion('Corrientes', 'Empedrado', 60.8, con_peaje=True) #PEAJE 700
    empresa.agregar_conexion('Empedrado', 'Goya', 167)
    empresa.agregar_conexion('Empedrado', 'Perugorria', 174)
    empresa.agregar_conexion('Goya', 'Perugorria', 73.2)
    empresa.agregar_conexion('Perugorria', 'Esquina', 194)
    empresa.agregar_conexion('Goya', 'Esquina', 110.7)
    empresa.agregar_conexion('Esquina','Corrientes', 387, con_peaje=True)

    return(empresa);

# Llamar a la función calcular_ruta_mas_corta
def calculo_ruta(empresa, origen, destino):
    ruta, distancia, peaje = calcular_ruta_mas_corta(empresa, origen, destino)
    if ruta is not None:
        print("Ruta más corta:", ruta, "Distancia total:", distancia)
        return(ruta, distancia, peaje)
    else:
        print("No se encontró una ruta válida para los destinos especificados.")
        return ("No se encontró una ruta válida para los destinos especificados.", 0)

def buscar_vehiculo(vehiculo_a_buscar):
    vehiculo_encontrado = None
    for vehiculo in vehiculos:
        if vehiculo["id"] == vehiculo_a_buscar[0]:
            vehiculo_encontrado = vehiculo
            break
    return(vehiculo_encontrado)

def calculo_carga_descarga(destinos,vehiculo):

    def calculo_volumen(tipo):
        medida_colchon = None
        if tipo == "1 PLAZA":
            medida_colchon = 0.59
        elif tipo == "1.5 PLAZAS":
            medida_colchon = 0.72
        elif tipo == "2 PLAZAS":    
            medida_colchon = 0.9
        else:
            medida_colchon = 1;
        return medida_colchon;

    for i in range(len(destinos)):
        if destinos[i][1] =="":
            destinos[i][1] = "00%";
        if destinos[i][3] == "":
            destinos[i][3] = "00%";

        porcentaje_carga = float(destinos[i][1].strip("%")) / 100
        porcentaje_descarga = float(destinos[i][3].strip("%")) / 100
        volumen_colchones_carga = calculo_volumen(destinos[i][2]) #Recibe medidas en m3
        volumen_colchones_descarga = calculo_volumen(destinos[i][4])
        vehiculo['capacidadDeCarga']
        volumen_disponible_carga = int(vehiculo['capacidadDeCarga'] * porcentaje_carga);
        volumen_disponible_descarga = int(vehiculo['capacidadDeCarga'] * porcentaje_descarga);
        total_colchones_carga = volumen_disponible_carga / volumen_colchones_carga;
        total_colchones_descarga = volumen_disponible_descarga / volumen_colchones_descarga;

        destinos[i].append([total_colchones_carga, total_colchones_descarga])

    return destinos;

def generar_logistica(origen, destinos, colchones, vehiculo):
    empresa = definir_empresa();
    
    id = len(logisticas)+1;
    nombresDestino = []
    for sublist in destinos:
        nombresDestino.append(sublist[0])
    ruta, distancia, peajes = calculo_ruta(empresa, origen, nombresDestino);
    vehiculoUso = buscar_vehiculo(vehiculo[0]);
    destinos = calculo_carga_descarga(destinos,vehiculoUso);
    consumoTotal = (distancia * vehiculoUso["consumo"]) / 100;
    precioNafta = precioNaftaXLitro * consumoTotal;
    horasViaje = distancia / vehiculoUso["velocidadMedia"];
    viaticos = (horasViaje / 8) * 2000;
    descansos = int(horasViaje/12);
    if descansos > 1:
        horasViaje = horasViaje + (8*descansos)
    salario = gananciaXHora * horasViaje;
    
    costo = Costo(salario, precioNafta, peajes ,viaticos)
    

    logistica = Logistica(id, ruta, costo, horasViaje, vehiculoUso["capacidadDeCarga"], destinos,distancia)
    logisticas.append(logistica)

    # Convertir el objeto "ordenes" a formato JSON
    logisticas_json = json.dumps(logisticas, default=lambda o: o.__dict__, indent=4)

    # Especificar la ruta del archivo JSON
    ruta_archivo = "./data/logisticas.json"

    # Guardar el objeto "ordenes" en el archivo JSON
    with open(ruta_archivo, "w") as archivo:
        archivo.write(logisticas_json)
        
    return(logistica);



    
    
    
    
    


