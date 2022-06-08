'''
NAME
    ej_fasta.py

VERSION
   1.1

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que crea un archivo fasta a partir de una secuencia en cierta direccion establecida.

USAGE
    null

ARGUMENTS
    null
'''
from typing import IO

try:
    # Guardar la secuencia de interes en una variable
    file_name = 'data/dna.txt'

# ver si la direccion en el codigo es correcta
except IOError as ex:
    print(F"El archivo {ex.filename} no se encuentra\n")
    quit()

# Cerrar el archivo
fasta.close()
file.close()

else:
    file = open(file_name)
    content = file.read().rstrip('\n')

    # Abrir un archivo en carpeta data y escribir la secuencia con formato FASTA
    fasta = open("results/dna.fasta", 'w')
    fasta.write(F">sequence_name\n{content}")

    # Cerrar el archivo
    fasta.close()

    # Decir al usuario donde esta su archivo generado
    print("Tu secuencia con formato fasta se encuentra en results/dna.fasta")
