import random

numero_ganador = random.randint(1, 10)
numero_elegido = int(input("Elige un numero entre el 1 y 10: "))

if numero_elegido == numero_ganador:
    print("Haz ganado! ♥")
if numero_elegido > 10:
    print("Te haz pasado! el numero debe ser menor que 11")

print("El numero ganador era " + str(numero_ganador) + " casi le atinas")
# print("El numero ganador era: {}".format(numnero_ganador))