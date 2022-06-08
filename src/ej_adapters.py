'''
NAME
    ej_adapters

VERSION
   1.1

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Programa que quita adaptadores que van de la posicion 1 a 14 de secuencias.
USAGE
    null

ARGUMENTS
    null
'''
# Guardar las secuencias como una como lista.
from typing import IO

# Agregar excepcion en la que la direccion del archivo este mal
try:
    file = open('data/input_adapters.txt')

except IOError as ex:
    print(F"El archivo {ex.filename} no se encuentra\n")
    quit ()
    
else:
    sequences = file.readlines()

    # Abrir el archivo
    no_adapters = open("results/no_adapters.txt", 'w')

    # Recorrer la lista de las secuencias y excluir el adaptador.
    for sequence in sequences:
        sequence.strip('\n')
        no_adapters.write(F"{sequence[14:]}")

    # Cerrar el archivo
    no_adapters.close()

    # Dar mensaje al usuario de donde se encuentra el resultado
    print(F"Las secuencias sin adaptadores se encuentran en results/no_adapters.txt\n")
