'''
NAME
    Porcentaje de un aa en una secuencia.

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime la suma de los porcentajes de aminoacidos en una secuencia

USAGE


ARGUMENTS
    null
'''

# guardar parametros en variables y pasar a mayuscula la secuencia
secuencia = input(
    "introduce la secuencia en la cual se buscaran tus aminoacidos: ").upper()
aa_s = input("Introduce los aminoacidos a buscar: ")


# funcion para calcular porcentaje
def porcentaje_aa(secuencia, aa_s=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    porcentaje = 0
    for aa in aa_s:
        long = len(secuencia)
        porcentaje += secuencia.count(aa) / long * 100
    return (porcentaje)


# imprimir porcentaje
if aa_s:
    print(porcentaje_aa(secuencia, aa_s.upper()))
else:
    print(porcentaje_aa(secuencia))

# hacer las pruebas
try:
    assert porcentaje_aa("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
    assert porcentaje_aa("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
    assert porcentaje_aa("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
    assert porcentaje_aa("MSRSLLLRFLLFLLLLPPLP") == 65
    print("todo funciona bien")
except:
    print("Existe un error")
