# se guarda la direccion del archivo con la secuencia en una variable
nombre_archivo = input("Introduce la direccion del archivo con la secuencia: ")

# se abre un archivo con la direccion
archivo = open(nombre_archivo)

# se guarda el contenido del archivo leido, se quita el salto de linea
contenido = archivo.read().rstrip('\n')

# se guarda la longitud de la cadena
long = len(contenido)

# se sacan los porcentajes
porcentaje_AT = ((contenido.count('A') + contenido.count('T')) / long * 100)
porcentaje_GC = ((contenido.count('G') + contenido.count('C')) / long * 100)

# se imprimen los porcentajes
print(
    F"Porcentaje de AT: {porcentaje_AT}%\nPorcentaje de GC: {porcentaje_GC}%")
