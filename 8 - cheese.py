
saludo = "\nBienvenido al test sobre el queso ♥"
print(saludo + "\n" + "-" * len(saludo) + "\n")

puntuacion = 0


opcion = input("""Pregunta 1: Que haces cuando ves una tabla de quesos?
A - Salgo corriendo
B - Pruebo uno de los quesos o incluso varios
C - No puedo evitar devorarla
Respuesta: """)

if opcion == "A":
    puntuacion = puntuacion + 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B o C")
    exit()

opcion = input("""Pregunta 2: Como te gusta la hamburguesa
A - Sin queso
B - Con queso
C - Pan y queso
Respuesta: """)

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B o C")
    exit()

opcion = input("""Pregunta 3: Eres intolerante a la lactosa? 
A - Si
B - A veces
C - No
Respuesta: """)

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B o C")
    exit()

if puntuacion >= 25:
    print("\nFelicidades, eres fanático del queso")
elif puntuacion >= 15:
    print("\nFelicidades, eres una persona que le gusta el queso")
else:
    print("\nCreo que no te gusta el queso")


