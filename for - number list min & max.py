num_list = []


print("Vamos a crar una lista de numeros \nCuando hayas terminado introduce [Q]")

while True:
    character = input("Introduce un numero: ")
    if character == "Q":
        break
    elif character.isnumeric() == True:
        num_list.append(character)
    else:
        print("No haz introducido un valor valido, intentalo de nuevo")
print("Esta es la lista de numeros: {}".format(num_list) + "\nEl menor es {} y el mayor es {}".format(min(num_list), max(num_list)))

