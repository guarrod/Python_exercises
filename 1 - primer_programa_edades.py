nombre = input('Cual es tu nombre? ')
nacimiento = int(input('En que año naciste? '))
print('Genial ' + nombre)
edad = 2022 - nacimiento
hermana = input('Ahora indicame el nombre de tu herman@ ')
nacimientohermana = int(input('Perfecto, ahora dime en que año nació ' + hermana + ' '))
edadhermana = 2022 - nacimientohermana
print('Listo ' + str(nombre) + ' Ahora se que tienes ' + str(edad) + ' años Y que tu herman@ ' + str(hermana) + ' tiene ' + str(edadhermana) + ' años')
mayoredad = max(edad, edadhermana)
menoredad = min(edad, edadhermana)
diferenciaedad = mayoredad - menoredad
print('Además se que el mayor tiene ' + str(mayoredad) + ' años y que la diferencia de edad entre ustedes es de ' + str(diferenciaedad) + ' años')