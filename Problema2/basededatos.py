from modules.Temperaturas import Temperaturas_DB
base_datos = Temperaturas_DB()

# Guardar temperaturas
base_datos.guardar_temperatura(22.5, "15/08/2022")
base_datos.guardar_temperatura(25.0, "16/08/2022")
base_datos.guardar_temperatura(23.7, "18/08/2022")
base_datos.guardar_temperatura(19.8, "19/08/2022")
base_datos.guardar_temperatura(24.2, "20/08/2023")
base_datos.guardar_temperatura(18.3, "21/09/2023")
base_datos.guardar_temperatura(12.1, "22/09/2023")
base_datos.guardar_temperatura(26.5, "23/09/2023")
base_datos.guardar_temperatura(9.4, "24/10/2023")
base_datos.guardar_temperatura(8.5, "18/10/2023")

# Consultar temperaturas
diaconsulta = "15/08/2022"
diarangoinicial= "15/08/2022"
diarangofinal= "19/08/2022"
borrartemp = "18/10/2023"
rangototalinicial = "15/08/2022"
rangototalfinal= "18/10/2023"

temp1 = base_datos.devolver_temperatura(diaconsulta)

# Consultar temperaturas en un rango tanto la minima como la maxima
max_temp = base_datos.max_temp_rango(diarangoinicial, diarangofinal)
min_temp = base_datos.min_temp_rango(diarangoinicial, diarangofinal)

# Consultar temperaturas extremas en un rango y devolverla como lista
min_temp2, max_temp2 = base_datos.temp_extremos_rango(diarangoinicial, diarangofinal)

print(f'Temperatura el {diaconsulta}',temp1  )

print("Máxima temperatura en el rango:", max_temp)
print("Mínima temperatura en el rango:", min_temp)

print("Mínima temperatura en el rango:", min_temp2)
print("Máxima temperatura en el rango:", max_temp2) 

# Consultar temperaturas en un rango
rango_temperaturas = base_datos.devolver_temperaturas( diarangoinicial,diarangofinal)
for temp in rango_temperaturas:
    print(temp)

# Obtener la cantidad de muestras en la base de datos
print("Cantidad de muestras:", base_datos.cantidad_muestras())

# Borrar una temperatura
base_datos.borrar_temperatura(borrartemp)

# Consultar temperaturas en un rango
rango_temperaturas = base_datos.devolver_temperaturas(rangototalinicial, rangototalfinal)
for temp in rango_temperaturas:
    print(temp)

# Obtener la cantidad de muestras en la base de datos para ver si borro sin problemas
print("Cantidad de muestras:", base_datos.cantidad_muestras())
