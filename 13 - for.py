vocales = ["a", "e", "i", "o", "u"]
frase = "Hola, hoy estoy aprendiendo Python como lenguaje de programacion"
num_vocales = 0
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for letra in frase:
    if letra in vocales:
        print("He encontrado una: " + letra)
        num_vocales += 1
        if letra == "a":
            a_count += 1
        if letra == "e":
            e_count += 1
        if letra == "i":
            i_count += 1
        if letra == "o":
            o_count += 1
        if letra == "u":
            u_count += 1

print("numero de vocales encontradas: {}".format(num_vocales))
print("En estas cantidades: ")
print("a: {}".format(a_count))
print("e: {}".format(e_count))
print("i: {}".format(i_count))
print("u: {}".format(u_count))
print("o: {}".format(o_count))
