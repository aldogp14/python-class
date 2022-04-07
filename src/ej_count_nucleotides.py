'''
NAME
    ej_count_nucleotides

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que cuenta el numero de A, T, C y G en una secuencia introducida por el usuario.

USAGE
    null

ARGUMENTS
    null
'''
# Pedir la secuencia
seq = input(F"Dame una secuencia de DNA:\n").upper()

# Imprimir las frecuencias contando cuantas veces aparecen A, T, C o G segun sea el caso.
print(f"\nfrecuencia de A:", seq.count('A'), "\nfrecuencia de T:", seq.count(
    'T'), "\nfrecuencia de C:", seq.count('C'), "\nfrecuencia de G:", seq.count('G'), "\n")
