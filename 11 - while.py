respuesta = None

while respuesta != 'A' and respuesta != 'B' and respuesta != 'C':
    respuesta = input("Que opcion prefires? [A, B, C] -> ")

if respuesta == "A":
    print('Bien hecho eres ' + respuesta)
elif respuesta == 'B':
    print('Perteneces a ' + respuesta)
elif respuesta == 'C':
    print('Elegiste el último, ' + respuesta)
else:
    print('No haz seleccionado alguna de las resuestas posibles')