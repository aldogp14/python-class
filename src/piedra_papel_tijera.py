'''
NAME
    Piedra papel o tijera

VERSION
   1.0

AUTHOR
    Aldo Garcia Prado

DESCRIPTION
    Prgorama que simula piedra, papel o tijera contra la computadora. La eleccion de la computadora se hace de forma random.

USAGE
    null

ARGUMENTS
    null
'''
import random

# generar numero aleatorio del 1 al 3
num = random.randint(1, 3)
play = "si"


while play.lower() == "si":
    # Pedir la eleccion al usuario
    print("Introduce tu eleccion: piedra, papel o tijera")
    user = input()

    # Asignar una eleccion de piedra, papel o tijera conforme al numero aleatorio
    if num == 1:
        cpu = "piedra"
    elif num == 2:
        cpu = "papel"
    else:
        cpu = "tijera"

    # Cuando las elecciones son iguales, hay un empate.
    if user.lower == cpu:
        print("Empate")
    # Verificar todas las opciones en las que ganas (usuario vs cpu): tijera vs papel || papel vs piedra || piedra vs tijera
    elif (user.lower == "tijera" and cpu == "papel") or (user.lower == "papel" and cpu == "piedra") or (user.lower == "piedra" and cpu == "tijera"):
        print("Ganaste")
    # Si no hubo empate ni tampoco gano el usuario, entonces perdio.
    else:
        print("Perdiste")

    print(F"¿Quieres jugar de nuevo?(si/no)")
    play = input()
