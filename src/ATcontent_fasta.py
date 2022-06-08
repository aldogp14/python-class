'''
NAME
    Porcentaje de AT y formateador a FASTA
    
VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que indica el porcentaje de AT y GC de una secuencia y ademas manda la secuencia a un archivo con formato fasta

USAGE


ARGUMENTS
    -s la secuencia a usar

'''
import argparse
# importar los modulos
import pkg.mod1
import pkg.mod2

# iniciar argparse
parser = argparse.ArgumentParser(
    description="Script que calcula el porcentaje de un aminoacido en una secuencia")
# crear el parametro para pedir secuencia
parser.add_argument("-s", "--secuencia",
                    help="secuencia de aas", required=True)
args = parser.parse_args()
# guardar parametro en variables y pasar a mayuscula
sec = args.secuencia.upper()

# llamar a funciones de los modulos
pkg.mod1.porcentaje_ATGC(sec)
pkg.mod2.fasta(sec)
