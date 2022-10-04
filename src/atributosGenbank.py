'''
NAME
    atributos archivo genbank

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime el organismo, fecha y feature[país] de un archivo genbank

USAGE
    py src/atributosGenbank.py

ARGUMENTS
'''
from Bio import SeqIO

for x in SeqIO.parse("data/virus.gb", "genbank"):
    print('organismo: ', x.annotations['organism'])
    print('fecha: ', x.annotations['date'])
    print('país: ', x.features[0].qualifiers['country'], '\n')
