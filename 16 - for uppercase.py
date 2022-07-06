import string

frase = input("Introduce la frase a analizar: ")
uppercase_count = 0

for a in frase:
    if a in string.ascii_uppercase:
        uppercase_count += 1

print("La frase tiene {} mayusculas".format(uppercase_count))
