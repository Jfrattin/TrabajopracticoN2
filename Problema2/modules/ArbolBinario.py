from modules.NodoArbol import NodoArbol
# Se implementa el codigo de la bibliografia para construir esta clase
class ArbolBinarioBusqueda:

    def __init__(self):
        # Constructor de la clase ArbolBinarioBusqueda
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        # Obtiene el tamaño del árbol
        return self.tamano

    def __len__(self):
        return self.tamano

    def agregar(self, clave, valor):
        # Agrega un nuevo nodo al árbol
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano = self.tamano + 1

    def _agregar(self, clave, valor, nodoActual):
        # Método privado para agregar un nodo de manera recursiva 
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)

    def __setitem__(self, c, v):
        # Permite agregar elementos utilizando notación de corchetes
        self.agregar(c, v)

    def obtener(self, clave):
        # Obtiene el valor asociado con una clave
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener(self, clave, nodoActual):
        # Método privado para obtener un nodo de manera recursiva
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __contains__(self, clave):
        # Verifica si una clave está en el árbol
        return self._obtener(clave, self.raiz) is not None

    def eliminar(self, clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano - 1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self, clave):
        self.eliminar(clave)

    def remover(self, nodoActual):
        if nodoActual.esHoja():
            # Nodo es hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos():
            # Nodo tiene dos hijos
            sucesor = nodoActual.encontrarSucesor()
            sucesor.empalmar()
            nodoActual.clave = sucesor.clave
            nodoActual.cargaUtil = sucesor.cargaUtil
        else:
            # Nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                                     nodoActual.hijoIzquierdo.cargaUtil,
                                                     nodoActual.hijoIzquierdo.hijoIzquierdo,
                                                     nodoActual.hijoIzquierdo.hijoDerecho)
            else:
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                                     nodoActual.hijoDerecho.cargaUtil,
                                                     nodoActual.hijoDerecho.hijoIzquierdo,
                                                     nodoActual.hijoDerecho.hijoDerecho)


