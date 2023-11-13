from modules.monticulo import MonticuloBinario
from modules.paciente import Paciente

lista = [4,8,4,5,89,4,15,1,3,5,19,819,4]

pruebamonticulo2 = MonticuloBinario()

pruebamonticulo = MonticuloBinario()
pruebamonticulo.construirMonticulo(lista)
print("montuculo desordenado")

print(pruebamonticulo)


pruebamonticulo2.insertar(1)
print("El monticulo ")
print(pruebamonticulo2)
pruebamonticulo2.insertar(12)
print("El monticulo ")
print(pruebamonticulo2)
pruebamonticulo2.insertar(1)
print("El monticulo ")
print(pruebamonticulo2)
pruebamonticulo2.insertar(1)
print("El monticulo ")
print(pruebamonticulo2)
pruebamonticulo2.insertar(1)
print("El monticulo ")
print(pruebamonticulo2)
pruebamonticulo2.insertar(5)
print("El monticulo ")
print(pruebamonticulo2)
pruebamonticulo2.insertar(4)
print("El monticulo ")
print(pruebamonticulo2)
pruebamonticulo2.insertar(4)
print("El monticulo ")
print(pruebamonticulo2)
pruebamonticulo2.insertar(5)
print("El monticulo ")
print(pruebamonticulo2)

print(pruebamonticulo2.eliminarMin())
print("El monticulo ")
print(pruebamonticulo2)
