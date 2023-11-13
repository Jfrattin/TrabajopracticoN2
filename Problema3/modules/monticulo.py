import heapq

class Monticulo:
    def __init__(self):
        self.cola = []
        self.indice = 0

    def insertar(self, clave, prioridad):#Inserta un elemento en la cola con una clave y una prioridad
        heapq.heappush(self.cola, (prioridad, self.indice, clave))
        self.indice += 1

    def obtener(self):#Elimina y devuelve el elemento con la mayor prioridad de la cola
        return heapq.heappop(self.cola)[-1]#heappop de la biblioteca heapq se utiliza para este propósito

    def esta_vacia(self):#Verifica si la cola está vacía 
        return not bool(self.cola)

    def decrementar_clave(self, clave, nueva_prioridad):#Este método disminuye la prioridad de un elemento dadao en la cola.
        for i, (prioridad, _, c) in enumerate(self.cola):
            if c == clave:
                self.cola[i] = (nueva_prioridad, self.indice, clave)
                self.indice += 1
                heapq.heapify(self.cola)
                break
