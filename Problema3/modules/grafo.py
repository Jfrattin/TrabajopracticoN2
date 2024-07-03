from modules.vertice import Vertice
from modules.monticulo import Monticulo
# se crea una clase Grafo utilizando la bilbiografia de brindada por la catedra y se  adapata al problema en cuestion
class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self, clave): #Agrega un nuevo vértice al grafo
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)#Nuevo objeto vertice
        self.listaVertices[clave] = nuevoVertice#Lo añade al diccionario y aumenta el contador
        return nuevoVertice

    def obtenerVertice(self, n):#Devuelve el vérice correspondiente a la clave pasada como argumento si existe en el grafo. Si no existe devuelve None
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self, n):#Verifica si la clave está en el grafo
        return n in self.listaVertices

    def agregarArista(self, de, a, costo=0,precio=0):#Agrega una arista al grafo. Las claves de los vértices de origen y destino se pasan como argumento,
        #junto con el costo y el precio.
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:#Si alguno de los vértices no existe en el grafo, se crea un nuevo vértice
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo,precio)

    def obtenerVertices(self):#Devuelve todas las claves de los vértices en el grafo
        return self.listaVertices.keys()

    def __iter__(self):#Permite iteraar sobre los objetos de vértice en el grafo.
        return iter(self.listaVertices.values())

    ## tomaremos como "distancia" el peso maximo
    def maximo_peso_transportado(self, ciudad_inicio, ciudad_destino):
        cola_prioridad = Monticulo()
        pesosmax = {ciudad: float("-inf") for ciudad in self.listaVertices}  # Asigna a cada ciudad peso inicial de menos infinito, excepto la ciudad de inicio
        pesosmax[ciudad_inicio] = float("inf")
        cola_prioridad.insertar(ciudad_inicio, float("inf"))

        while not cola_prioridad.esta_vacia():  # Mientras no esté vacía
            ciudad_actual = cola_prioridad.obtener()  # Obtiene la ciudad con la mayor distancia es decir la ciudad con mayor peso maximo
            # print(cola_prioridad)
            # print(ciudad_actual)
            if ciudad_actual == ciudad_destino:  # Si es la ciudad final devuelve el peso maximo .
                return pesosmax[ciudad_actual]

            vertice_actual = self.listaVertices[ciudad_actual]

            for vecino in vertice_actual.obtenerConexiones():  # Para cada vecino de la ciudad actual
                ciudad_vecino = vecino.id
                peso = vertice_actual.obtenerPonderacion(vecino)
                peso_posible = min(pesosmax[ciudad_actual], peso)  # Calcula el posible peso como el mínimo entre la peso actual a la ciudad y el peso de la arista a ese vecino
                if peso_posible > pesosmax[ciudad_vecino]:  # Si este peso posible es mayor que la peso actual al vecino
                    pesosmax[ciudad_vecino] = peso_posible  # Actualiza lel peso del vecino
                    cola_prioridad.insertar(ciudad_vecino, peso_posible)  # Lo inserta en la cola de prioridad

        return float("-inf")

    def minimo_precio_envio(self, ciudad_inicio, ciudad_destino):
        pesomax = self.maximo_peso_transportado(ciudad_inicio, ciudad_destino) # calculo el maximo peso posible a trasportar
        cola_prioridad = Monticulo()
        costos = {city: float("inf") for city in self.listaVertices}  # Asigna a cada ciudad un costo inicial infinito
        costos[ciudad_inicio] = 0  # Ciudad de inicio tiene un costo de cero
        cola_prioridad.insertar(ciudad_inicio, 0)

        while not cola_prioridad.esta_vacia():
            ciudad_actual = cola_prioridad.obtener()  # Obtiene la ciudad con el menor costo actual

            if ciudad_actual == ciudad_destino:
                return costos[ciudad_actual]  # Si es la ciudad final, devuelve el costo mínimo hasta ella

            vertice_actual = self.listaVertices[ciudad_actual]
            for vecino in vertice_actual.obtenerConexiones():  # Para cada vecino de la ciudad actual
                ciudad_vecino = vecino.id
                costo = vertice_actual.obtenerPrecio(vecino)  # Obtiene el precio de la arista
                peso = vertice_actual.obtenerPonderacion(vecino) # obtengo el peso 
                costo_posible = costos[ciudad_actual] + costo
                # print("###ciudad_actual##")
                # print(ciudad_actual)
                # print(pesomax)
                # print(peso)
                # print("#####")
                if pesomax <= peso: # siempre que peso maximo sea menor al peso trasportado
                    if costo_posible < costos[ciudad_vecino]:
                                    # Si el costo posible es menor que el costo actual y el peso de la arista es <= pesomax
                                        costos[ciudad_vecino] = costo_posible  # Actualiza el costo del vecino
                                        cola_prioridad.insertar(ciudad_vecino, -costo_posible)  # Inserta en la cola de prioridad

        return float("inf")  # Si no se encontró camino válido, devuelve infinito o maneja según tu lógica
