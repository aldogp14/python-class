'''
NAME
    ej_porcentaje_GCAT

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que indica los porcentajes de GC y AT cuando le introduces la direccion de la secuencia.

USAGE
    null

ARGUMENTS
    null
'''

# Pedir la secuencia al usuario y guardarla en una variable
nombre_archivo = input("Introduce la direccion del archivo con la secuencia: ")
archivo = open(nombre_archivo)
contenido = archivo.read().rstrip('\n')

# Hacer las cuentas y calculos para los porcentajes
long = len(contenido)
porcentaje_AT = ((contenido.count('A') + contenido.count('T')) / long * 100)
porcentaje_GC = ((contenido.count('G') + contenido.count('C')) / long * 100)

# imprimir los porcentajes
print(
    F"Porcentaje de AT: {porcentaje_AT}%\nPorcentaje de GC: {porcentaje_GC}%\n")
