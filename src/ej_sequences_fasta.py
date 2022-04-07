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
# Guardar las secuencias como una cadena y no como lista.
file = open('data/dna_sequences.txt')
content = file.read()

# Cortar la cadena por saltos de linea, para que cada secuencia quede en un elemento de una lista.
sequences = content.split('\n')

# Abrir el archivo para el fasta
fasta = open("results/sequences_fasta.txt", 'w')

# Recorrer cada elemento de la lista.
# Antes que nada se debe agregar el > al nombre de la secuencia.
# De cada elemento, separar la parte de "seq#" de la secuencia y eso mandarlo a otra lista para poder recorrer esta ultima y dar el formato fasta.
# Con replace y upper hacer las modificaciones pertinentes.
for sequence in sequences:
    seq = sequence.replace(F"{sequence}", F"> {sequence}")
    template = seq.split('   ')
    for t in template:
        if t == "> seq_1" or t == "> seq_2" or t == "> seq_3":
            fasta.write(F"{t}\n")
        else:
            x = t.upper().replace("-", "", 1000)
            fasta.write(F"{x}\n")

# Cerrar el archivo
fasta.close()
