primer_nota = int(input("Ingresa el primer nota: "))
segundo_nota = int(input("Ingresa el segundo nota: "))
promedio = (primer_nota + segundo_nota) / 2

if promedio >= 8:
    print("Promociona")
elif 8 > promedio >= 4:
    print("Va a final")
else:
    print("Reprueba")