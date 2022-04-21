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
    py ej_sequences_fasta.py

ARGUMENTS
    null
'''
# Guardar las secuencias como lista.
file = open('data/dna_sequences.txt', 'r')
sequences = file.readlines()
file.close()

# Abrir el archivo para el fasta
fasta = open("results/sequences_fasta.fasta", 'w')

# Recorrer cada elemento de la lista.
# Primero hacer modificaciones generales y luego especificas, como el upper y reemplazar caracteres.
# Guardar cada elemento modificado en un archivo.
for sequence in sequences:
    record = sequence.replace(sequence, f"> {sequence}").split("   ")
    record[1] = record[1].upper().replace("-", "", 1000).rstrip('\n')
    for element in record:
        fasta.write(f"{element}\n")

# Cerrar el archivo
fasta.close()
