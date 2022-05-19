'''
NAME
    Porcentaje de un aa en una secuencia.

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    programa que imprime el porcentaje de un aminoacido en una secuencia

USAGE


ARGUMENTS
    null
'''
secuencia = input(
    "introduce la secuencia en la cual se buscaran tus aminoacidos: ").upper()
aa = input("Introduce el aminoacido a buscar: ").upper()


def porcentaje_aa(secuencia, aa):  # funcion para calcular porcentaje
    long = len(secuencia)
    return(secuencia.count(aa) / long * 100)


# imprimir porcentaje
print(porcentaje_aa(secuencia, aa))

# hacer las pruebas
try:
    assert porcentaje_aa("MSRSLLLRFLLFLLLLPPLP", "M") == 5
    # en este manda error por no estar en mayuscula, sin embargo cuando el usuario lo ingresa de esta forma no hay problema ya que se hace un upper a su input
    assert porcentaje_aa("MSRSLLLRFLLFLLLLPPLP", "r") == 10
    assert porcentaje_aa("msrslllrfllfllllpplp", "L") == 50
    assert porcentaje_aa("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
    print("todo funciona bien")
except:
    print("algo anda mal")
