import random

lista = []
def carga_datos(len):
    for i in range(len):
        lista.append(random.randint(1, 1000))

def bubble_sort():
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]



carga_datos(int(input("Ingrese la cantidad de numeros deseados: ")))
bubble_sort()
print(lista)