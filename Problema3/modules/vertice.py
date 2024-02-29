
class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.peso = 0
        self.predecesor = None
        self.precio=float('inf')
    def agregarVecino(self, vecino, ponderacion=0,precio=0):#Este método agrega un vértice vecino al vértice actual con una ponderación la ponderacion en este caso seria el peso maximo  y un precio dados
        self.conectadoA[vecino] = (ponderacion,precio)#Guardamos el precio junto con la ponderación
    #Este metodo asigna una peso entre los nodos
    def asignarPeso(self, peso):
        self.peso = peso
    #Este metodo obtiene una peso entre los nodos
    def obtenerpeso(self):
        return self.peso
    #Este metodo obtiene una peso entre los nodos
    def asignarPredecesor(self, predecesor):
        self.predecesor = predecesor
    #Este metodo obtiene el predecesor entre los nodos
    def obtenerPredecesor(self):
        return self.predecesor
    #Devuelve la informacion del vertice representada como una cadena de caracteres
    def __str__(self):
        return str(self.id)
    #Devuelve todos los vértices vecinos del vértice actual
    def obtenerConexiones(self):
        return self.conectadoA.keys()   
    #Devuelve la ponderación al vértice dado
    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino][0]
    #Devuelve el precio al vértice dado
    def obtenerPrecio(self,vecino):
        return self.conectadoA[vecino][1]
 