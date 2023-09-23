
dicc = {"fruta1" : "manzana", "fruta2" : "pera", "fruta3" : "frutilla"}
print(dicc)

dic2 = {"ciudad1" : "Paris", "ciudad2" : "Nueva York", "ciudad3" : "Buenos Aires"} 
dic2["ciudad4"] = "Resistencia"
print(dic2)

print(dic2["ciudad2"])

set1 = {1,2,3,4,5,6,7,8,9,10}
print(max(set1))

set1 = (1,3,5,7,9)
print(len(set1))

lista1  = [1,2,3,4,5,6,7,8,9,10]

print(lista1[: -1 ])

lista2 = ["pera", "manzana", "aguacate"]
lista2.remove("manzana")
print(lista2)

tupla = (1,2,3,4,5)
suma = 0
for n in tupla:
    suma += n
print(suma)

#NUEVOS CAMBIOS PARA GIT

#CON NOTAS DETERMINADAS
notas = [6,8,8,8,9]
suma = 0
for n in notas:
    suma += n
print("Promedio: ", suma/len(notas))


#CON NOTAS DEFINIDAS POR EL USUARIO 
cant_notas = int(input("Cantidad de notas: "))
notas = []
suma = 0
for n in range(1, cant_notas + 1):
    notas.append(int(input("Dime tu nota: ")))

print("Promedio: ", sum(notas)/cant_notas)