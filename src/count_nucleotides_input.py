# SE DEBE CORRER EL PROGRAMA DESDE LA CARPETA PYTHON_CLASS

# nombre del archivo en variable
my_file_name = 'data/dna.txt'

# abrir el archivo
my_file = open(my_file_name)
print(my_file)

# leer el contenido del archivo
my_file_content = my_file.read().rstrip('\n')

# mostrar el contenido del archivo
print(my_file_content)

# contar la longitud de la cadena
data_lenght = len(my_file_content)

print(f"La longitud de la secuencia {my_file_content} es: {data_lenght}")
