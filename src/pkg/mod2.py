# funcion para mandar una secuencia a fasta
def fasta(seq):
    # Abrir un archivo en carpeta data y escribir la seencia con formato FASTA
    fasta = open("results/mod.fasta", 'w')
    fasta.write(F">sequence_name\n{seq}")
    # Cerrar el archivo
    fasta.close()
    # Dar mensaje al usuario de donde se encuentra el resultado
    print(F"La secuencia en FASTA se encuentra en results/mod.fasta\n")
    return 0
