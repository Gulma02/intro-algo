# Constantes del sistema
carreras = ["Arquitectura", "Sistemas", "Administración", "Economía", "Ingeniería"]

# Lista con inscriptos
total_inscriptos = [0, 0, 0, 0, 0]
mayor_cantidad_inscriptos = 0

"""
Suma el alumno al contador según el indice ingresado previamente.
"""
def registrar_alumno(carrera, mayor_c_inscriptos):
    match carrera:
        case 1:
            total_inscriptos[0] += 1
            if total_inscriptos[0] > mayor_c_inscriptos:
                mayor_c_inscriptos += total_inscriptos[0]
        case 2:
            total_inscriptos[1] += 1
            if total_inscriptos[1] > mayor_c_inscriptos:
                mayor_c_inscriptos = total_inscriptos[1]
        case 3:
            total_inscriptos[2] += 1
            if total_inscriptos[2] > mayor_c_inscriptos:
                mayor_c_inscriptos = total_inscriptos[2]
        case 4:
            total_inscriptos[3] += 1
            if total_inscriptos[3] > mayor_c_inscriptos:
                mayor_c_inscriptos = total_inscriptos[3]
        case 5:
            total_inscriptos[4] += 1
            if total_inscriptos[4] > mayor_c_inscriptos:
                mayor_c_inscriptos = total_inscriptos[4]

    return mayor_c_inscriptos
"""
Recorre e imprime la lista de carreras con su indice.
"""
def mostrar_carreras():
    for i in range(len(carreras)):
        print(f"[{i + 1}] {carreras[i]}")

"""
Valida el indice ingresado
"""
def validar_indice(indice):
    return 1 <= indice <= 5

"""
Valida la edad ingresada.
"""
def validar_edad_alumno(edad):
    return 17 <= edad <= 60


"""
Muestra la cantidad de inscriptos por carrera
"""
def mostrar_inscriptos_por_carrera():
    print("Total inscriptos por carrera:")
    for i in range(len(carreras)):
        print(f"Se inscribieron {total_inscriptos[i]} a la carrera de {carreras[i]}.")

"""
Porcentaje inscriptos
"""
def mostrar_porcentaje_por_carrera():
    print("Porcentaje de inscriptos por carrera: ")
    # Contador
    suma_inscriptos = 0
    for i in range(len(carreras)):
        suma_inscriptos += total_inscriptos[i]

    for i in range(len(carreras)):
        print(f"La carrera {carreras[i]} tuvo un {total_inscriptos[i]/suma_inscriptos * 100}% de inscriptos sobre el total.")

"""
Se encarga de mostrar la carrera con más inscriptos luego de haberla ordenado
"""
def carrera_con_mas_inscriptos():
    primer_indice = 0
    for i in range(len(carreras)):
        if total_inscriptos[i] == mayor_cantidad_inscriptos:
            primer_indice = i
            break

    if primer_indice == 4:
        print(f"La carrera con mas inscriptos es: {carreras[len(carreras)-1]}")
    else:
        carreras_string = ""
        for i in range(primer_indice, len(carreras)):
            carreras_string += " " + carreras[i]

        print(f"Las carreras con más inscriptos son: {carreras_string}")


"""
Ordena por cantidad de inscriptos a las carreras
"""
def ordenar_por_inscriptos():
    for i in range(len(carreras)):
        for j in range(i + 1, len(carreras)):
            if total_inscriptos[i] > total_inscriptos[j]:
                carreras[i], carreras[j] = carreras[j], carreras[i]
                total_inscriptos[i], total_inscriptos[j] = total_inscriptos[j], total_inscriptos[i]

"""
Muestra las carreras según cantidad de inscriptos de mayor a menor
"""
def mostrar_carreras_mayor_menor():
    indices = [-1, -2, -3, -4, -5]
    print("Listado de mayor a menor: ")
    for num in indices:
        print(f"{carreras[num]}: {total_inscriptos[num]}")

seguir_registrando = 0
while not seguir_registrando == -1:
    mostrar_carreras()
    print("[-1] Para salir")
    seguir_registrando = int(input("Ingrese el indice de carrera al que quiere inscribir al alumno: "))

    if seguir_registrando == -1:
        continue

    if not validar_indice(seguir_registrando):
        print("El indice ingresado no es valido.")
        continue

    while not validar_edad_alumno(int(input("Ingrese su edad: "))):
        print("Ingrese una edad entre 17 y 60 años.")

    mayor_cantidad_inscriptos = registrar_alumno(seguir_registrando, mayor_cantidad_inscriptos)

mostrar_inscriptos_por_carrera()
mostrar_porcentaje_por_carrera()
ordenar_por_inscriptos()
carrera_con_mas_inscriptos()
mostrar_carreras_mayor_menor()


