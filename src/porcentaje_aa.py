'''
NAME
    Porcentaje de un aa en una secuencia.

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime el porcentaje de un aminoacido en una secuencia, los parametros se pasan por linea de comandos

USAGE


ARGUMENTS
    -i: secuencia en la que se buscara el aminoacido
    -aa: codigo IUPAC de una letra del aminoacido a buscar
'''
import argparse

# crear parametros
parser = argparse.ArgumentParser(
    description="Script que calcula el porcentaje de un aminoacido en una secuencia")
parser.add_argument("-i", "--input", metavar="path/to/file",
                    help="secuencia de aas", required=True)
parser.add_argument("-aa", "--aminoAcido", metavar="path/to/file",
                    help="aminoacido a buscar", required=True)
args = parser.parse_args()

# guardar parametros en variables y pasar a mayusculas
secuencia = args.input.upper()
aa = args.aminoAcido.upper()


def porcentaje_aa(secuencia, aa):  # funcion para calcular porcentaje
    long = len(secuencia)
    return(secuencia.count(aa) / long * 100)


# imprimir porcentaje
print(porcentaje_aa(secuencia, aa))
