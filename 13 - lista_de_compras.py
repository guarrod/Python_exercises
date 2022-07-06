lista = []
item = None

print("Programa de lista de compras\n")

# while item != "Q":
while True: # Mejora de la linea anterior
    item = input("Que desea comprar? ([Q] para salir): ")
    if item == "Q":
        break
    elif item in lista:
        print("{} ya está en la lista".format(item))
    else:
        if input("Seguro que desea añadir {} a la lista? [S]i o [N]o: ".format(item)) == "S":
            lista.append(item)

print("La lista de compra es:")
print(lista)    