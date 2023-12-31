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

    def maximo_peso_transportado(self, ciudad_inicio, ciudad_destino):
        cola_prioridad = Monticulo()
        distancias = {ciudad: float("-inf") for ciudad in self.listaVertices}  # Asigna a cada ciudad distancia inicial de menos infinito, excepto la ciudad de inicio
        distancias[ciudad_inicio] = float("inf")
        cola_prioridad.insertar(ciudad_inicio, float("inf"))

        while not cola_prioridad.esta_vacia():  # Mientras no esté vacía
            ciudad_actual = cola_prioridad.obtener()  # Obtiene la ciudad con la mayor distancia
            if ciudad_actual == ciudad_destino:  # Si es la ciudad final devuelve la distancia
                return distancias[ciudad_actual]

            vertice_actual = self.listaVertices[ciudad_actual]

            for vecino in vertice_actual.obtenerConexiones():  # Para cada vecino de la ciudad actual
                ciudad_vecino = vecino.id
                peso = vertice_actual.obtenerPonderacion(vecino)
                peso_posible = min(distancias[ciudad_actual], peso)  # Calcula el posible peso como el mínimo entre la distancia actual a la ciudad y el peso de la arista a ese vecino
                if peso_posible > distancias[ciudad_vecino]:  # Si este peso posible es mayor que la distancia actual al vecino
                    distancias[ciudad_vecino] = peso_posible  # Actualiza la distancia del vecino
                    cola_prioridad.insertar(ciudad_vecino, peso_posible)  # Lo inserta en la cola de prioridad
        
        return float("-inf")
    
    def minimo_precio_envio(self, start_city, end_city):
        cola = Monticulo()
        costos = {city: float("inf") for city in self.listaVertices}#Asigna a cada ciudad un costo inicial infinito
        costos[start_city] = 0 #Ciudad de inicio tiene un costo de cero
        cola.insertar(start_city, 0)

        
        while not cola.esta_vacia():#Mientras la cola no esté vacía
            current_city = cola.obtener()#Obtiene la ciudad con el menor costo
            if current_city == end_city:#Si es la ciudad final, devuelve el costo
                return costos[current_city]

            current_vertex = self.listaVertices[current_city]

            for neighbor in current_vertex.obtenerConexiones():#Para cada vecino de la ciudad actual
                neighbor_city = neighbor.id
                cost = current_vertex.obtenerPrecio(neighbor)  #devuelve el precio de la arista
                possible_cost = costos[current_city] + cost
                if possible_cost < costos[neighbor_city]:#Si el posible costo es menor que el costo actual al vecino 
                    costos[neighbor_city] = possible_cost#Actualiza el costo del vecino
                    cola.insertar(neighbor_city, -possible_cost)#Lo inserta en la cola de prioridad
