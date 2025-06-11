# ENTRADA
monto_previsto = int(input("Ingrese el monto total previsto: "))

# ACUMULADORES
monto_total = 0
monto_total_pares = 0

# CONTADORES
cantidad_gastos = 0
cantidad_montos_pares = 0
cantidad_montos_menores_veinticinco = 0

# CONDICIONALES
seguir_preguntando = True

while seguir_preguntando:
    nuevo_monto = int(input("Ingrese un nuevo gasto. Ingrese -1 para finalizar:"))
    if nuevo_monto == -1:
        seguir_preguntando = False
    else:
        if nuevo_monto % 2 == 0:
            cantidad_montos_pares += 1
            monto_total_pares += nuevo_monto

        if nuevo_monto <= 25000:
            cantidad_montos_menores_veinticinco += 1

        monto_total += nuevo_monto
        cantidad_gastos +=1

if monto_previsto > monto_total:
    print("La empresa se ha mantenido dentro de los límites de gastos.")
elif monto_previsto < monto_total:
    print("Ha excedido el límite de gastos")
else:
    print("Ha igualado el monto total de gastos previsto.")
    
print(f"Se realizaron {cantidad_montos_pares} gastos con montos pares")
if cantidad_montos_pares != 0:
    print(f"Con un monto promedio de {monto_total_pares / cantidad_montos_pares}")

print(f"Se han realizado un {cantidad_montos_menores_veinticinco / cantidad_gastos * 100}% de gastos no superiores a 25.000$")