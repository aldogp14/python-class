'''
NAME
    ADN, ARN y proteina de gen Genbank

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprimela secuencia ADN, ARN y proteica de un gen que este en un archivo genbank

USAGE
    py src/secuenciasGenbank.py 

ARGUMENTS
'''
# importar librerias
from Bio import SeqIO
from Bio.Seq import Seq

# guardar el gen a buscar como lista
gen = ['L']
# guardar la lectura del archivo genbank
x = SeqIO.read('data/virus.gb', 'genbank')

# recorrer los genes
for i in range(2, len(x.features), 2):
    # ver si el gen del indice es el que se busca
    if x.features[i].qualifiers['gene'] == gen:
        # guardar la secuencia con las posiciones de inicio y final
        sec = Seq(x.seq[x.features[i].location.nofuzzy_start:
                        x.features[i].location.nofuzzy_end])
        # imprimir el output
        print('Secuencia: ', sec)
        print('\nTranscripcion: ', sec.transcribe())
        print('\nTraduccion: ', sec.translate(), '\n')
