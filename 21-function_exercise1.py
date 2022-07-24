import platform

my_system = platform.uname()

def main(variable):
    if my_system.system == "Linux":
        opinion = "eres un programador eh"
    elif my_system.system == "Windows":
        opinion = "eres una windowsFans"
    print("Buenos dias {}\nVeo que hoy vamos a trabajar con {}\n{}".format(variable, my_system.system, opinion))


if __name__ == "__main__":
    main("Carlitos")