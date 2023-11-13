
class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def infiltArriba(self, i):#El método infiltArriba se utiliza para mantener la propiedad del montículo después de insertar un nuevo elemento
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:#Compara el nuevo elemento con su padre 
                #si el nuevo elemento es menor,lo intercambia. Cotinúa hasta que el elemento esté en una posicion mayor a la del padre 
                aux = self.listaMonticulo[i // 2]#Sucede el intercambio
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]#El padre pasa a ser el nuvo elemento
                self.listaMonticulo[i] = aux#El que era el padre pasa a ser el hijo
            i = i // 2

    def insertar(self, paciente):#Añade un nuevo elemento al final del montículo 
        self.listaMonticulo.append(paciente)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)#luego llama a infiltArriba para asegurarse de que el montículo siga siendo un montículo.

    def infiltAbajo(self, i):#Se utiliza para mantener la propiedad del montículo luego de eliminar la raíz
        while (i * 2) <= self.tamanoActual:
            hijo_menor = self.hijoMin(i)
            if self.listaMonticulo[i]> self.listaMonticulo[hijo_menor]:#Compara la nueva raíz (último elemento del árbol)
                # con sus hijos, y si es mayor que cualquiera de ellos, los intercambia. Continúa haciendo esto hasta que elemento esté en una posicion donde es menor que sus hijos
                aux = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hijo_menor]
                self.listaMonticulo[hijo_menor] = aux
            i = hijo_menor#Luego, se mueve al hijo y repite el proceso hasta que llega a una hoja del montículo

    def hijoMin(self, i): #Devuelve el índice del hijo que es menor de un nodo
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2]< self.listaMonticulo[i * 2 + 1]:
                #Si el nodo solo tiene un hijo(está en el índice tamanoActual//2)
                return i * 2#devuelve ese hijo
            else:#De lo contrario, devuelve el hijo con el valor más pequeño
                return i * 2 + 1

    def eliminarMin(self):#Elimina y devuelvela  raíz del montículo (el elemento más pequeño)
        valor_eliminado = self.listaMonticulo[1]#Guarda el valor de la raíz
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]#reemplaza la raíz con el último elemento del montículo
        self.tamanoActual = self.tamanoActual - 1#Disminuye el tamaño del montículo en 1
        self.listaMonticulo.pop()#Elimina el último elemento de la lista
        self.infiltAbajo(1)#Llama inflitAbajo para restaurar la propiedad del montpiculo
        return valor_eliminado

    def construirMonticulo(self, unaLista): #Construye un montículo a partir de una lista de elementos
        i = len(unaLista) // 2#Comienza en el medio de la lista (padre del último elelemnto de la list)
        self.tamanoActual = len(unaLista)#Inicializa tamaño con la cantidad de elemento de la lista
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)#Llamando a infiltAbajo para cada elemento
            i = i - 1#comienza a moverse hacia atrás. Esto asegura que cada subárbol es un montículo antes de que infiltAbajo se llame en su padre,
            #lo que a su vez asegura que cada subárbol más grande también es un montículo
    
    def __str__(self):
        return str(self.listaMonticulo)
    
    def __len__(self):
        return len(self.listaMonticulo)

        #hacerla iterable

    def __iter__(self):
        self._iter_index = 1  # Iniciar desde el primer elemento del montículo
        return self

    def __next__(self):
        if self._iter_index <= self.tamanoActual:
            elemento = self.listaMonticulo[self._iter_index]
            self._iter_index += 1
            return elemento
        else:
            raise StopIteration
    
    def ordenar_monticulo(self):
        
        while self.listaMonticulo:
            minimo = self.extraer_min()
            elementos_iguales = [minimo]

            while self.listaMonticulo and self.listaMonticulo[1] == minimo:
                elementos_iguales.append(self.extraer_min())

        return

