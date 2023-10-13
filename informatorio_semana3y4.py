def cadena_invertida(cadena):
    return cadena[::-1]


print(cadena_invertida("Hola"))


def es_divisible(a, b):
    if a % b == 0:
        print(f"{a} es divisible por {b}")
    else:
        print(f"{a} NO es divisible por {b}")


es_divisible(7, 10)


def imprimir_pares(n):
    lista = []
    for num in range(n):
        if num % 2 == 0:
            lista.append(num)
        else:
            continue
    return lista


print(imprimir_pares(100))


def promedio(*args):
    return sum(args) / len(args)


print(promedio(2, 4, 8, 9, 10))

def factorial(numero):
    total = numero
    for n in range(1, numero):
        total *= n
    return total

print(factorial(5))

