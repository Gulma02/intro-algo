primer_numero = 0
ultimo_numero = 0
end = False
while not end:
    numero = int(input("Introduce un numero: "))

    if numero == -1:
        end = True
        continue

    if primer_numero is None:
        primer_numero = numero
        continue

    ultimo_numero = numero


print(f"El primer numero es: {primer_numero}")
print(f"El ultimo numero es: {ultimo_numero}")