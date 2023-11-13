
from modules.grafo import Grafo
from modules.utilidades import *

#utilizo la funcion de utilidades para leer los datos del archivo y revolverlo en forma de grafica
ciudadesconectadas = Grafo()
ciudadesconectadas  = leer_vertices("C:/AlgoritmosTuped/TP2-2023/Problema3/rutas.txt")

Centro_reparto_inicial = 'CiudadBs.As.'
Centro_reparto_final= 'LaRioja' 

Peso_maximo = ciudadesconectadas.maximo_peso_transportado(Centro_reparto_inicial,Centro_reparto_final)
print(f'El peso máximo que puede ser ser trapsortado desde {Centro_reparto_inicial} hasta {Centro_reparto_final} es: {Peso_maximo}')
Costo_minimo = ciudadesconectadas.minimo_precio_envio(Centro_reparto_inicial, Centro_reparto_final)
print(f'El precio mínimo de envio desde {Centro_reparto_inicial} hasta {Centro_reparto_final} es: {Costo_minimo}')
