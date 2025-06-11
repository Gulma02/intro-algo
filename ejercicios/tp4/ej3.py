end = False

min_value = 0
max_value = 0

while not end:
    numero = int(input("Introduce un numero: "))

    if min_value == 0:
        min_value = numero

    if numero == -1:
        end = True
        continue

    if numero > max_value:
        max_value = numero
        continue

    if numero < min_value:
        min_value = numero
        continue


print(f"El numero más chico es: {min_value}")
print(f"El numero más grande es: {max_value}")