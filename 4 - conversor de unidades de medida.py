
print("Bienvenido al conversor de unidades de medidas")
opcion = input("""
Indica que tipo de conversion deseas hacer
A - Metros a centimetros
B - Centimetros a metros
C - Metros a Kilometros
D - pulgadas a centimetros\n""")

texto_solicitud = "indcanos cuantos {} deseas convertir a {}: "

if opcion == "A":
    solicitud_numero = float(input(texto_solicitud.format("metros","centimetros")))
    print(str(solicitud_numero) + " metros equivalen a " + str(solicitud_numero * 100) + " centimetros")
elif opcion == "B":
    solicitud_numero = float(input(texto_solicitud.format("centimetros","metros")))
    print(str(solicitud_numero) + " centimetros equivalen a " + str(solicitud_numero / 100) + " metros")
elif opcion == "C":
    solicitud_numero = float(input(texto_solicitud.format("metros","kilometros")))
    print(str(solicitud_numero) + " metros equivalen a " + str(solicitud_numero / 1000) + " kilometros")
elif opcion == "D":
    solicitud_numero = float(input(texto_solicitud.format("pulgadas","centimetros")))
    print(str(solicitud_numero) + " metros pulgadas a " + str(solicitud_numero * 2.54) + " centimetros")
else:
    print("No ha seleccionado una opción válida")