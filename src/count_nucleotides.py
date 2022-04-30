'''
NAME
    ej_count_nucleotides

VERSION
   1.1

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que cuenta el numero de A, T, C y G en una secuencia introducida por el usuario.

USAGE
    null

ARGUMENTS
    null
'''
from typing import IO

# Pedir la secuencia
seq = input(F"Dame una secuencia de DNA:\n").upper()

# ver si la secuencia tiene Ns y mandar error
if seq.count('N') > 0:
    raise ValueError(F"La secuencia contiene {seq.count('N')} Ns")

# Imprimir las frecuencias contando cuantas veces aparecen A, T, C o G segun sea el caso.
else:
    print(f"\nfrecuencia de A:", seq.count('A'), "\nfrecuencia de T:", seq.count(
        'T'), "\nfrecuencia de C:", seq.count('C'), "\nfrecuencia de G:", seq.count('G'), "\n")
