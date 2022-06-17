saludo = "Bienvenido a tu ayudante para elegir tu nuevo movil"
print(saludo + "\n" + "-" * len(saludo) + "\n")

tipo = input("""Que tipo de móvil deseas?"
A - Android
B - IOS\n""")

if tipo == "A":
    dinero = input("Tienes dinero? [S/N]")
    if dinero == "S":
        camara = input("Te importa la cámara del movil? [S/N]")
        if camara == "S":
            print("Tu opción correcta es el Google Pixel Supercamara")
        elif camara == "N":
            print("Deberias de adquirir un movil calidad-precio")
    elif dinero == "N":
        print("Mejor busca un Android Chino de 100$")
elif tipo == "B":
    dinero = input("Tienes dinero? [S/N]")
    if dinero == "S":
        print("Ve por un Iphone Ultra Pro Max")
    elif dinero == "N":
        print("Buscate un Iphone de segunda mano")
