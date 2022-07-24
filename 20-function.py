from datetime import datetime

now = datetime.now()

def main(mood):
    name = input("Cual es tu nombre?: ")
    largo = 0
    for n in mood:
        largo +=1
    print("Hola {}, Hoy es {} y nuestro mood de hoy será {} y el mood tiene {} letras".format(name, now.strftime("%d/%m/%y"), mood, largo))
    return largo


if __name__ ==  "__main__":
    main("Dia lluvioso") 
