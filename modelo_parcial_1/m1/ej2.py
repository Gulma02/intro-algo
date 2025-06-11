legajo = 0
cantidad_alumnos_panaderia = 0
cantidad_alumnos_pasteleria = 0
cantidad_alumnos_chef = 0
total_edades = 0
mas_alto = 0

while legajo != -1:
    while legajo < 1000 or legajo > 9999:
        legajo = int(input("Ingrese el número de legajo: "))

        if legajo == -1:
            break

        if legajo < 1000 or legajo > 9999:
            continue

        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = 0

        while edad < 18 or edad > 65:
            edad = int(input("Ingrese el edad: "))

            if edad < 18 or edad > 65:
                print("Edad invalida. Vuelva a ingresarla.")

        total_edades += edad
        tipo_curso = 0

        while tipo_curso < 1 or tipo_curso > 3:
            print("Elija su tipo de curso: ")
            print()
            print("[1] Panaderia")
            print("[2] Pasteleria")
            print("[3] Chef")
            print()

            tipo_curso = int(input("Ingrese el tipo de curso: "))

        match tipo_curso:
            case 1:
                cantidad_alumnos_panaderia += 1
                if cantidad_alumnos_panaderia > mas_alto:
                    mas_alto = cantidad_alumnos_panaderia
            case 2:
                cantidad_alumnos_pasteleria += 1
                if cantidad_alumnos_pasteleria > mas_alto:
                    mas_alto = cantidad_alumnos_pasteleria
            case 3:
                cantidad_alumnos_chef += 1
                if cantidad_alumnos_chef > mas_alto:
                    mas_alto = cantidad_alumnos_chef

        legajo = 0

print(f"Total alumnos panaderia: {cantidad_alumnos_panaderia}")
print(f"Total alumnos pasteleria: {cantidad_alumnos_pasteleria}")
print(f"Total alumnos chef: {cantidad_alumnos_chef}")

print("Mas alto: ", mas_alto)

total_alumnos = cantidad_alumnos_pasteleria + cantidad_alumnos_chef + cantidad_alumnos_panaderia

print(f"Procentaje alumnos panaderia: {cantidad_alumnos_panaderia/total_alumnos}")
print(f"Procentaje alumnos pasteleria: {cantidad_alumnos_pasteleria/total_alumnos}")
print(f"Procentaje alumnos chef: {cantidad_alumnos_chef/total_alumnos}")

print(f"Promedio edad: {total_edades/total_alumnos}")

if cantidad_alumnos_chef == cantidad_alumnos_pasteleria == cantidad_alumnos_panaderia:
    print("Todos son los más altos y más bajos.")
elif cantidad_alumnos_chef == mas_alto:
    if cantidad_alumnos_chef == cantidad_alumnos_panaderia:
        print("Chef y Panadero son los más altos.")
    elif cantidad_alumnos_chef == cantidad_alumnos_pasteleria:
        print("Chef y Pastelero son los más altos.")
    else:
        print("Chef es el más alto.")
elif cantidad_alumnos_panaderia == mas_alto:
    if cantidad_alumnos_panaderia == cantidad_alumnos_pasteleria:
        print("Panaderia y Pasteleria son las más altas.")
    else:
        print("Panaderia es la más alta.")
else:
    print("Pasteleria es la más alta.")

if not cantidad_alumnos_chef == cantidad_alumnos_pasteleria == cantidad_alumnos_panaderia:
    if cantidad_alumnos_chef <= cantidad_alumnos_pasteleria and cantidad_alumnos_chef <= cantidad_alumnos_panaderia:
        if cantidad_alumnos_chef <= cantidad_alumnos_panaderia:
            print("Chef y Panaderia son los más bajos")
        elif cantidad_alumnos_chef <= cantidad_alumnos_pasteleria:
            print("Chef y Pasteleria son los más bajos")
        else:
            print("Chef es el más bajo")
    if cantidad_alumnos_pasteleria <= cantidad_alumnos_panaderia:
        if cantidad_alumnos_pasteleria == cantidad_alumnos_panaderia:
            print("Pasteleria y panaderia son los más bajos")
        else:
            print("Pasteleria es el más bajo")
    else:
        print("Panaderia es el más bajo")