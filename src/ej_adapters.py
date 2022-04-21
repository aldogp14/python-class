'''
NAME
    ej_adapters

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que quita adaptadores que van de la posicion 1 a 14 de secuencias.
USAGE
    py ej_adapters.py

ARGUMENTS
    null
'''
# Guardar las secuencias como una como lista.
file = open('data/input_adapters.txt', 'r')
sequences = file.readlines()
file.close()

# Abrir el archivo
no_adapters = open("results/no_adapters.txt", 'w')

# Recorrer la lista de las secuencias y excluir el adaptador.
for sequence in sequences:
    sequence.strip('\n')
    no_adapters.write(F"{sequence[14:]}")

# Cerrar el archivo
no_adapters.close()
