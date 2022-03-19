# se guarda la direccion del archivo con la secuencia en una variable
file_name = 'data/dna.txt'

# se abre un archivo con la direccion
file = open(file_name)

# se lee y guarda el contenido del archivo
content = file.read().rstrip('\n')

# se crea el archivo fasta
fasta = open("data/dna.fasta", 'w')

# se escribe el formato de archivo FASTA y se guarda la secuencia
fasta.write(F">sequence_name\n{content}")

# se cierra el archivo
fasta.close()
