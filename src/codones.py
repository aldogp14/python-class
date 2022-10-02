'''
NAME
    Codones de una secuencia

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime los codones de una secuencia de ADN

USAGE
    py src/codones.py

ARGUMENTS
'''

# importar
from Bio.Seq import Seq
from Bio import SeqIO
import re

archivo = "data/seq.nt.fa"

# pasar fasta a diccionario
dict = SeqIO.to_dict(SeqIO.parse(archivo, "fasta"))

# recorrer las secuencias del diccionario
for i in range(1, len(dict) + 1):
    # buscar codones
    codones = re.findall(r'(.{3})', str(dict[F'seq{i}'].seq))
    # imprimir
    print(F">{dict[F'seq{i}'].id}")
    for i in range(0, len(codones)):
        print(codones[i], end=" ")
    print("\n")
