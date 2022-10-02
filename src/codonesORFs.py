'''
NAME
    Codones 6 ORFs de una secuencia

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime los codones de una secuencia de ADN buscando en los 6 ORFs

USAGE
    py src/codonesORFs.py

ARGUMENTS
'''

# importar
from Bio.Seq import Seq
from Bio import SeqIO
import re

archivo = "data/seq.nt.fa"

# pasar a un diccionario
dict = SeqIO.to_dict(SeqIO.parse(archivo, "fasta"))

# funcion para imprimir los codones


def imprimir():
    for i in range(0, len(codones)):
        print(codones[i], end=" ")
    print("\n")


# recorrer las secuencias del diccionario
for i in range(1, len(dict) + 1):
    # recorrer marcos de lectura
    for j in (1, 2, 3):
        # buscar codones e imprimir
        codones = re.findall(r'(.{3})', str(dict[F'seq{i}'].seq)[j:])
        print(F">{dict[F'seq{i}'].id}, ORF:{j}")
        imprimir()
        codones = re.findall(r'(.{3})', str(
            dict[F'seq{i}'].seq.reverse_complement())[abs(j):])
        print(F">{dict[F'seq{i}'].id}, ORF:-{j}")
        imprimir()
