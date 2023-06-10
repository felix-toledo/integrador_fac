class Colchon:
    def __init__(self,id, marca, tipo, posicion):
        self.id = id
        self.marca = marca
        self.tipo = tipo 
        self.posicion = posicion
        
class Vehiculo:
    def __init__(self,id, unidad, marca, modelo, capacidadDeCarga, consumo, velocidadMedia):
        self.id = id
        self.unidad = unidad
        self.marca = marca
        self.modelo = modelo
        self.capacidadDeCarga = capacidadDeCarga
        self.consumo = consumo
        self.velocidad = velocidadMedia

class Destino:
    def __init__(self, nombre, carga, descarga):
        self.nombre = nombre;
        self.carga = carga;
        self.descarga = descarga;

class Costo:
    def __init__(self, salario, combustible, peaje, viatico):
        self.salario = salario
        self.combustible = combustible
        self.peaje = peaje
        self.viatico = viatico

class Logistica:
    def __init__(self,id, distribucion, costo, tiempo, capacidad, destinos,distancia):
        self.id = id
        self.distribucion = distribucion
        self.costo = costo
        self.tiempo = tiempo
        self.capacidad = capacidad
        self.destinos = destinos
        self.distancia = distancia

class Orden:
    def __init__(self,id, fecha, origen, destino, colchones, vehiculo, logistica):
        self.id = id
        self.fecha = fecha
        self.origen = origen
        self.destino = destino
        self.colchones = colchones
        self.vehiculo = vehiculo
        self.logistica = logistica