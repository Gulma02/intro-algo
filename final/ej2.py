lista_temperaturas = []
dias_mayores_a_30 = 0
posicion_mayor_temperatura = 0
posicion_menor_temperatura = 0

for i in range(7):
    nueva_temperatura = -21
    while nueva_temperatura <= -20 or nueva_temperatura >= 60:
        nueva_temperatura = int(input("Ingrese el nueva temperatura: "))

        if nueva_temperatura <= -20 or nueva_temperatura >= 60:
            print("Por favor ingrese un valor permitido.")

    lista_temperaturas.append(nueva_temperatura)
    if nueva_temperatura > 30:
        dias_mayores_a_30 += 1

    if lista_temperaturas[i] > lista_temperaturas[posicion_mayor_temperatura]:
        posicion_mayor_temperatura = i

    if lista_temperaturas[i] < lista_temperaturas[posicion_menor_temperatura]:
        posicion_menor_temperatura = i

suma_temperaturas = 0
for i in range(len(lista_temperaturas)):
    suma_temperaturas += lista_temperaturas[i]

print(f"El promedio de temperaturas fue de {suma_temperaturas/len(lista_temperaturas)}")
print(f"{dias_mayores_a_30} tuvieron más de 30 grados")
print(f"Un {dias_mayores_a_30/len(lista_temperaturas)*100}% de días tuvieron más de 30 grados")
print(f"El día {posicion_mayor_temperatura} fue el día con la temperatura máxima")
print(f"El día {posicion_menor_temperatura} fue el día con la temperatura minima")