'''
NAME
    Secuencias de calidad

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime las secuencias que cumplan con un umbral en cada una de sus bases

USAGE
    py src/calidadFastq.py

ARGUMENTS
'''
import argparse
from Bio import SeqIO
import os

# crear parseo y parametros
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--umbral",
                    help="umbral de score para las bases", required=True)
parser.add_argument("-f", "--direccion",
                    help="direccion del archivo fastq", required=True)

# funcion que encuentre las secuencias que cumplan con el umbral en cada una de sus bases


def getSeqsUmbral(archivo, umbral):
    numSecuencias = 0
    # crear archivo de salida
    fasta = open("results/sampleUmbral.fasta", 'w')
    # recorrer cada secuencia
    for record in SeqIO.parse(archivo, "fastq"):
        # recorrer cada score de cada base
        for i in range(0, len(record.letter_annotations["phred_quality"])):
            # ver si respetan el umbral
            if record.letter_annotations["phred_quality"][i] < umbral:
                break
            # escribir secuencia en archivo
            if i == len(record.letter_annotations["phred_quality"]) - 1:
                numSecuencias += 1
                fasta.write(F"{record.id}\n{record.seq}\n\n")

    print(F"Numero de secuencias que cumplen = {numSecuencias}")
    # cerrar archivo de salida
    fasta.close()
    if numSecuencias > 0:
        print(F"archivo de salida en: results/sampleUmbral.fasta")
    else:
        os.remove("results/sampleUmbral.fasta")


getSeqsUmbral(parser.parse_args().direccion,
              int(parser.parse_args().umbral))
