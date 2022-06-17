from random import randint
import time

# Personaje
vida_inicial_pikachu = 80
vida_pikachu = vida_inicial_pikachu

# Ataques
# Bola voltio = 10
# Onda trueno = 11

# Personaje
vida_inicial_squirtle = 90
vida_squirtle = vida_inicial_squirtle
# Ataques
# Placaje = 10
# Pistola de Agua = 12
# Burbuja = 9


tamano_barra = 20

print('\n\nVa a empezar la batalla la vida de Pikachu es {} y la vida de Squirtle es {}'.format(vida_pikachu,
                                                                                                vida_squirtle))

while vida_pikachu > 0 and vida_squirtle > 0:
    # Empieza Pikachu

    print('\n Turno de Pikachu ')
    print('------------------')
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print('Pikachu ataca con Bola voltio')
        vida_squirtle -= 10
    elif ataque_pikachu == 2:
        print('Pikachu ataca con Onda trueno')
        vida_squirtle -= 11

    barra_de_vida_pikachu = int(vida_pikachu * tamano_barra / vida_inicial_pikachu)
    barra_de_vida_squirtle = int(vida_squirtle * tamano_barra / vida_inicial_squirtle)

    print('La vida de Pikachu es: [{}{} - {}/{}], \nla vida de Squirtle es [{}{} - {}/{}]'.format(
        "█" * barra_de_vida_pikachu, "░" * (tamano_barra - barra_de_vida_pikachu), vida_pikachu, vida_inicial_pikachu,
        "█" * barra_de_vida_squirtle, "░" * (tamano_barra - barra_de_vida_squirtle), vida_squirtle, vida_inicial_squirtle))

    # Turno de Squirtle
    print('\n Turno de Squirtle ')
    print('-------------------')

    
    ataque_squirtle = None
    # while ataque_squirtle != 1 and ataque_squirtle != 2 and ataque_squirtle != 3:
    while ataque_squirtle not in [1, 2, 3]: # mejora de la linea anterior usando una lista
        ataque_squirtle = int(input('Selecciona tu ataque [1 - Placaje(10), 2 - Pistola de Agua(12), 3 - Burbuja(9)]: '))
    if ataque_squirtle == 1:
        print('Squirtle ataca con Placaje')
        vida_pikachu -= 10
    elif ataque_squirtle == 2:
        print('Squirtle ataca con Pistola de Agua')
        vida_pikachu -= 12
    elif ataque_squirtle == 3:
        print('Squirtle ataca con Burbuja')
        vida_pikachu -= 9

    barra_de_vida_pikachu = int(vida_pikachu * tamano_barra / vida_inicial_pikachu)
    barra_de_vida_squirtle = int(vida_squirtle * tamano_barra / vida_inicial_squirtle)

    print('La vida de Pikachu es: [{}{} - {}/{}], \nla vida de Squirtle es [{}{} - {}/{}]'.format(
        "█" * barra_de_vida_pikachu, "░" * (tamano_barra - barra_de_vida_pikachu), vida_pikachu, vida_inicial_pikachu,
        "█" * barra_de_vida_squirtle, "░" * (tamano_barra - barra_de_vida_squirtle), vida_squirtle, vida_inicial_squirtle))

    # Espera 3seg para que pikachu ataque
    time.sleep(3)


if vida_pikachu > vida_squirtle:
    print('\n\nEl vencedor es Pikachu, haz perdido!')
elif vida_squirtle > vida_pikachu:
    print('\n\nEl vencedor es Squirtle, haz GANADO!')


