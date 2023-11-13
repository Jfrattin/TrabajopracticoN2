class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        # Constructor de la clase NodoArbol
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        # Verifica si el nodo tiene un hijo izquierdo
        return self.hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        # Verifica si el nodo tiene un hijo derecho
        return self.hijoDerecho is not None

    def esHijoIzquierdo(self):
        # Verifica si el nodo es el hijo izquierdo de su padre
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        # Verifica si el nodo es el hijo derecho de su padre
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        # Verifica si el nodo es la raíz del árbol
        return not self.padre

    def esHoja(self):
        # Verifica si el nodo es una hoja (sin hijos)
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        # Verifica si el nodo tiene al menos un hijo
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        # Verifica si el nodo tiene ambos hijos
        return self.hijoDerecho and self.hijoIzquierdo

    def encontrarSucesor(self):
        # Encuentra el sucesor del nodo actual
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def empalmar(self):
        # Empalma el nodo actual en el árbol
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

    def encontrarMin(self):
        # Encuentra el nodo con el valor mínimo en el subárbol
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        # Reemplaza los datos del nodo con nuevos valores
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

