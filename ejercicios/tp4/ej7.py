suma = 0
maximo = 0
posicion = 0
for i in range(10):
    numero = int(input("ingrese un numero: "))
    if numero > maximo:
        posicion = i
        maximo = numero

    suma += numero


print("Promedio: ", suma / 10)
print("maximo: ", maximo)
print("posicion: ", posicion)