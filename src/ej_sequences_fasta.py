'''
NAME
    ej_sequences_fasta

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que convierte un input con el nombre de la secuencia y la secuencia a un archivo con formato fasta.

USAGE
    null

ARGUMENTS
    null
'''
# Guardar las secuencias como lista.
file = open('data/dna_sequences.txt')
sequences = file.readlines()

# Abrir el archivo para el fasta
fasta = open("results/sequences_fasta.txt", 'w')

# Recorrer cada elemento de la lista.
# Primero hacer modificaciones generales y luego especificas, como el upper y reemplazar caracteres.
# Guardar cada elemento modificado en un archivo.
for sequence in sequences:
    seq = sequence.replace(F"{sequence}", F"> {sequence}").split("   ")
    seq[1] = seq[1].upper().replace("-", "", 1000).rstrip('\n')
    for s in seq:
        fasta.write(F"{s}\n")

# Cerrar el archivo
fasta.close()
