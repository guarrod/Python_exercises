dolar_euro = 0.91
libra_euro = 1.18
dolar_bolivar = 4.47

opcion = input("""Que desea hacer?
A - Convertir de dolar a euro
B - Convertir de euro a dolar
C - Convertir de libra a euro
D - Convertir de euro a libra
E - Convertir de dolar a bolivar\n""")

texto_usuario = "introduzca la cantidad de {} a convertir: "

if opcion == "A":
    cantidad_de_dinero = float(input(texto_usuario.format("dolares")))
    print("La cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))
elif opcion == "B":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en dolares es: {}".format(cantidad_de_dinero / dolar_euro))
elif opcion == "C":
    cantidad_de_dinero = float(input(texto_usuario.format("libras")))
    print("La cantidad en euros es: {}".format(cantidad_de_dinero * libra_euro))
elif opcion == "D":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en libras es: {}".format(cantidad_de_dinero / libra_euro))
elif opcion == "E":
    cantidad_de_dinero = float(input(texto_usuario.format("dolares")))
    print("La cantidad en bolivares es: {}".format(cantidad_de_dinero * dolar_bolivar))
else:
    print("No ha seleccionado una opción válida")
