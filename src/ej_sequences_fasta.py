'''
NAME
    ej_sequences_fasta

VERSION
   1.1

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que convierte un input con el nombre de la secuencia y la secuencia a un archivo con formato fasta.

USAGE
    null

ARGUMENTS
    null
'''
try:
    # Guardar las secuencias como lista.
    file = open('data/dna_sequences.txt')

# ver si la direccion en el codigo es correcta
except IOError as ex:
    print(F"El archivo {ex.filename} no se encuentra\n")
    quit()

else:
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

    # Decir al usuario donde esta su archivo generado
    print("Tus secuencias con formato fasta se encuentran en results/dna.fasta")
