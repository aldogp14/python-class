'''
NAME
    Porcentaje de un aa en una secuencia.

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime la suma de los porcentajes de aminoacidos en una secuencia, 
    los parametros se pasan por linea de comandos

USAGE
    python sr/porcentaje_aa_lista.py [-h] -i str [-as list]

ARGUMENTS
    -i: secuencia en la que se buscara el aminoacido
    -aa_s: codigo IUPAC de los aminoacidoa a buscar
'''
import argparse
import re

# crear parametros
parser = argparse.ArgumentParser(
    description="Script que calcula calcula la suma del porcentaje de aminoacidos en una secuencia")
parser.add_argument("-i", "--input",
                    help="secuencia de aas", required=True)
parser.add_argument("-as", "--aminoAcidos",
                    help="lista aminoacidos a buscar", required=False)
args = parser.parse_args()

# guardar parametros en variables y pasar a mayuscula la secuencia
secuencia = args.input.upper()
aa_s = args.aminoAcidos

try:
    if re.search("\d", secuencia):
        raise ValueError()
except ValueError:
    print("Tu secuencia contiene digito(s)\n")
    quit()

# funcion para calcular porcentaje


def porcentaje_aa(secuencia, aa_s=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    porcentaje = 0
    for aa in aa_s:
        long = len(secuencia)
        porcentaje += secuencia.count(aa) / long * 100
    return (porcentaje)


# imprimir porcentaje
if aa_s:
    print(
        F"Los aminoacidos que busca representan el {porcentaje_aa(secuencia, aa_s.upper())}%\n")
else:
    print(F"Aminoacidos hidrofilicos: {porcentaje_aa(secuencia)}%\n")
