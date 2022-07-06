frase = "Esta es la frase de prueba, tenemos que contar los puntos. las comas, y los espacios en la misma."
spaces_count = 0
comma_count = 0
dot_count = 0

for a in frase:
    if a == " ":
        spaces_count += 1
    elif a == ",":
        comma_count += 1
    elif a == ".":
        dot_count += 1


#print("numero de vocales encontradas: {}".format(num_vocales))
print("En estas cantidades: ")
print("Espacios: {}".format(spaces_count))
print("Comas: {}".format(comma_count))
print("Puntos: {}".format(dot_count))
