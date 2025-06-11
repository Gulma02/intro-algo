lista = []

def mayor():
    test = lista[0]
    for i in range(len(lista)):
        if lista[i] > test:
            test = lista[i]

    return test

def menor():
    apa = lista[0]
    for i in range(len(lista)):
        if lista[i] < apa:
            apa = lista[i]

    return apa

def listas():
    valor = 0
    while valor != -1:
        valor = int(input("Ingrese un valor: "))
        if valor != -1:
            lista.append(valor)

listas()
print(lista)
print(f"El mayor valor es: {mayor()}")
print(f"El menor valor es: {menor()}")