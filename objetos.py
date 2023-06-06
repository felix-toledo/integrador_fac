class Colchon:
    def __init__(self,id, marca, tipo, posicion, medida):
        self.id = id
        self.marca = marca
        self.tipo = tipo
        self.posicion = posicion
        self.medida = medida
        
class Vehiculo:
    def __init__(self,id, unidad, marca, modelo, capacidadDeCarga, consumo):
        self.id = id
        self.unidad = unidad
        self.marca = marca
        self.modelo = modelo
        self.capacidadDeCarga = capacidadDeCarga
        self.consumo = consumo
        
class Costo:
    def __init__(self,ID_Costo, salario, combustible):
        self.ID_Costo = ID_Costo
        self.salario = salario
        self.combustible = combustible

class Logistica:
    def __init__(self,ID_Logistica, distribucion, costo, tiempo, capacidad):
        self.ID_Logistica = ID_Logistica
        self.distribucion = distribucion
        self.costo = costo
        self.tiempo = tiempo
        self.capacidad = capacidad

class Orden:
    def __init__(self,ID_Orden, fecha, origen, destino, colchones, vehiculo, logistica):
        self.ID_Orden = ID_Orden
        self.fecha = fecha
        self.origen = origen
        self.destino = destino
        self.colchones = colchones
        self.vehiculo = vehiculo
        self.logistica = logistica