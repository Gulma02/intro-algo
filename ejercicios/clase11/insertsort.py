import random
lista = []

def carga_datos(nums):
    for i in range(nums):
        lista.append(random.randint(1, 1000))

def insertsort():
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1
        while j >= 0 and valor < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor

carga_datos(int(input("Ingrese la cantidad de numeros deseados: ")))
insertsort()
print(lista)