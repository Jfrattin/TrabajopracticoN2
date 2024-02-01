# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
from modules.paciente import Paciente as pac
from faker import Faker
from modules.monticulo import MonticuloBinario 
import random

n = 20  # cantidad de ciclos de simulación

cola_de_espera =  MonticuloBinario()
    
# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    
    # Crea una instancia de Faker
    fake = Faker()

    # Genera un nombre aleatorio
    nombre_aleatorio = fake.name()          
    
    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    criticidad_aleatoria = random.randint(1, 3)
    paciente = pac(ahora,criticidad_aleatoria,nombre_aleatorio)
    print('-*-'*15)
    print("Ingreso el paciente", paciente.nombre ,'', ahora.strftime('%d/%m/%Y %H:%M:%S'), '' , "con Riesgo:" ,criticidad_aleatoria )
    
    cola_de_espera.insertar(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.eliminarMin()
        
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)
