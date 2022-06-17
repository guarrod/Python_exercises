import random
from time import sleep

random_bit = random.getrandbits(1)  #Genera un bit aleatorio 0/1
random_boolean = bool(random_bit)   #Combierte el bit en un valor booleano

numero_pregunta_aleatorio = random.randint(1, 30)


saludo = "\nBienvenido al juego de Escape de la mazmorra"
print(saludo + "\n" + "-" * len(saludo) + "\n")

print("Esta es la sitación, acabas estás escapando de una orda de Vikingos\nque te persiguen, y en el camino encuentras una gran pared en donde\nhay una puerta y una escotilla en el piso, cual decides tomar?")
begin = input("(P)uerta ó (E)scotilla? > ")

if begin == "P":
    print("\nAl entrar te das cuenta de que alguien se está acercando por el pasillo,\ntienes que tomar una decisión.")
    esconderse_correr = input("""Puedes esconderte detrás de la puerta o salir corriendo en la dirección\nque seguiría el Guardia.
(E)sconderme ó (C)Correr > """)
    if esconderse_correr == "E":
        print("El Guardia Vikingo te encontró y te mató")
    elif esconderse_correr == "C":
        if random_boolean == True:
            print("Corriste por el pasillo y al final habia una puerta que atravesaste y pudiste escapar")
        elif random_boolean == False:
            print("Corriste por el pasillo y al final habia una puerta que atravesaste y moriste")
elif begin == "E":
    print("Acabas de entrar en la escotilla y hay un tunel que debes de recorrer")
    sleep(4)
    print("Empiezas a caminar y ves que el pasillo es largo, húmedo y oscuro")
    sleep(4)
    print("Vez que más adelante hay un área con un claro de luz")
    sleep(4)
    print("Al llegar al claro vez que hay un garrote reposando contra la pared y parece algo pesado y tienes que decidir si lo vas a tomar")
    sleep(6)
    palo = input("(T)omar el palo ó (D)ejar el palo > ")
    if palo == "T":
        palo = True
    elif palo == "D":
        palo = False
    print("Tomaste tu decisión, ahora sigues caminando hasta que te topas con una Rata de 2 metros")
    sleep(5)
    print("La rata te ofrece una opción, si contestas bien a su pregunta te dejará pasar para ser libre, pero si fallas te bloqueará el paso y podrías quedar atrapado para siempre")
    sleep(8)
    print("La pregunta es la siguiente")
    sleep(3)
    print("Cuanto es 2 * " + str(numero_pregunta_aleatorio))
    respuesta = int(input("Cual es tu respuesta? > "))
    if respuesta == (2 * numero_pregunta_aleatorio):
        print("Bien respondido, sigue por este pasillo y llegarás a la libertad")
    elif respuesta != (2 * numero_pregunta_aleatorio):
        print("Haz fallado! ahora te quedarás conmigo para siempre en este tunel oscuro")
        sleep(5)
        if palo == True:
            print("Pero recuerdas que tienes el garrote! y decides amazar a palo a la rata y poder seguir adelante")
            sleep(5)
            print("Decides molerlo a palo y logras salir de ese tunel y escapar")
            sleep(4)
            print("FIN")
        elif palo == False:
            print("Recuerdas que si hubieras tomado el palo hubieras podido matar a la rata y escapar, asi que pasaste la vida encerrado y estiraste la patita")
            sleep(8)
            print("FIN")




