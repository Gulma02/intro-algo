suma = 0
total_numeros = 0

while suma < 100:
    numero = int(input("Ingresa un numero: "))
    if numero % 2:
        suma += numero

    total_numeros += 1

print("Suma: ", suma)
print("Total de numeros: ", total_numeros)