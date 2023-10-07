palabra = input("Dame una palabra: ")
palabra.lower()
palabra = list(palabra)

if "a" not in palabra and "e" not in palabra and "i" not in palabra and "o" not in palabra and "u" not in palabra:
    print("Tu palabra no tiene vocales")
else:
    for letra in palabra:
        indice = palabra.index(letra)
        if letra == "a":
            palabra[indice] = "A"
        elif letra == "e":
            palabra[indice] = "E"
        elif letra == "i":
            palabra[indice] = "I"
        elif letra == "o":
            palabra[indice] = "O"
        elif letra == "u":
            palabra[indice] = "U"

print("".join(palabra))
