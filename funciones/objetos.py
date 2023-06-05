class Colchon:
    def __init__(self, marca, tipo, posicion, medida):
        self.marca = marca
        self.tipo = tipo
        self.posicion = posicion
        self.medida = medida
        
class Vehiculos:
    def __init__(self, unidad, marca, modelo, capacidadDeCarga):
        self.unidad = unidad
        self.marca = marca
        self.modelo = modelo
        self.capacidadDeCarga = capacidadDeCarga
        
class Costo:
    def __init__(self, salario, combustible):
        self.salario = salario
        self.combustible = combustible

class Logistica:
    def __init__(self, distribucion, costo, tiempo, capacidad):
        self.distribucion = distribucion
        self.costo = costo
        self.tiempo = tiempo
        self.capacidad = capacidad

class Orden:
    def __init__(self, fecha, origen, destino, colchones, logistica):
        self.fecha = fecha
        self.origen = origen
        self.destino = destino
        self.colchones = colchones
        self.logistica = logistica