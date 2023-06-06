from funciones.calculoDistancia import Empresa, calcular_ruta_mas_corta
import json

precioNaftaXLitro = 245;


with open('./data/vehiculos.json') as json_file:
    vehiculos = json.load(json_file)

def definir_empresa():
    # Crear una instancia de la clase Empresa
    empresa = Empresa()

    # Agregar centros de distribución
    empresa.agregar_centro('Resistencia')
    empresa.agregar_centro('Corrientes')
    empresa.agregar_centro('Empedrado')
    empresa.agregar_centro('Perugorria')
    empresa.agregar_centro('Goya')
    empresa.agregar_centro('Esquina')

    # Agregar conexiones entre centros de distribución
    empresa.agregar_conexion('Resistencia', 'Corrientes', 34.3)
    empresa.agregar_conexion('Corrientes', 'Empedrado', 60)
    empresa.agregar_conexion('Empedrado', 'Goya', 167)
    empresa.agregar_conexion('Empedrado', 'Perugorria', 175)
    empresa.agregar_conexion('Goya', 'Perugorria', 74.2)
    empresa.agregar_conexion('Perugorria', 'Esquina', 194)
    empresa.agregar_conexion('Goya', 'Esquina', 266)

    return(empresa);

# Llamar a la función calcular_ruta_mas_corta
def calculo_ruta(empresa, origen, destino):
    ruta, distancia = calcular_ruta_mas_corta(empresa, origen, destino)
    if ruta is not None:
        print("Ruta más corta:", ruta, "Distancia total:", distancia)
        return(ruta, distancia)
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


def generar_logistica(origen, destino, colchones, vehiculo):
    empresa = definir_empresa();
    print(origen)
    print(destino)

    ruta, distancia = calculo_ruta(empresa, origen, [destino]);
    vehiculoUso = buscar_vehiculo(vehiculo[0]);

    consumoTotal = (distancia * vehiculoUso["consumo"]) / 100;
    precioNafta = precioNaftaXLitro * consumoTotal;
    print(consumoTotal);
    print(precioNafta);
    print(ruta);

    
    


