'''
NAME
    Costos de inductores

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime los genes mas baratos para cada condicion

USAGE
    py src/costoProduccion.py

ARGUMENTS
'''
# importar librerias
import numpy as np

# EJERCICIO 1
# pasar a array los archivos
produccion_gMl = np.genfromtxt(
    r'C:\Users\Aldo Garcia Prado\Desktop\ciencias_genomicas\semestre_2\python_class\data\prod_gml.csv', delimiter=',')
costos = np.genfromtxt(
    r'C:\Users\Aldo Garcia Prado\Desktop\ciencias_genomicas\semestre_2\python_class\data\ind_cost.csv', delimiter=',')

# convertir gramos/mililitro a gramos/litro
produccion_gL = produccion_gMl * 1000

# convertir los costos
costos_30C = costos * 1.75
costos_35C = costos * 0.8


# EJERCICIO 2
# sacar el costo de 1 gramo/litro de cada condicion
costo_gL_30C = costos_30C / produccion_gL[0:4, 0]
costo_gL_35C = costos_35C / produccion_gL[0:4, 1]


# EJERCICIO 3
# crear una lista de numeros, relativos a los genes
genes = np.array([1, 2, 3, 4])
fo

# sacar la diferencia de costos por condicion
difCostos = costo_gL_30C - costo_gL_35C

# imprimir los genes mas baratos para cada condicion
print(F'genes mas \'baratos\' a 30C: {genes[difCostos < 0]}')
print(F'genes mas \'baratos\' a 35C: {genes[difCostos > 0]}')
