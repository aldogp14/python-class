'''
NAME
    Regiones ricas en AT

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que busca regiones ricas de ATs 

USAGE
    py src/at_region_rica.py [-h] -f str -s int

ARGUMENTS
    -f: direccion de donde se encuentra el archivo con la secuencia
    -s: numero que indica la region minima a buscar de ATs
'''

# importar modulos
import argparse
import re

# crear parametros
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--direccion",
                    help="direccion de la secuencia de DNA", required=True)
parser.add_argument("-s", "--region_min",
                    help="region minima a buscar de ATs", required=True)
args = parser.parse_args()
# guardar parametros en variables
direccion = args.direccion.upper()
region_min = args.region_min

# crear funcion que encuentre las regiones ricas


def finder(secuencia, region_min):
    # ver si hay coincidencias
    if re.search("[A|T]{" + region_min + ",}", secuencia):
        coincidencias = re.finditer(r"[A|T]{" + region_min + ",}", secuencia)
        type(coincidencias)
        # ver si hay coincidencias
        for c in coincidencias:
            type(c)
            region = c.group()
            pos = c.span()
            print(region + " se encontro en la posicion: " + str(pos))
        print("\n")
    # si no hay coincidencias avisar al usuario
    else:
        print("No hay coincidencias\n")
    archivo.close()


# crear funcion para ver la integridad de la secuencia
def int_secuencia(secuencia):
    # ver si hay caracteres distintos
    if re.search(f"[^ATCG]", secuencia):
        print("Hay caracteres diferentes a ATCG:\n")
        coincidencias = re.finditer(r"[^ATCG]", secuencia)
        type(coincidencias)
        for c in coincidencias:
            type(c)
            caracter = c.group()
            pos = c.start()
            print(caracter + " en la posicion " + str(pos))
        print("\n")
        archivo.close()
        quit()
    # si la secuencia esta "sana" enviar a la funcion de busqueda
    else:
        finder(secuencia, region_min)


# ver si la direccion es correcta
try:
    archivo = open(direccion)
except IOError as ex:
    print(F"El archivo {ex.filename} no se encuentra\n")
    quit()

else:
    secuencia = archivo.read().rstrip('\n')
    int_secuencia(secuencia)
