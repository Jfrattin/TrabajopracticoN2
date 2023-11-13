from modules.monticulo import Monticulo
from modules.grafo import Grafo
from modules.vertice import Vertice

def leer_vertices(ruta):
    grafo = Grafo()
    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                # Separo los datos por ","
                elementos = linea.strip().split(",")

                ciudad_origen = elementos[0]
                ciudad_destino = elementos[1]
                peso = int(elementos[2])
                precio = int(elementos[3])

                # Agrego la arista
                grafo.agregarArista(ciudad_origen, ciudad_destino, peso, precio)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en la ruta: {ruta}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

    return grafo
    