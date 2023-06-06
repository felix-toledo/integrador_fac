import networkx as nx

class Empresa:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_centro(self, centro):
        self.grafo.add_node(centro)

    def agregar_conexion(self, origen, destino, distancia):
        self.grafo.add_edge(origen, destino, distance=distancia)

    def obtener_ruta_mas_corta(self, origen, destinos):
        ruta_mas_corta = []
        distancia_total = 0

        for i in range(len(destinos)):
            if i == 0:
                origen_actual = origen
            else:
                origen_actual = destinos[i - 1]

            destino_actual = destinos[i]

            ruta = nx.dijkstra_path(self.grafo, origen_actual, destino_actual, weight='distance')
            distancia = nx.dijkstra_path_length(self.grafo, origen_actual, destino_actual, weight='distance')

            ruta_mas_corta.extend(ruta[:-1])
            distancia_total += distancia

        ruta_mas_corta.append(destinos[-1])
        return ruta_mas_corta, distancia_total


def calcular_ruta_mas_corta(empresa, origen, destinos):
    try:
        return empresa.obtener_ruta_mas_corta(origen, destinos)
    except nx.NetworkXNoPath:
        return None, None

