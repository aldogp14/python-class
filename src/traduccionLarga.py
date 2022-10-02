'''
NAME
    Proteína traducida más larga

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime la secuencia proteíca mas larga de los 6 posibles ORFs

USAGE
    py src/traduccionLarga.py

ARGUMENTS
'''

# importar
import argparse
from Bio.Seq import Seq
from Bio import SeqUtils
from Bio import SeqIO

# iniciar parseo
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--direccion",
                    help="direccion del archivo fasta", required=False)
args = parser.parse_args()
archivo = args.direccion

secuencias = []
if archivo:
    encabezado = []
    # crear un vector con todas las secuencias del fasta y uno con los encabezados
    for secuencia in SeqIO.parse(archivo, "fasta"):
        secuencias.append(secuencia.seq)
        encabezado.append(secuencia.id)
else:
    # guardar secuencia default
    secuencias.append(Seq(
        "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"))
# guardar el patron
patron = Seq("ATG")

# buscar las posiciones de inicio


def posicionesInicio(secuencia):
    posiciones = []
    for i in range(0, 2):
        resultado = SeqUtils.nt_search(str(secuencia[i:]), patron)
        for i in range(1, len(resultado)):
            posiciones.append(resultado[i])
    return(posiciones)

# traducir todos los ORFs


def traduce(secuencia, posiciones):
    peptidos = []
    for i in range(0, len(posiciones)):
        peptidos.append(secuencia[posiciones[i]:].translate(to_stop=True))
    return(peptidos)

# buscar cual es el peptido mas largo


def peptidoLargo(peptidos):
    long = 0
    for i in range(0, len(peptidos)):
        # en caso de entrar al "if" es porque se encontro un peptido mas largo
        if int(len(peptidos[i])) > long:
            indice = i
            long = int(len(peptidos[i]))
    return(indice)


for i in range(0, len(secuencias)):
    # llamar a funciones
    posiciones = posicionesInicio(secuencias[i])
    posicionesRevComp = posicionesInicio(secuencias[i].reverse_complement())
    peptidos = traduce(secuencias[i], posiciones) + \
        traduce(secuencias[i].reverse_complement(), posicionesRevComp)
    # imprimir output
    if archivo:
        print(F"{encabezado[i]} -> {peptidos[peptidoLargo(peptidos)]}")
    else:
        print(F"Default -> {peptidos[peptidoLargo(peptidos)]}")
