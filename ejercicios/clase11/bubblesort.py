import random

lista = []
def carga_datos(len):
    for i in range(len):
        lista.append(random.randint(1, 1000))

def bubble_sort():
    print(lista)
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i], lista[j])
            if lista[j] > lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
                print(lista)



carga_datos(int(input("Ingrese la cantidad de numeros deseados: ")))
bubble_sort()
print(lista)