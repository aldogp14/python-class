'''
NAME
    ej_porcentaje_GCAT

VERSION
   1.2

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que indica los porcentajes de GC y AT cuando le introduces la direccion de la secuencia.

USAGE
    python src/ej_porcentaje_GCAT.py [-h] -i path/to/file [-o OUTPUT]

ARGUMENTS
  -h, --help            show this help message and exit
  -i path/to/file, --input path/to/file
                        File with gene sequences
  -o OUTPUT, --output OUTPUT
                        Direccion del archivo de salida
'''

from multiprocessing.sharedctypes import Value
from typing import IO
import argparse

# crear parser
parser = argparse.ArgumentParser(
    description="Script que calcula el contenido de AT usando argumentos por linea de comando")
# añadir argumentos
parser.add_argument("-i", "--input", metavar="path/to/file",
                    help="File with gene sequences", required=True)
parser.add_argument(
    "-o", "--output", help="Direccion del archivo de salida", required=False)
# ejecutar
args = parser.parse_args()
# guardar en variables
nombre_archivo = args.input
nombre_output = args.output

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

# condicion para ver si nombre_output fue rellenada
if nombre_output:
    # mandar el resultado a la direccion introducida por el usuario
    file = nombre_output
    file = open(nombre_output, 'w')
    file.write(
        F"Porcentaje de AT: {porcentaje_AT}%\nPorcentaje de GC: {porcentaje_GC}%")
    file.close()
    print(F"Los porcentajes se encuentran en: {nombre_output}")
else:
    # imprimir los porcentajes
    print(
        F"Porcentaje de AT: {porcentaje_AT}%\nPorcentaje de GC: {porcentaje_GC}%\n")
