year = int(input("Ingrese el año que desea saber si es bisiesto: "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("No es bisiesto")
    else:
        print("Es bisiesto")
else:
    print("No es bisiesto")

