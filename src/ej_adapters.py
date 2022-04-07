'''
NAME
    ej_adapters

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que quita los adaptadores de secuencias, sabiendo que dichos adaptadores: van de la posicion 1 a la 14 y que conservan la secuencia.

USAGE
    null

ARGUMENTS
    null
'''
# Guardar las secuencias como una cadena y no como lista.
file = open('data/input_adapters.txt')
content = file.read()

# Cortar la cadena con la secuencia del adaptador. Dicha secuencia la conozco, va de posicion 1 a 14. Guardar la secuencia cortada en una lista.
sequences = content.split('ATTCGATTATAAGC')

# Abrir el archivo
no_adapters = open("results/no_adapters.txt", 'w')

# Recorrer la lista de las secuencias sin adaptador e ir guardando cada elemento (secuencias) en un archivo
for sequence in sequences:
    if (sequence != ""):  # evita que agregue renglones en blanco
        sequence.strip('\n')
        no_adapters.write(sequence)

# Cerrar el archivo
no_adapters.close()
