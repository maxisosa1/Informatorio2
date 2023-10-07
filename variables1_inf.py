palabra = input("Dame una palabra: ")
for letra in palabra:
    print(letra)

numero = int(input("Dame un número: "))
contador = 1
suma = 0
while contador <= numero:
    suma += contador
    contador += 1
print(suma)

contador = 1
while contador <= 10:
    print(numero*contador)
    contador += 1

numero = 100
contador = 1
lista = []
for n in range(101):
    if n % 2 == 0:
        lista.append(n)
print(lista)

suma = 0
for n in lista:
    suma += n
print(suma)

# Solicita al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Convierte la palabra a minúsculas para que la comparación sea insensible a mayúsculas
palabra = palabra.lower()

# Invierte la palabra utilizando el operador de slicing [::-1]
palabra_invertida = palabra[::-1]

# Comprueba si la palabra original es igual a la palabra invertida
if palabra == palabra_invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")

frase = input("Dame una frase: ")
contador = 0
for n in frase:
    if n == " ":
        contador += 1
print(contador + 1)