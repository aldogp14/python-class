'''
NAME
    Traductor de RNA

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que traduce una secuencia de RNA 

USAGE
    python src/traductor_rna.py [-h] -i str [-secuencia RNA]

ARGUMENTS
    -i: secuencia de RNA
'''

# importar librerias
import argparse
import re

# iniciar argparse y añadir argumentos
parser = argparse.ArgumentParser(
    description="Script que traduce una secuencia de RNA")
parser.add_argument("-i", "--input",
                    help="secuencia de RNA", required=True)
args = parser.parse_args()

# guardar parametros en variables y pasar a mayuscula la secuencia
rna = args.input.upper()

gencode = {
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M', 'ACA': 'T',
    'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AAC': 'N', 'AAU': 'N',
    'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGU': 'S', 'AGA': 'R',
    'AGG': 'R', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CAC': 'H',
    'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
    'CGG': 'R', 'CGU': 'R', 'GUA': 'V', 'GUC': 'V', 'GUG': 'V',
    'GUU': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
    'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'UCA': 'S', 'UCC': 'S',
    'UCG': 'S', 'UCU': 'S', 'UUC': 'F', 'UUU': 'F', 'UUA': 'L',
    'UUG': 'L', 'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
    'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W'}

# ver si hay caracteres distintos
if re.search(f"[^AUCG]", rna):
    print("Hay caracteres diferentes a 'AUCG'\n")
    quit()

proteina = ""
# ir rompiendo la secuencia en codones y buscar el codon en el diccionario
# la division entera sirve para no tratar de acceder a una celda que no existe**
for i in range(0, len(rna) // 3):
    # multiplicar por tres porque trabajamos con codones**
    codon = rna[i * 3:i * 3 + 3]
    # ver si es un codon de paro
    if gencode.get(codon) != "_":
        proteina += gencode.get(codon)
    else:
        break

# imprimir la secuencia
print(F"secuencia de aminoacidos: {proteina}\n")
