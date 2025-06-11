edad = int(input("Edad: "))
altura = float(input("Altura: "))
peso = int(input("Peso en kg (redondo): "))

if edad != 16 or altura != 1.75 or peso != 70:
    print("No juega")
else:
    print("Juega")