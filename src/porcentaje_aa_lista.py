'''
NAME
    Porcentaje de un aa en una secuencia.

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime la suma de los porcentajes de aminoacidos en una secuencia, los parametros se pasan por linea de comandos

USAGE


ARGUMENTS
    -i: secuencia en la que se buscara el aminoacido
    -aa_s: codigo IUPAC de los aminoacidoa a buscar
'''
import argparse

# crear parametros
parser = argparse.ArgumentParser(
    description="Script que calcula calcula la suma del porcentaje de aminoacidos en una secuencia")
parser.add_argument("-i", "--input", metavar="path/to/file",
                    help="secuencia de aas", required=True)
parser.add_argument("-as", "--aminoAcidos", metavar="path/to/file",
                    help="lista aminoacidos a buscar", required=False)
args = parser.parse_args()

# guardar parametros en variables y pasar a mayuscula la secuencia
secuencia = args.input.upper()
aa_s = args.aminoAcidos


# funcion para calcular porcentaje
def porcentaje_aa(secuencia, aa_s=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    porcentaje = 0
    for aa in aa_s:
        long = len(secuencia)
        porcentaje += secuencia.count(aa) / long * 100
    return (porcentaje)


# imprimir porcentaje
if aa_s:
    print(porcentaje_aa(secuencia, aa_s.upper()))
else:
    print(porcentaje_aa(secuencia))
