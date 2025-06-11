cantidad_alumnos_panaderia = 6
cantidad_alumnos_pasteleria = 6
cantidad_alumnos_chef = 2
mas_alto = 6

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