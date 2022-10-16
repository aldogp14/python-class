'''
NAME
    resumen genes Genbank

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    resumen archivo genbank e imprime la secuencia ADN, ARN y proteica de genes que pida el usuario

USAGE
    py src/resumenGenbank.py -i [direccion] -g [genes]

ARGUMENTS
-i direccion del archivo genbank
-g genes que se buscan
'''

# importar librerias
import argparse
from Bio import SeqIO
from Bio.Seq import Seq

# crear parseo y parametros
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--genes",
                    help="genes que se busquen", required=True)
parser.add_argument("-i", "--direccion",
                    help="direccion del archivo genbank", required=True)
genes = parser.parse_args().genes

# funcion para revisar si esta el gen del indice esta en la lista de genes del usuario


def check(gen):
    for genX in genes:
        if gen == genX:
            # borrar de la lista del usuario para hacerlo mas eficiente
            genes.replace('genX', '')
            return True

# funcion que imprime lo que respecta a cada gen


def printDogma():
    n = 1
    # recorrer los genes
    for i in range(2, len(x.features), 2):
        if check(x.features[i].qualifiers['gene'][0]):
            # guardar la posicion de inicio del gen en la secuencia
            inicio = x.features[i].location.nofuzzy_start
            # guardar la secuencia
            sec = Seq(x.seq[inicio: inicio + 15])
            print('Gen_', n, ': ', x.features[i].qualifiers['gene'][0])
            print('Secuencia: ', sec)
            # traducir y transcribir
            print('Transcripcion: ', sec.transcribe())
            print('Traduccion: ', sec.translate(), '\n')
            n += 1


# guardar la lectura del archivo genbank
x = SeqIO.read(parser.parse_args().direccion, 'genbank')
# imprimir el resumen
print('Organismo: ', x.annotations['organism'])
print('Fecha: ', x.annotations['date'])
print('País: ', x.features[0].qualifiers['country'][0], '\n')
printDogma()
