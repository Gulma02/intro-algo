count_pares = 0
count_impares = 0
ultimo_numero = 0

while ultimo_numero != -1:
    ultimo_digito_patente = int(input("Digite el último numero de la patente: "))

    if ultimo_digito_patente == -1:
        continue

    if ultimo_digito_patente % 2 == 0:
        count_pares += 1
    else:
        count_impares += 1

print("Pares totales: ", count_pares)
print("Impares totales: ", count_impares)