cantidad_meses = 6
interes_mensual = 2
interes_total = 1

for i in range(0, cantidad_meses):
    interes_total += interes_total * interes_total * (interes_mensual / 100)

print(f"Su interes total es de {(interes_total - 1) * 100}%")