'''
NAME
    ej_porcentaje_GCAT

VERSION
   1.1

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que indica los porcentajes de GC y AT cuando le introduces la direccion de la secuencia.

USAGE
    usar el archivo en la direccion: data/dna.txt

ARGUMENTS
    null
'''
from multiprocessing.sharedctypes import Value
from typing import IO

# Pedir la direccion al usuario y guardarla en una variable
nombre_archivo = input("Introduce la direccion del archivo con la secuencia: ")

# Ver si la direccion es correcta
try:
    archivo = open(nombre_archivo)

except IOError as ex:
    print(F"El archivo {ex.filename} no se encuentra\n")
    quit()

else:
    seq = archivo.read().rstrip('\n')

    # Ver si la secuencia tiene Ns y mandar un error si asi es.
    try:
        if seq.count('N') > 0:
            raise ValueError()
    except ValueError:
        print(F"La secuencia contiene {seq.count('N')} Ns")
        quit()

    else:
        try:
            # Ver si la cadena esta vacia
            if (len(seq) < 1):
                raise ValueError()
        except ValueError:
            print(F"Tu cadena esta vacia")
            quit()
        # Hacer las cuentas y calculos para los porcentajes
        else:
            long = len(seq)
            porcentaje_AT = ((seq.count('A') + seq.count('T')) / long * 100)
            porcentaje_GC = ((seq.count('G') + seq.count('C')) / long * 100)

# imprimir los porcentajes
print(
    F"Porcentaje de AT: {porcentaje_AT}%\nPorcentaje de GC: {porcentaje_GC}%\n")
