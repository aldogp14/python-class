'''
NAME
    ej_fasta.py

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que crea un archivo fasta a partir de una secuencia en cierta direccion establecida.

USAGE
    null

ARGUMENTS
    null
'''

# Guardar la secuencia de interes en una variable
file_name = 'data/dna.txt'
file = open(file_name)
content = file.read().rstrip('\n')

# Abri un archivo en carpeta data y escribir la secuencia con formato FASTA
fasta = open("results/dna.fasta", 'w')
fasta.write(F">sequence_name\n{content}")

# Cerrar el archivo
fasta.close()
file.close()
