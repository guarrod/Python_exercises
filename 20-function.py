from datetime import datetime

now = datetime.now()

def main():
    name = input("Cual es tu nombre?: ")
    print("Hola {} Hoy es {} y la hora actual {} Tienes tareas pendientes".format(name, now.strftime("%d/%m/%y"), now.strftime("%X")))


if __name__ ==  "__main__":
    main() 
